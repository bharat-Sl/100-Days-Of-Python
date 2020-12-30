#challenge 3
row1=["⬜️","⬜️","⬜️"]
row2=["⬜️","⬜️","⬜️"]
row3=["⬜️","⬜️","⬜️"]
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position=input("Where do you want to put the treasure? ")

if(int(position[0])<4 and int(position[1])<4):
    map[int(position[1])-1][int(position[0])-1]='X'
    print(f"{row1}\n{row2}\n{row3}")
else:
    print('Some Error Occured.')