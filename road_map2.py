 #  Don't change the code below 
row1 = ["⬜️","⬜","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# Don't change the code above 

#Write your code below this row

vertical = int(position[0])
column = int(position[1])

map[vertical - 1][column-1] = "X"
print(f"{row1}\n{row2}\n{row3}")


