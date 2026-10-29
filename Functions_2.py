#nawili1:
#აქ შევქმენით რეკურსული ფაქტორიალის ფუნქცია 
# სადაც ფრჩხილებში მივანიჭეთ პარამეტრი n,
# რომელიც მიიღებს ნებისმიერ დადებით ინტეჯერს.
def factorial_recursive(n):

#აქ ვწერთ ლოგიკურ 
# პირობას რომლის საფუძველზე უნდა 
# შესრულდეს ჩვენი დაწერილი კოდი(პირველი if აკეთებს 
# იმას რომ თუ შიყვანს მომხმარებელი უარყოფით რიცხვს
# returnის საშუალებით დაგვიბრუნებს Factorial is not 
# defined for negative numbers.და დამთავრდა.
# თუ პირველი if არ შესრულდა 
# გაგრძელდება და წამოვა მეორე if ში,
# თუ რიცხვი(n) უდრის ნულს ან 1 ს 
# დაგვიბრუნებს True ს
# ანუ 1 ს...გაგრძელდება კოდი და წამოვა 
# ჩვენს შეყვანილ ფორმულაში,სადაც 
# სწორი მონაცემის შეყვანის შემთხვევაში 
# return დაგვიბრუნებს 
# შესაბამის პასუხს მაგალითად თუ 3 ს 
# შევიყვათ კომპილერში 6 გამოვა,
# მაგრამ კომპილერში გამოსატანად და 
# დასატესტად პრინტს ვიყენებთ და არა
# returns.   )
    if n < 0:
        return "Factorial is not defined for negative numbers."
    if n == 0 or n == 1:
        return 1
    
    return n * factorial_recursive(n - 1)

# Test the function
print(factorial_recursive(10)) 

#nawili2:
def calculate_cart_total(discount_rate, *prices):

    total = sum(prices)
    discount_amount = total * discount_rate / 100
    discounted_total = total - discount_amount
    return float(discounted_total)

print(calculate_cart_total(20, 5, 15, 30))

#nawili3:
from functools import reduce

names = ["Ana", "Nino", "Luka", "Giorgi", "Mariam"]
scores = [45, 82, 91, 38, 74]

def pair_students(names_list, scores_list):
    students = list(zip(names_list, scores_list))
    return students

result = pair_students(names, scores)
print(result)

def get_passed_students(paired_data, passing_score=60):
    return list(filter(lambda student: student[1] >= passing_score, paired_data))

def calculate_average_of_passed(passed_students):
    scores = list(map(lambda student: student[1], passed_students))

    if not scores:
        return 0.0

    total = reduce(lambda a, b: a + b, scores)
    average = total / len(scores)

    return average

paired_data = pair_students(names, scores)
passed_students = get_passed_students(paired_data)

print("ყველა სტუდენტი:", paired_data)
print("ჩაბარებული სტუდენტები:", passed_students)

#sashualo chabarebuli studentebis:
average = calculate_average_of_passed(passed_students)

print("საშუალო ქულა:", round(average, 2))



