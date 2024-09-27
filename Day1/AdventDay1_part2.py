if (__name__ == '__main__'):
    with open("input.txt", "r") as f:
        lines=f.readlines()
    first = last =-1
    final_sum=0
    literals = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
    }
    for line in lines :
        last=-1
        first=-1  
        for i in range(len(line)):
            litteral=-1
            if(48<=ord(line[i])<=57):
                last=int(line[i])
                if(first==-1):
                    first=last*10
            else:
                for word, num in literals.items():
                    if line[i:i+len(word)] == word:
                        last = num
                        if(first == -1):
                            first = last*10
                

        final_sum+=first+last
    print(final_sum)
