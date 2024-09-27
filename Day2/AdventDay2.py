if (__name__ == '__main__'):
    with open("input2.txt", "r") as f:
        lines = f.readlines()

    red = blue = green = 0  
    max_red = max_blue = max_green = 0  
    
    id=-1
    final_sum=0
    reset=False
    for line in lines :
        red = blue = green = 0  
        max_red = max_blue = max_green = 0  
        id=-1
        words=line.replace(',', '').replace(':', '').split()
        for i in range (len(words)):
            if (words[i] == "Game"):
                id=int(words[i+1])
            else:
                if(words[i][len(words[i])-1]==';'):
                    reset=True
                    words[i]=words[i].replace(';', '')

                if(words[i]=="red"):
                    red+=int(words[i-1])
                    max_red=max(red,max_red)

                elif(words[i]=="green"):
                    green=int(words[i-1])
                    max_green=max(green,max_green)

                elif(words[i]=="blue"):
                    blue+=int(words[i-1])
                    max_blue=max(blue,max_blue)

            if(reset):
                red = blue = green = 0
                reset=False

        if(max_red<=12 and max_green<=13 and max_blue<=14):
            final_sum+=id

    print(final_sum)