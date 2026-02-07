# Parent Class
class Payment:
    def pay(self):
        print("Processing payment...")


# Child Class 1
class GooglePay(Payment):
    def pay(self):
        print("Payment made using Google Pay")


# Child Class 2
class PhonePe(Payment):
    def pay(self):
        print("Payment made using PhonePe")


# Child Class 3
class CreditCard(Payment):
    def pay(self):
        print("Payment made using Credit Card")

payment1 = GooglePay()
payment2 = PhonePe()
payment3 = CreditCard()

payment1.pay()
payment2.pay()
payment3.pay()
