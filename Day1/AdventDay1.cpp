#include <fstream> 
#include <iostream> 
#include <string> 
using namespace std; 
  
int main() 
{ 
    int first, last;
    int sum=0;
    ifstream inputFile("input.txt"); 
    if (!inputFile.is_open()) { 
        cerr << "Error opening the file!" << endl; 
        return 1; 
    } 
    
    string line;
    while (std::getline(inputFile, line))
    {
        first = last =-1;

        for(int i = 0;i<line.length();i++){
            if(line[i]>=48 && line[i]<=57){

                last=stoi(&line[i]);
                while(last>10){
                    last=last/10;
                }
                if(first==-1){
                    first=last*10;
                    
                }

            }  
        
        }
        sum=sum+first+last;
    }
    cout << sum;
    return 0;
}