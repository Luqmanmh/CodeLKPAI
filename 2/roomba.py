class Roomba:
    def __init__(self, x, y):
        self.coorx = x
        self.coory = y
    
    def movR(self, floor):
        if floor[self.coory][self.coorx] == 1:
            floor[self.coory][self.coorx] = 0
        self.coorx += 1
            
    def movL(self, floor):
        if floor[self.coory][self.coorx] == 1:
            floor[self.coory][self.coorx] = 0
        self.coorx -= 1
            
    def dropDown(self, floor):
        if floor[self.coory][self.coorx] == 1:
            floor[self.coory][self.coorx] = 0
        self.coory += 1

    def printroom(self, floor, room):
        width, height = room
        
        for i in range(height):
            for j in range(width):
                if i == self.coory and j == self.coorx:
                    print("x ", end="")
                else:
                    print(f"{floor[i][j]} ", end="")
            print() 
        
print("Room size (width, height):")
roomS = input().split(", ")
roomS = [int(i) for i in roomS]

print("Input room content:")
floor_inp = input()

floor = []
for i in range(roomS[1]):
    row = list(map(int, floor_inp[i * roomS[0]:(i + 1) * roomS[0]]))
    floor.append(row)

Roomb4 = Roomba(0, 0)

time = 1
cond = 0
flip = 0

for i in range(roomS[0] * roomS[1]):
    
    
    if Roomb4.coorx == roomS[0] - 1 and flip == 0:
        cond = 1
        Roomb4.dropDown(floor)
        i -= 1
        flip = 1
        continue
    
    if Roomb4.coorx == 0 and Roomb4.coory != 0 and flip == 0:
        cond = 0
        Roomb4.dropDown(floor)
        i -= 1
        flip = 1
        continue
    
    print(f"time: {time}")
    Roomb4.printroom(floor, roomS)
        
    if cond == 0:
        Roomb4.movR(floor)
    else:
        Roomb4.movL(floor)
        
    time += 1
    flip = 0
    print(Roomb4.coorx, Roomb4.coory)
    


print(f"time: {time}")
Roomb4.printroom(floor, roomS)
print(Roomb4.coorx, Roomb4.coory)