#include <bits/stdc++.h>
using namespace std;

class hammingCode
{
    static char c;
    static vector<bool> bitset;
    hammingCode()
    {
        c = NULL;
        bitset = NULL;
    }
    void getInput();
}


void hammingCode :: getInput()
{
    cout<<"Enter Character : ";
    cin>>this.c;
    
    while(c!=0)
    {
        
    }
}


int main()
{
    int i='a';
    char buff[33];
    itoa(i,buff,2);
    string s = std::string(buff);
    cout<<s<<endl;;
}
