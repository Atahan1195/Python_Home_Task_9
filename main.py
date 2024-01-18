# Task - 1 Создайте абстрактный базовый класс "Фигура" и от него наследуйте конкретные классы, такие как "Круг",
# "Прямоугольник", "Треугольник" и т.д. Каждый класс должен иметь методы для вычисления площади и периметра фигуры.
# Создайте несколько объектов разных фигур и выведите их площадь и периметр.
from abc import ABC, abstractmethod


class Figure:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def perimeter(self):
        pass

    def __str__(self):
        return f"{self.name} area is {self.area()} and perimeter is {self.perimeter():.2f}"


class Circle(Figure):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius


class Rectangle(Figure):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2


class Triangle(Figure):
    def __init__(self, name, side_a, side_b, side_c):
        super().__init__(name)
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self):
        p = (self.side_a + self.side_b + self.side_c) / 2
        return (p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)) ** 0.5

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c


class Square(Figure):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return self.side * 4


class Rhombus(Figure):
    def __init__(self, name, side, height):
        super().__init__(name)
        self.side = side
        self.height = height

    def area(self):
        return self.side * self.height

    def perimeter(self):
        return self.side * 4


circle = Circle("Circle", 5)
print(circle)
rectangle = Rectangle("Rectangle", 5, 10)
print(rectangle)
triangle = Triangle("Triangle", 3, 4, 5)
print(triangle)
square = Square("Square", 5)
print(square)
rhombus = Rhombus("Rhombus", 5, 10)
print(rhombus)


# Task - 2 Создайте абстрактный базовый класс "ПлатежноеСредство" с методом "осуществить_платеж()".
# Создайте подклассы "КредитнаяКарта", "БанковскийПеревод", "ЭлектронныйКошелек" и т.д.,
# которые наследуют этот метод и реализуют его в соответствии со спецификой каждого платежного средства.
# Создайте класс "ПлатежныйПроцессор", который содержит список доступных платежных средств и
# метод для выполнения платежа через выбранное средство. Можно создать объекты различных платежных средств,
# добавить их к платежному процессору и осуществить платежи через них


class PaymentMethod(ABC):

    def __init__(self, name, currency, balance):
        self.name = name
        self.currency = currency
        self.balance = balance

    @abstractmethod
    def make_payment(self, amount):
        pass

    def __str__(self):
        return f"{self.name} balance is {self.balance} {self.currency}"


class CreditCard(PaymentMethod):
    def __init__(self, name, currency, balance, credit_limit):
        super().__init__(name, currency, balance)
        self.credit_limit = credit_limit

    def make_payment(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Payment of {amount} {self.currency} is successful")
        elif self.balance + self.credit_limit >= amount:
            self.balance -= amount
            print(f"Payment of {amount} {self.currency} is successful")
        else:
            raise ValueError("Not enough money")


class BankTransfer(PaymentMethod):
    def __init__(self, name, currency, balance, bank_name, account_number):
        super().__init__(name, currency, balance)
        self.bank_name = bank_name
        self.account_number = account_number

    def make_payment(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Payment of {amount} {self.currency} is successful")
        else:
            raise ValueError("Not enough money")


class EWallet(PaymentMethod):
    def __init__(self, name, currency, balance, email):
        super().__init__(name, currency, balance)
        self.email = email

    def make_payment(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Payment of {amount} {self.currency} is successful")
        else:
            raise ValueError("Not enough money")


class PaymentProcessor:
    def __init__(self):
        self.payment_methods = []

    def add_payment_method(self, payment_method):
        self.payment_methods.append(payment_method)

    def make_payment(self, amount, payment_method):
        for method in self.payment_methods:
            if method.name == payment_method:
                method.make_payment(amount)
                break
        else:
            raise ValueError("Invalid payment method")


credit_card = CreditCard("Credit Card", "USD", 100, 100)
bank_transfer = BankTransfer("Bank Transfer", "USD", 100, "PrivatBank", "123456789")
e_wallet = EWallet("E-Wallet", "USD", 100, "atahan")
payment_processor = PaymentProcessor()
payment_processor.add_payment_method(credit_card)
payment_processor.add_payment_method(bank_transfer)
payment_processor.add_payment_method(e_wallet)
payment_processor.make_payment(200, "Credit Card")
payment_processor.make_payment(200, "Bank Transfer")
payment_processor.make_payment(200, "E-Wallet")
print(credit_card)
print(bank_transfer)
print(e_wallet)



