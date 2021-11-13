#import turtle
#from turtle import Turtle, Screen

#timmy = Turtle()
#print(timmy)

#my_screen = Screen()
#print(my_screen.canvheight)

from prettytable import PrettyTable
table = PrettyTable()  # table is the object, PrettyTable is class
table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align ="l"
print(table)