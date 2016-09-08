#Author: Kishan Bhugul
#Version: 1.0

file = open('IP-Address.txt', 'r')
#print file.read()

for line in file:
        count=0
        for word in line.split():
            if(count==0):
               x = "ip nat inside source static "+word+" "
               count=count+1
            else:
                x=x+word

                print x
