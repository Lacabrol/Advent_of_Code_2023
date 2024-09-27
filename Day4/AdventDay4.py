if (__name__ == '__main__'):
    with open("input4.txt", "r") as f:
        lines = f.readlines()

    final_sum=0
    winning_numbers=[]
    nb_winning_numbers=-1
    numbers=False

    for line in lines:

        winning_numbers=[]
        nb_winning_numbers=-1
        words=line.split()
        numbers=False

        for word in words:
            if (word[:1]!=':' and word.isnumeric()):
                if (not (numbers)):
                    winning_numbers.append(int(word))
                else:
                    if(int(word) in winning_numbers):
                        nb_winning_numbers+=1

            elif(word=="|"):
                numbers=True
        if(nb_winning_numbers!=-1):
            final_sum+=2**nb_winning_numbers
    print(final_sum)
            

                

