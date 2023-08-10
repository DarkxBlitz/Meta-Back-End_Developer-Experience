class House:
    '''
    This is a stub for a class representing a house that can be used to create objects and evaluate different metrics that we may require in constructing it.
    '''
    num_rooms = 5
    bathrooms = 2
    def cost_evaluation(self):
        print(self.num_rooms)
        pass
        # Functionality to calculate the costs from the area of the house

house = House()
print(house.num_rooms)
print(House.num_rooms)
house.num_rooms = 7
print(house.num_rooms)
print(House.num_rooms)
House.num_rooms = 7
print(house.num_rooms)
print(House.num_rooms)
House.num_rooms -= 4
print(house.num_rooms)
print(House.num_rooms)

'''
# Define class MyFirstClass
class MyFirstClass:
    print("Who wrote this")
    index = "Author-Book"
    def hand_list(self, philosopher, book):
        print(philosopher + " wrote the book: " + book)

whodunnit = MyFirstClass()
print(whodunnit.hand_list("Sun Tzu","The Art of War"))
    # Define string variable called index
    
    # Define function hand_list()
    
        # variable + “ wrote the book: ” + variable
        

# Call function handlist()
'''
'''
# Sample Solution code
class MyFirstClass():
    print("Who wrote this?")
    index = "Author-Book"

    def hand_list(self, philosopher, book):
        print(MyFirstClass.index)
        print(philosopher + " wrote the book: " + book)

whodunnit = MyFirstClass()
whodunnit.hand_list("Sun Tzu", "The Art of War")
'''
