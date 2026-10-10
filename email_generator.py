print("HELLO!\n")

name=str(input("Please type your name: \n")) #saxeli
surname=str(input("please type your surname: \n")) #gvari
platform = input("Please choose platform:gmail.com, itstep.ge, yahoo.com \n") 

name= name.strip().lower()
surname=surname.strip().lower()
platform=platform.strip().lower()
first_two= name[0:2]     
email=f"{first_two}{surname}@{platform} " 

print(f"შენი ელფოსტაა:  {email}" )
print()     
print()
print("თქვენი ელ-ფოსტა წარმატებით შეიქმნა! ")
