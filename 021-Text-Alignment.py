#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i)(thickness-1)+c+(c*i)(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness)(thickness*2)+(c*thickness)(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5)(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness)(thickness*2)+(c*thickness)(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1))(thickness)+c+(c*(thickness-i-1))(thickness))(thickness*6))