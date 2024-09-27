if (__name__ == '__main__'):
    with open("input.txt", "r") as f:
        lines=f.readlines()
    first = last =-1
    final_sum=0
    for line in lines :

        last=-1
        first=-1

        for i in range(len(line)):

            if(48<=ord(line[i])<=57):

                last=int(line[i])

                if(first==-1):
                    first=last*10

        final_sum+=first+last
    print(final_sum)
