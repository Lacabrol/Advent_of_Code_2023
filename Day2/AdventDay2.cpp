#include <fstream> 
#include <iostream> 
#include <string> 

using namespace std; 

unsigned int find_number(int start,string line){
    unsigned int j=0;
    int number=0;

    while (line[start-j]>=48 && line[start-j]<=57)
    {
        number=stoi(&line[start-j]);
        j++;

    }
    return number;

}
  
int main() 
{ 
    unsigned int red = 0, green = 0, blue = 0;
    unsigned int max_red = 0, max_green = 0, max_blue = 0;
    int sum = 0, id = 0;
    
    ifstream inputFile("input2.txt"); 
    if (!inputFile.is_open()) { 
        cerr << "Error opening the file!" << endl; 
        return 1; 
    } 
    
    string line;
    while (std::getline(inputFile, line))
    {
        id = red = green = blue = 0;
        max_red = max_green = max_blue = 0;


        for(int i=0;i<line.size();i++){
        
            if (line.substr(i, 3) == "red"){
                red=red+find_number(i-2,line);
                max_red=max(red,max_red);

            }
            else if (line.substr(i, 5) == "green"){
                green=green+find_number(i-2,line);
                max_green=max(green,max_green);

            }
            else if (line.substr(i, 4) == "blue"){
                blue=blue+find_number(i-2,line);
                max_blue=max(blue,max_blue);
            }
            else if (line[i]==':'){
                id=find_number(i-1,line);
            }
            else if (line[i]==';'){
                red=0;
                green=0;
                blue=0;
            }
        }
        if( max_red<=12 && max_green<=13 && max_blue<=14){
            sum=sum+id;
        }
    }
    cout << sum;
    return 0;
}