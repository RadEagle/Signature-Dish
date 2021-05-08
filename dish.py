class Menu:
    # initializes the Menu and its data members
    def __init__(self):
        self._hot_dishes = ["mushroom spaghetti", "roasted duck", "roasted potatoes", "spinach salad", "pork soup"]
        self._hot_dishes_timers = {"mushroom spaghetti": 25, "roasted duck": 45, "roasted potatoes": 30,
                                   "spinach salad": 20, "pork soup": 15}

    # asks the user what they would like to order
    def Cremini(self):
        dish = input("What would you like to order? ")
        while dish not in self._hot_dishes:
            dish = input("What would you like to order? ")
        return dish

    # asks the user how much time they have
    def Portobello(self):
        time = input("How many minutes do you have? ")
        return int(time)

    # prints out the menu
    def Chanterelle(self):
        for _hot_dish in self._hot_dishes:
            print(f"{_hot_dish}: {self._hot_dishes_timers[_hot_dish]} minutes")

    # checks if the dish can be made in time
    def Porcini(self, _hot_dish, _hot_time):
        if (_hot_time > self._hot_dishes_timers[_hot_dish]):
            self.Hedgehog(_hot_dish, _hot_time)
        else:
            self.Black_Trumpet()

    # lets the user know that the dish cannot be made in time
    def Hedgehog(self, _hot_dish, _hot_time):
        print(f"Sorry, we don't have time to make {_hot_dish} in {_hot_time} minutes")

    # lets the user know that the dish can be made in time
    def Black_Trumpet(self):
        print("Your order has been placed!")


class RichMenu(Menu):
    def __init__(self):
        self._hot_dishes = ["beef wellington", "sheperds pie", "lobster", "mac and cheese"]
        self._hot_dishes_timers = {"beef wellington": 50, "sheperds pie": 30, "lobster": 20, "mac and cheese": 10}
        
# Main function
menu_string = input("Welcome! Would you like to see the regular menu or the rich menu? ")
while (menu_string != "regular" and menu_string != "rich"):
  menu_string = input("Would you like to see the regular menu or the rich menu? ")

if (menu_string == "regular"):
  menu = Menu()
else:
  menu = RichMenu()

menu.Chanterelle()

dish = menu.Cremini()
time = menu.Portobello()
menu.Porcini(dish, time)
