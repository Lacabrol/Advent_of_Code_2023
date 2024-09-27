if (__name__ == '__main__'):
    with open("input4.txt", "r") as f:
        lines = f.readlines()

    final_sum=0
    winning_numbers=[]
    nb_winning_numbers=0
    numbers=False
    numbers_of_cards=[1]
    indice = 1

    for line in lines[:5]:

        winning_numbers=[]
        nb_winning_numbers=0
        words=line.split()
        numbers=False


        for word in words:
            if (word[:1]!=':' and word.isnumeric()):
                if (not (numbers)):
                    winning_numbers.append(int(word))
                else:
                    if(int(word) in winning_numbers):
                        nb_winning_numbers+=1
                        if(nb_winning_numbers<len(numbers_of_cards)):
                            numbers_of_cards[nb_winning_numbers]+=numbers_of_cards[0]
                        else:
                            numbers_of_cards.append(numbers_of_cards[0]+1)

            elif(word=="|"):
                numbers=True
                

            
        final_sum+=numbers_of_cards[0]
        numbers_of_cards.pop(0)
        print(numbers_of_cards)
        if(len(numbers_of_cards)==0):
            numbers_of_cards.append(1)

    print(final_sum)
            

                

