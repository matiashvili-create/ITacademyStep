print("Hello Guest")

Name = str(input("What is your name? ")) #მომხმარებლის სახელი
Lastname = str(input("What is your lastname? ")) #მომხმარებლის გვარი
Age = int(input("What is your Age? ")) #მომხმარებლის ასაკი
Language = str(input("What is your favourite programming language? ")) #მომხმარებლის საყვარელი პროგრამირების ენა

Current_year=2026
Yourbirthyear=Current_year-Age
is_adult= Current_year - Yourbirthyear >=18

print(Name.upper(), Lastname.upper(), Age, Language, is_adult, sep=" | ")

score = int(input("შეიყვანე მიღებული ქულა (მაქსიმუმ 20 ქულა): "))

grade = score // 2

print(grade)





