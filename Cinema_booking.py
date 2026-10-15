import re

text = str(input("შეიყვანე ტექსტი: "))
numbers = re.findall(r"\d+",text) #parsing

print(numbers)

try :
    tickets=int(numbers[0]) 
    price=int(numbers[1])
    paid=int(numbers[2]) 

    price=15 # 1-ცალი ბილეთის ფასი.
    
    if tickets<=0:
        raise ValueError("ბილეთების რაოდენობა უნდა იყოს მინიმუმ 1!")
    
    total=tickets*price #ითვლის ბილეთების საერთო ღირებულებას.
    
    if paid<total :
        raise ValueError("თანხა არ არის საკმარისი!")

except IndexError:
    print("შეცდომა: ტექსტში სამი რიცხვი უნდა იყოს მითითებული!")

except ValueError as e:
    print(f"შეცდომა: {e}")


else:
    change =paid - total 

    print(f"ბილეთების რაოდენობა: {tickets}")
    print(f"ერთი ბილეთის ფასი: {price:.2f} ლარი")
    print(f"ჯამური ღირებულება: {total:.2f} ლარი")
    print(f"გადახდილი თანხა: {paid:.2f} ლარი")
    print(f"დასაბრუნებელი ხურდა: {change:.2f} ლარი")

finally:
    print("[სისტემა]: ტრანზაქციის მცდელობა დასრულდა.")








