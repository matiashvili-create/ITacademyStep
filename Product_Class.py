class Product:
    store_name = "TechShop Georgia" 
    currency = "GEL"            
    total_products = 0 

    def __init__(self,name=str,price=float,stock=int,category=str,discount=0):
        self.name=name
        self.price=price
        self.stock=stock
        self.category=category
        self.discount=discount

        Product.total_products +=1

    def get_info(self):
        return f"პროდუქტი: {self.name}, ფასი: {self.price} {Product.currency}, მარაგი: {self.stock}, კატეგორია: {self.category}, დაკლებული: {self.discount*100}%"


    def apply_discount(self, percent):
        if percent < 0 or percent > 100:
            raise ValueError("ფასდაკლება უნდა იყოს 0-დან 100-მდე.")

        self.discount = percent
        print(f"ფასდაკლება განახლდა: {percent}%")

    def update_stock(self, amount):
        if self.stock + amount < 0:
            print("გაფრთხილება: მარაგი არ არის საკმარისი!")
        else:
            self.stock += amount

    def calculate_final_price(self):
        return self.price - (self.price * self.discount / 100)
        
    @classmethod
    def get_total_products_count(cls):
        return cls.total_products

p1 = Product("Smartphone X", 1200, 15, "Electronics")
p2 = Product("Wireless Headphones", 250, 30, "Electronics", discount=10)
p3 = Product("Running Shoes", 180, 8, "Sportswear")


print(p1.get_info())
p1.apply_discount(15)
print(f"ფასდაკლებული ფასი: {p1.calculate_final_price()} {Product.currency}")

p3.update_stock(9)  # მარაგის გაზრდა
p3.update_stock(-2) # მარაგის შემცირება (გაყიდვა)

print(f"სულ შექმნილი პროდუქტები: {Product.get_total_products_count()}")
