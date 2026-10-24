# ინვენტარი - Dictionary
inventory = {
    "laptop": {"price": 2500, "stock": 5},
    "phone": {"price": 1200, "stock": 10},
    "headphones": {"price": 150, "stock": 8},
    "keyboard": {"price": 100, "stock": 0}
}

# მომხმარებლები - Sets
active_users = {"nika@gmail.com", "ana@gmail.com", "gio@gmail.com"}
vip_users = {"ana@gmail.com", "gio@gmail.com", "mari@gmail.com"}


# ახალი პროდუქტის დამატება ან რაოდენობის განახლება
while True:
    print("\nპროდუქტის მართვა: ")
    print("1. ახალი პროდუქტის დამატება ან რაოდენობის განახლება")
    print("2. გაგრძელება ანალიტიკაზე")

    choice = input("აირჩიეთ მოქმედება (1 ან 2): ")

    if choice == "1":
        name = input("შეიყვანეთ პროდუქტის სახელი: ").lower()

        if name in inventory:
            try:
                amount = int(input("რამდენით შევცვალოთ რაოდენობა? "))
                if inventory[name]["stock"] + amount >= 0:
                    inventory[name]["stock"] += amount
                    print("პროდუქტის რაოდენობა განახლდა.")
                else:
                    print("შეცდომა: რაოდენობა 0-ზე ნაკლები ვერ იქნება.")
            except ValueError:
                print("გთხოვთ შეიყვანოთ მთელი რიცხვი.")

        else:
            try:
                price = float(input("შეიყვანეთ პროდუქტის ფასი: "))
                stock = int(input("შეიყვანეთ პროდუქტის რაოდენობა: "))

                if price > 0 and stock >= 0:
                    inventory[name] = {
                        "price": price,
                        "stock": stock
                    }
                    print("ახალი პროდუქტი დაემატა.")
                else:
                    print("ფასი უნდა იყოს 0-ზე მეტი, რაოდენობა კი 0 ან მეტი.")
            except ValueError:
                print("გთხოვთ, სწორად შეიყვანოთ ფასი და რაოდენობა.")

    elif choice == "2":
        break

    else:
        print("არასწორი არჩევანი. აირჩიეთ 1 ან 2.")


# ინვენტარის სრული სია და ჯამური ღირებულება
print("\nინვენტარი: ")

total_value = 0

for name, details in inventory.items():
    price = details["price"]
    stock = details["stock"]
    value = price * stock
    total_value += value

    print(
        f"პროდუქტი: {name} | "
        f"ფასი: {price:.2f} ლარი | "
        f"რაოდენობა: {stock} | "
        f"ღირებულება: {value:.2f} ლარი"
    )

print("--------------------------------")
print(f"ინვენტარის ჯამური ღირებულება: {total_value:.2f} ლარი")


# 5. მარაგში არსებული პროდუქტები
print("\nხელმისაწვდომი პროდუქტები: ")

for name, details in inventory.items():
    if details["stock"] > 0:
        print(name, "- რაოდენობა:", details["stock"])


# 6. ყველაზე ძვირადღირებული პროდუქტი
print("\nყველაზე ძვირადღირებული პროდუქტი: ")

most_expensive = max(
    inventory,
    key=lambda name: inventory[name]["price"]
)

print("პროდუქტი:", most_expensive)
print("ფასი:", inventory[most_expensive]["price"], "ლარი")


# 7. Set-ების ოპერაციები
print("\nმომხმარებელთა ანალიტიკა: ")

# ყველა უნიკალური მომხმარებელი
all_users = active_users | vip_users
print("ყველა უნიკალური მომხმარებელი:", all_users)

# აქტიური მომხმარებლები, რომლებიც VIP-ებიც არიან
active_vip = active_users & vip_users
print("აქტიური VIP მომხმარებლები:", active_vip)

# აქტიური მომხმარებლები, რომლებიც VIP-ები არ არიან
active_non_vip = active_users - vip_users
print("აქტიური მომხმარებლები, რომლებიც VIP-ები არ არიან:", active_non_vip)
