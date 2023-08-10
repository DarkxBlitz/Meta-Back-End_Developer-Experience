class MyClass:
    a = 5
    print("hello friends")
    def greeting(self):
        print("Welcome everybody to the world of coding!")
#    pass    #pass is a placeholder telling python we wont do anything with it yet and use it when you have an empty class with no attributes


anyvar_name_iwant = MyClass()     #this will print hello friends

print(MyClass.a)    #here we are getting the attribute from the class and printing it which will be 5 in the terminal, you can also perform math in the paranthesis itself and many other things

print(anyvar_name_iwant.a + 3)  #here we are getting he attribute from the class but through the object we created "anyvar_name_iwant" and performs the same action

print(anyvar_name_iwant.greeting()) #here we call the function inside the class and use "self" in the class so we get get an argument error


#Instantiate a custom Object
class Recipe:
    def __init__(self,dish,items,time) -> None:
        self.dish = dish
        self.items = items
        self.time = time

    def contents(self):
        print("The " + self.dish + " has " + str(self.items) + \
              " and takes " + str(self.time) + " min to prepare.")
        
pizza = Recipe("Pizza", ["cheese", "bread", "tomato", "sausage"], 45)
pasta = Recipe("pasta", ["cheese", "spaghetti", "tomato", "ground beef"], 45)

print(pizza.items)
print(pasta.items)

print(pizza.contents())
print("\nNow lets do pasta")
print(pasta.contents())