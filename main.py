"""
from turtle import Turtle,Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("green")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)

my_screen.exitonclick()
"""

from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ("Pokemon Name", "Type", "City")
table.add_row(["Pikachu", "Electric", "US"])
table.add_row(["Pikachu1", "Electric1", "EUROPE"])
table.add_row(["Pikachu2", "Electric2", "ASIA"])
table.align = "l"

print(table)
