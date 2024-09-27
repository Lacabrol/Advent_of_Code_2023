#include <fstream> 
#include <iostream> 
#include <string> 
#include <math.h>

using namespace std; 

int main() 
{ 

    ifstream inputFile("input4.txt"); 
    if (!inputFile.is_open()) { 
        cerr << "Error opening the file!" << endl; 
        return 1; 
    } 

    unsigned int final_sum = 0, next_id;
    bool number;
    int nb_winning_numbers, i, j, temp; ;
    int winning_numbers[15]={0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
 

    
    string line;
    while (std::getline(inputFile, line))
    {
        nb_winning_numbers = -1;
        number = false;
        temp = 0;

        for(i=0;i<line.size();i++){
            if (line[i]>=48 && line[i]<=57){
                if (!number){
                    winning_numbers[next_id] = winning_numbers[next_id]*10 + (line[i]-48);
                }
                else{
                    temp = temp*10 + (line[i]-48);
                    
                            
                        }

            }
            else if (line[i]==':'){
                next_id = -1;
            }
            else if (line[i]=='|'){
                number = true;
            }
            else if (line[i]==' ' ){
                if(!number){
                    if(line[i-1]!=' ' ){
                
                        next_id++;
                    }
                    
                }
                else{
                    for(j=0;j<next_id;j++){
                        if (winning_numbers[j] == temp){
                            nb_winning_numbers++;
                    
                        }
                    }
                    temp = 0;
                }
            }
            
        }
        if(nb_winning_numbers != -1){
            final_sum = final_sum + pow(2,nb_winning_numbers);
        }
    }
    cout << final_sum;
    return 0;
}