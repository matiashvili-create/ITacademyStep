total = 0
count = 0
min_num = None
max_num = None

while True:
    text = input("შეიყვანეთ რიცხვი (ან 'stop' დასასრულებლად): ")

    if text.lower() == "stop":
        break

    try:
        number = float(text)

        total += number
        count += 1

        if min_num is None or number < min_num:
            min_num = number

        if max_num is None or number > max_num:
            max_num = number

    except ValueError:
        print("გთხოვთ შეიყვანოთ მხოლოდ რიცხვი ან 'stop'")

print("რიცხვების ჯამი:", total)
print("რიცხვების რაოდენობა:", count)

if count > 0:
    print("მინიმალური რიცხვი:", min_num)
    print("მაქსიმალური რიცხვი:", max_num)
else:
    print("რიცხვები არ შეგიყვანიათ.")
