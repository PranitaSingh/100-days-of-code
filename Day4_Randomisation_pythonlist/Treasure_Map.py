row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']

print(f"{row1}\n{row2}\n{row3}") 
map = [row1, row2, row3]

value_of_treasure = input("where you want to put the treasure")

vertical = int(value_of_treasure[0])
horizontal = int(value_of_treasure[1])

map[vertical][horizontal] = "X"

print(f"{row1}\n{row2}\n{row3}")


