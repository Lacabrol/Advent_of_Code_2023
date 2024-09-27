def find_adjacent_symbol(ascii_value):
    return(not(48<=ascii_value<=57) and not(ascii_value==46) and ascii_value!=ord('\n'))


if (__name__ == '__main__'):
    with open("input3.txt", "r") as f:
        lines = f.readlines()
    number=final_sum=0
    adjacent=False
    for i in range(len(lines)):
        adjacent=False
        number=0
        for j in range(len(lines[i])):
            if(48<=ord(lines[i][j])<=57):
                number=number*10+int(lines[i][j])
                if(not(adjacent)):
                    if(i!=0):
                        adjacent=find_adjacent_symbol(ord(lines[i-1][j]))
                        if(not(adjacent) and j!=0):
                            adjacent=find_adjacent_symbol(ord(lines[i-1][j-1]))
                        if(not(adjacent) and j!=len(lines[i])-1):
                            adjacent=find_adjacent_symbol(ord(lines[i-1][j+1]))
                    if(not(adjacent) and i!=len(lines)-1):
                        adjacent=find_adjacent_symbol(ord(lines[i+1][j]))
                        if(not(adjacent) and j!=0):
                            adjacent=find_adjacent_symbol(ord(lines[i+1][j-1]))
                        if(not(adjacent) and j!=len(lines[i])-1):
                            adjacent=find_adjacent_symbol(ord(lines[i+1][j+1]))
                    if(not(adjacent) and j!=len(lines[i])-1):
                        adjacent=find_adjacent_symbol(ord(lines[i][j+1]))
                    if(not(adjacent) and j!=0):
                        adjacent=find_adjacent_symbol(ord(lines[i][j-1]))

            else:
                if(adjacent):
                    final_sum+=+number
                    print(number)
                    
                adjacent=False
                number=0
    print(final_sum)
                    
