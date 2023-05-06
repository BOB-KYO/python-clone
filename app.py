# from turtle import Turtle,Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")

# my_screen = Screen()
# print(my_screen.canvheight)# screen property (canvheight, canvwidth)
# my_screen.exitonclick()
# # This exitionclick will allow our program to continue running until 
# #we click on the screen and then it exits our code#

from prettytable import PrettyTable # 아스키 스타일
table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu","Squirtle","Charmander"])#column
table.add_column("Type",["Electric","Water","Fire"])#column

table.align = "l" # align
print(table)