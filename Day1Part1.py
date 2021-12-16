file = open('Day1Part1.txt','r')
depths = file.readlines()

total_increasing = 0

for i in range(len(depths)):
    if i == 0:
        continue 
    
    if depths[i] > depths[i - 1]:
      total_increasing += 1
      
print (total_increasing)
      
      

