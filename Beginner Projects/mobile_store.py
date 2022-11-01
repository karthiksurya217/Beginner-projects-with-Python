#Mobile_Store
class Samsung(): 
    all = []
    def __init__(self, model: str, price: float,ram: int, camera: int, battery: int, quantity: float = 0):
        #assert
        assert price >= 0
        assert quantity > 0
        
        #Assignment
        self.model = model
        self.price = price
        self.ram = ram
        self.camera = camera
        self.battery = battery
        self.quantity = quantity
        
        
        #Actions
        Samsung.all.append(self)
        
    #discount
    def discount(self):
        valid_codes = ['XMAS 10', 'NEWCUST 30', 'LUCK 40']
        code = str(input("Enter the coupon code"))
        for i in range(0, len(valid_codes)):
            if code in valid_codes[i]:
                print("you have entered a valid code")
                decode = code.split()
                disc_value = int(decode[1])
                self.price  = self.price - (self.price * disc_value//100)
        print(self.price)
        if code not in valid_codes:
            print("you have entered an invalid code")

    

product1 = Samsung("Galaxy Z Flip 4", 150000, 16, 50 , 1800, 5)
product2 = Samsung("Galaxy S22 Ultra", 100000, 16, 35, 1400, 5)
product3 = Samsung("Galaxy A23", 30000, 8, 15, 1000, 15)
product4 = Samsung("Galaxy M200", 15000, 8, 12, 800, 20)

#INITIALIZATIONS
model_list = list()
price_list  = list()


customer_choice = str(input(("Good day, are you looking for someting particular? ")))
if customer_choice == "YES":
    for instance in Samsung.all:
        model_list.append(instance.model)
    print("These are our available models: ", model_list)
    cust_choice_2 = str(input("what model would you like? "))
    for i in range(0,len(model_list)):
        if cust_choice_2 == model_list[i]:
            cust_choice_3 = str(input(("That model is available with us, do you have a discount coupon? ")))
        if cust_choice_2 == product1.model:
                    product1.discount()
        elif cust_choice_2 == product2.model:
                    product2.discount()
        elif cust_choice_2 == product3.model:
                    product3.discount()
        elif cust_choice_2 == product4.model:
                    product4.discount()
        
            
        
        
        
        
        
        
        
        