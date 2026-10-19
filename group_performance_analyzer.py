scores = []

while True:
    user_input = input("შეიყვანეთ სტუდენტის ქულა (ან 'stop' დასასრულებლად): ")

    if user_input.lower() == "stop":
        break

    try:
        score = float(user_input)

        if 0 <= score <= 10:
            scores.append(score)
        else:
            print("გთხოვთ შეიყვანოთ ქულა 0-დან 10-ის ჩათვლით.")

    except ValueError:
        print("გთხოვთ შეიყვანოთ სწორი რიცხვი ან 'stop'")

if len(scores) > 0:

    minimum = min(scores)
    maximum = max(scores)
    average = sum(scores) / len(scores)

    print("კლასის შედეგები: \n")
    print(f"მინიმალური ქულა: {minimum:g}")
    print(f"მაქსიმალური ქულა: {maximum:g}")
    print(f"საშუალო ქულა: {average:.2f}")

    scores.sort()   #სორტირება,ქულები ზრდადობით დალაგდება

    print("\nქულები ზრდადობით: ")
    print(scores)
    print("\nთითოეული ქულის გამეორების რაოდენობა:")

    for score in sorted(set(scores)):
        print(f"ქულა {score:g} — {scores.count(score)}-ჯერ")

else:
    print("\nქულები არ არის შეყვანილი.")
        
    
                
                
        
            
                
            
