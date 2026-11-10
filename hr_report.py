import csv
import json
import os
import time
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


# ფაილების მისამართები — pathlib

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "employees.csv"
OUTPUT_DIR = BASE_DIR / "output"


# ლოგის ფუნქცია

def log(message):
    log_path = OUTPUT_DIR / "log.txt"
    timestamp = datetime.now().isoformat()

    with log_path.open("a", encoding="utf-8") as f:
        f.write(f"{timestamp} - {message}\n")


# backup_file() — სარეზერვო ასლი
# ამ ფუნქციის მიზანია ერთი ფაილის მეორეში დაკოპირება.

def backup_file(src, dst):
    copied_lines = 0

    with src.open("r", encoding="utf-8", newline="") as source, \
            dst.open("w", encoding="utf-8", newline="") as destination:
        for line in source:
            destination.write(line)
            copied_lines += 1

    return copied_lines


# გარემოს მომზადება და საწყისი CSV ფაილის შემოწმება

def prepare_environment():
    OUTPUT_DIR.mkdir(exist_ok=True)
    log("პროგრამა დაიწყო")

    if not DATA_FILE.exists():
        print("შეცდომა: data/employees.csv ფაილი ვერ მოიძებნა.")
        return False

    print("CSV ფაილის აბსოლუტური ბილიკი:", DATA_FILE.resolve())
    return True


# lock ფაილის შექმნა

def create_lock():
    lock_path = OUTPUT_DIR / "lock.txt"

    try:
        with lock_path.open("x", encoding="utf-8") as f:
            f.write(datetime.now().isoformat())
        print("Lock ფაილი შეიქმნა.")
    except FileExistsError:
        print("ანგარიში უკვე შექმნილია")


# csv.reader

def show_reader_report(csv_path):
    with csv_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        header = next(reader)
        employees = list(reader)

    print("\nსათაური:")
    print(header)

    print("\nპირველი 3 თანამშრომელი:")
    for employee in employees[:3]:
        print(employee)

    print("\nთანამშრომლების რაოდენობა:", len(employees))


# DictReader-ით ანალიზი და CSV ანგარიშები

def analyze_employees(csv_path, output_dir):
    with csv_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        employees = list(reader)

    department_salaries = defaultdict(list)
    active_employees = []
    active_count = 0
    inactive_count = 0

    for employee in employees:
        salary = int(employee["salary"])
        department = employee["department"]

        department_salaries[department].append(salary)

        if employee["is_active"] == "True":
            active_count += 1
            active_employees.append(employee)
        else:
            inactive_count += 1

    # დეპარტამენტების სტატისტიკა

    department_stats = []

    print("\nდეპარტამენტების სტატისტიკა:")
    for department, salaries in department_salaries.items():
        count = len(salaries)
        average = round(sum(salaries) / count, 2)

        print(f"{department}: {count} თანამშრომელი, საშუალო ხელფასი: {average}")

        department_stats.append({
            "department": department,
            "employee_count": count,
            "avg_salary": average
        })

    # 3 ყველაზე მაღალანაზღაურებადი აქტიური თანამშრომელი

    top_3 = sorted(
        active_employees,
        key=lambda employee: int(employee["salary"]),
        reverse=True
    )[:3]

    print("\nTOP 3 აქტიური თანამშრომელი:")
    for employee in top_3:
        print(
            employee["first_name"],
            employee["last_name"],
            int(employee["salary"])
        )

    print("\nაქტიური თანამშრომლები:", active_count)
    print("არააქტიური თანამშრომლები:", inactive_count)

    # department_stats.csv

    sorted_stats = sorted(
        department_stats,
        key=lambda item: item["avg_salary"],
        reverse=True
    )

    stats_path = output_dir / "department_stats.csv"
    with stats_path.open("w", encoding="utf-8", newline="") as f:
        fieldnames = ["department", "employee_count", "avg_salary"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sorted_stats)

    # high_earners.csv

    high_earners = []

    for employee in active_employees:
        salary = int(employee["salary"])

        if salary >= 5000:
            full_name = f'{employee["first_name"]} {employee["last_name"]}'
            high_earners.append([
                employee["id"],
                full_name,
                employee["department"],
                salary
            ])

    high_path = output_dir / "high_earners.csv"
    with high_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "full_name", "department", "salary"])
        writer.writerows(high_earners)

    print("\nhigh_earners.csv ჩანაწერები:", len(high_earners))

    return sorted_stats


