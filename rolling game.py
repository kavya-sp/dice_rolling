from random import randint
import sys,os
x=[]
mi=1
ma=6
i=0
j=0
start=0
cur=0
def roll_back () :
    dice=randint(1,8)
    print "%d"
    cur=cur-dice
ch = int(raw_input("1.roll 2.quit\n"))
while cur <= 64 :
 for i in range(1,8) :
         for j in range (1,8) :
             if ch == 1 &  j< 8 :
               dice=randint(mi,ma)
               print "value of dice 1%d" %(dice)
               cur=cur+dice
               print "position is %d" %(cur)
             elif j >=8 :
                 dice=randint(mi,ma)
                 print "%d" %(dice)
                 cur=cur-dice
                 print "position is %d"  %(cur)
             elif i == 8 & j==3 :
                 dice=randint(1,2)
             elif ch == 2 :
               print "terminating..."
               sys.exit()


