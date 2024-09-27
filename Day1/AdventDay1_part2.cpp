#include <fstream> 
#include <iostream> 
#include <string> 
using namespace std; 
  
int main() 
{ 
    int first, last,tmp;
    int sum=0;
    ifstream inputFile("input.txt"); 
    if (!inputFile.is_open()) { 
        cerr << "Error opening the file!" << endl; 
        return 1; 
    } 
    
    string line;
    while (std::getline(inputFile, line))
    {
        first =-1;
        last =-1;

        for(int i = 0;i<line.length();i++){
            if(line[i]>=48 && line[i]<=57){

                tmp=stoi(&line[i]);
                while(tmp>10){
                    tmp=tmp/10;
                }
            }
            else if (i + 3 < line.length() && line.substr(i, 4) == "zero") tmp = 0;

            else if (i + 2 < line.length() && line.substr(i, 3) == "one") tmp = 1;

            else if (i + 2 < line.length() && line.substr(i, 3) == "two") tmp = 2;

            else if (i + 4 < line.length() && line.substr(i, 5) == "three") tmp = 3;

            else if (i + 3 < line.length() && line.substr(i, 4) == "four") tmp = 4;

            else if (i + 3 < line.length() && line.substr(i, 4) == "five") tmp = 5;

            else if (i + 2 < line.length() && line.substr(i, 3) == "six") tmp = 6;

            else if (i + 4 < line.length() && line.substr(i, 5) == "seven") tmp = 7;

            else if (i + 4 < line.length() && line.substr(i, 5) == "eight") tmp = 8;

            else if (i + 3 < line.length() && line.substr(i, 4) == "nine") tmp = 9;

            else{tmp=-1;}  

            if(tmp!=-1){  

                last=tmp;     
                if(first==-1){
                        first=tmp*10;
                }
                
            }
        
        


        }
        cout << first+last;
        cout << '\n';
        sum=sum+first;
        sum=sum+last;
    }
    cout << sum;
    return 0;
}