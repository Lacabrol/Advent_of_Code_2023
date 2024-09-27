import math
import re

def find_number(line,pos):
    if(not(48<=ord(line[pos])<=57)):
        return(-1)
    else: 
        if (pos!=0 and pos!=len(line)-1 and 48<=ord(line[pos-1])<=57 and 48<=ord(line[pos+1])<=57):
            number=re.findall('\d+', line[pos-1:pos+2])[0]
        elif (pos!=0 and 48<=ord(line[pos-1])<=57):
            if (pos>1):
                number=re.findall('\d+', line[pos-2:pos+1])[0]
            else:
                number=re.findall('\d+', line[pos-1:pos+2])[0]
        elif (pos!=len(line)-1 and 48<=ord(line[pos+1])<=57):
            if (pos<len(line)-2):
                number=re.findall('\d+', line[pos:pos+3])[0]
            else:
                number=re.findall('\d+', line[pos:pos+2])[0]
        else:
            number=re.findall('\d+', line[pos])[0]
            
        return int(number)
        
def remove_values_from_list(list, val):
   return [value for value in list if value != val]


if (__name__ == '__main__'):
    with open("input3.txt", "r") as f:
        lines = f.readlines()
    numbers=[]
    sum=0
    for i in range(len(lines)):
        numbers=[]
        for j in range(len(lines[i])):
            if(lines[i][j]=='*'):
    
                    if(i!=0):
                        numbers.append(find_number(lines[i-1],j))
                        if(numbers[len(numbers)-1]==-1):
                            if(j!=0):
                                numbers.append(find_number(lines[i-1],j-1))
                            if(j!=len(lines[i])-1):
                                numbers.append(find_number(lines[i-1],j+1))
                            else:
                                numbers.append(find_number(lines[i-1],j))

                    if(i!=len(lines)-1):
                        numbers.append(find_number(lines[i+1],j))
                        if(numbers[len(numbers)-1]==-1) :
                            if(j!=0):
                                numbers.append(find_number(lines[i+1],j-1))
                            if(j!=len(lines[i])-1):
                                numbers.append(find_number(lines[i+1],j+1))
                    if(j!=len(lines[i])-1):
                        numbers.append(find_number(lines[i][j:],1))
                    if(j!=0):
                        numbers.append(find_number(lines[i],j-1))

            else:
                numbers=remove_values_from_list(numbers,-1)
                
                if(len(numbers)>=2):
                    print(numbers)
                    sum=sum+math.prod(numbers)
                    

                numbers=[]
    print(sum)
                    
