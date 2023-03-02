from BirdBrain import Finch

myFinch = Finch('A')
print("hello")

# for i in range(0,4):
#     myFinch.setBeak(100, 100, 100)
#myFinch.setMove('F', 30, 100)
    # time.sleep(1)
#myFinch.setTurn('R', 180, 100 )
    # time.sleep(1)
##myFinch.setMove ('F', 20, 100)
#myFinch.setTurn('L', 180, 1E00)
myFinch.setMove('F',100,30)
while True:
    print("how far away?: ", myFinch.getDistance())
    time.sleep(1)
    if myFinch.getDistance() < 10:
        myFinch.setTurn('R',180,100)
        myFinch.setMove('F', 100,100)
