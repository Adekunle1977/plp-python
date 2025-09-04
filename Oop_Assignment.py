# Defining a class
class Smartphone:
    color = "red"  # Attribute

    # Method
    def Call(self):
        print("The Smartphone is making Call ")

# Creating an object
my_Smartphone = Smartphone()
print(my_Smartphone.color)
my_Smartphone.Call()
class Smartphone:
    def __init__(self, color, model):
        self.color = color    # Instance variable
        self.model = model    # Instance variable

# Creating objects with unique attributes

Smartphone1= Smartphone("blue", "Iphone 15")
Smartphone2= Smartphone("Red", "Samsung A05")

print(Smartphone1.color)  # Output: Red
print(Smartphone2.model)  # Output: Iphone 15

class MobilePhone:
    def __init__(self, camera):
        self.camera = camera

class Smartphone(MobilePhone):
    pass

Smartphone = Smartphone(2)
print(Smartphone.camera)  # Output: 2

class SecretBash:
    def __init__(self):
        self.__Book = 10  # Private attribute

    def take_Book(self):
        if self.__Book > 0:
            self.__Book -= 1
            print("One Book taken!")
        else:
            print("No Book left 😢")

stash = SecretBash()
stash.take_Book()