# უსაფრთხო ფაილის წაკითხვა
def safe_read(path):
    try:
        with path.open("r", encoding="utf-8") as f:
            return f.read()

    except FileNotFoundError:
        log(f"ფაილი ვერ მოიძებნა: {path.name}")
        return ""

    except UnicodeDecodeError:
        log(f"UnicodeDecodeError ფაილში: {path.name}")
        with path.open("r", encoding="utf-8", errors="replace") as f:
            return f.read()


def test_safe_read():
    missing_path = OUTPUT_DIR / "missing.txt"
    missing_text = safe_read(missing_path)
    print("\nmissing.txt შედეგი:", repr(missing_text))

    broken_path = OUTPUT_DIR / "broken.txt"

    # ბინარული რეჟიმით ვქმნით განზრახ დაზიანებულ UTF-8 ფაილს
    with broken_path.open("wb") as f:
        f.write(bytes([99, 97, 102, 233, 32, 255]))

    broken_text = safe_read(broken_path)
    print("broken.txt შედეგი:", repr(broken_text))


# ქალაქების TOP 3 Counter-ით
def city_report(csv_path, output_dir):
    with csv_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        cities = Counter(employee["city"] for employee in reader)

    top_cities = cities.most_common(3)

    print("\nქალაქების TOP 3:")
    for city, count in top_cities:
        print(city, count)

    cities_path = output_dir / "cities.txt"
    with cities_path.open("w", encoding="utf-8") as f:
        print("ქალაქების TOP 3:", file=f)
        for item in top_cities:
            print(item, file=f)


# JSON-ის უსაფრთხო შენახვა
def save_json_safe(data, path):
    temp_path = Path(str(path) + ".tmp")

    with temp_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    os.replace(temp_path, path)


def save_department_json(department_stats):
    json_path = OUTPUT_DIR / "summary.json"
    save_json_safe(department_stats, json_path)
    print("\nJSON ანგარიში შეინახა:", json_path.name)


# საკუთარი context manager
class Timer:
    def __init__(self, name):
        self.name = name
        self.start_time = None

    def __enter__(self):
        print(f"START {self.name}")
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        elapsed = time.perf_counter() - self.start_time
        print(f"FINISH {self.name}: {elapsed:.4f} წამი")

        if exc_type is not None:
            print(f"FAILED {self.name}: {exc_type.__name__}")

        return False


#  Timer-ის შეცდომის დემონსტრაცია
def timer_test():
    try:
        with Timer("test"):
            1 / 0
    except ZeroDivisionError:
        print("ZeroDivisionError დაჭერილია with-ის გარეთ.")


# მთავარი ფუნქცია
def main():
    # 1.1 — გარემოს მომზადება
    if not prepare_environment():
        return

    # 1.2 — backup
    backup_path = OUTPUT_DIR / "employees_backup.csv"
    line_count = backup_file(DATA_FILE, backup_path)
    print("Backup-ში გადაკოპირებული ხაზები:", line_count)

    # 1.4 — lock
    create_lock()

    log("ნაწილი 1 დასრულდა")

    # ნაწილი 2 — CSV ანალიზი
    with Timer("CSV ანალიზი"):
        show_reader_report(DATA_FILE)
        department_stats = analyze_employees(DATA_FILE, OUTPUT_DIR)

    log("ნაწილი 2 დასრულდა")

    # ნაწილი 3 — შეცდომები, ქალაქები და JSON
    test_safe_read()
    city_report(DATA_FILE, OUTPUT_DIR)
    save_department_json(department_stats)

    log("ნაწილი 3 დასრულდა")

    # ნაწილი 4 — Timer-ის ტესტი
    timer_test()

    log("ნაწილი 4 დასრულდა")
    log("პროგრამა დასრულდა")

    print("\nპროგრამა დასრულდა.")


if __name__ == "__main__":
    main()


# ნაწილი 5 — თეორიული კითხვები

# 1. რეჟიმი w სახიფათოა, რადგან ფაილის გახსნისას ძველ შიგთავსს შლის.
# არსებული ფაილის ბოლოში დასამატებლად გამოვიყენებდი a რეჟიმს.

# 2. __exit__() სრულდება with ბლოკის დასრულებისას და ამუშავებს რესურსის
# დახურვის პროცესს. with ავტომატურად ზრუნავს ფაილის დახურვაზე მაშინაც,
# როცა შეცდომა ხდება, ამიტომ ხელით close() აღარ გვჭირდება.

# 3. split(',') არასწორია, რადგან CSV ველში შეიძლება მძიმეც იყოს.
# მაგალითად: 1,"თბილისი, საქართველო",5000 — split(',') სვეტებს არასწორად გაყოფს.
# csv მოდული ასეთ შემთხვევებს სწორად ამუშავებს.

