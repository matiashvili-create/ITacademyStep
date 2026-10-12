
cart_total = float(input("შეიყვანე კალათის ღირებულება ლარებში: "))
user_status = input("შეიყვანე სტატუსი (regular/vip/admin): ").lower()
has_promo_code = input("აქვს პრომოკოდი? (კი/არა): ").lower() == "კი"
loyalty_points = float(input("შეიყვანე დაგროვილი ქულები: "))
delivery_city = input("შეიყვანე ქალაქი: ").strip()
is_account_active = input("აქტიურია ანგარიში? (კი/არა): ").lower() == "კი"

# 1. ანგარიშისა და კალათის შემოწმება
if not is_account_active:
    print("ანგარიში დაბლოკილია. შეკვეთა ვერ დამუშავდება.")

elif cart_total <= 0:
    print("შეცდომა: კალათის ღირებულება უნდა იყოს 0-ზე მეტი.")

elif user_status not in ["regular", "vip", "admin"]:
    print("შეცდომა: მომხმარებლის სტატუსი არასწორია.")

else:
    # 2. ფასდაკლების გამოთვლა
    discount = 0

    if user_status == "vip":
        discount = 20

        if loyalty_points >= 500:
            discount = 25

    elif user_status == "regular":
        if has_promo_code or cart_total >= 150:
            discount = 10

    elif user_status == "admin":
        discount = 50

    # 3. ფასდაკლებული თანხა
    discounted_total = cart_total * (1 - discount / 100)

    # 4. მიტანის საფასური
    if delivery_city in ["თბილისი", "ქუთაისი", "ბათუმი"]:
        if discounted_total >= 100:
            delivery_fee = 0
        else:
            delivery_fee = 5
    else:
        delivery_fee = 15

    # 5. საბოლოო გადასახდელი თანხა
    final_price = discounted_total + delivery_fee

    # 6. ინვოისი
    print("\n--- ინვოისი ---")
    print(f"საწყისი ფასი: {cart_total:.2f} ლარი")
    print(f"ფასდაკლება: {discount}%")
    print(f"ფასდაკლებული თანხა: {discounted_total:.2f} ლარი")
    print(f"მიტანის საფასური: {delivery_fee:.2f} ლარი")
    print(f"საბოლოო გადასახდელი: {final_price:.2f} ლარი")








