#include <bits/stdc++.h>
using namespace std;

class hammingCode
{
    char c;
    vector<bool> bitset;
    vector<bool> data;
    map <int,vector<int>> m;
    public:
    hammingCode()
    {
        c = 0;
        int arr[] = {1,3,5,7,9,11,13,15};
        m.insert( make_pair( 1,vector <int > ( begin(arr),end(arr) ) ) );
        int arr1[] = {2,3,6,7,10,11,14,15};
        m.insert( make_pair( 1,vector <int > ( begin(arr1),end(arr1) ) ) );
        int arr2[] = {4,5,6,7,12,13,14,15};
        m.insert( make_pair( 1,vector <int > ( begin(arr2),end(arr2) ) ) );
        int arr3[] = {8,9,10,11,12,13,14,15};
        m.insert( make_pair( 1,vector <int > ( begin(arr3),end(arr3) ) ) );
    }
    void getInput();


    void displayVector(vector<bool> v)
    {
        cout<<setw(10)<<"Data : ";
        for( auto it = bitset.begin() + 1 ; it != bitset.end() ;it++ )
        {
            cout<<setw(5)<<*it;
        }
        cout<<endl;
        cout<<setw(10)<<"Index : ";
        for(int i=1;i<bitset.size();i++)
        {
            cout<<setw(5)<<i;
        }
        cout<<"\n"<<endl;
    }
};


void hammingCode :: getInput()
{
    cout<<"\n\nEnter Character : ";
    int t;
    cin>>t;
    if(t > 127 || t < 0)
    {
        cout<<"Invalid Number"<<endl;
        exit(0);
    }
    c = (char)t; 
    //cin>>c;
    while(c!=0)
    {
        int r = c%2;
        c = c/2;
        bitset.push_back(r);
        //data.push_back(r);
    }
    reverse(bitset.begin(),bitset.end());
    //reverse(data.begin(),data.end());
    bitset.insert(bitset.begin(),NULL);
    //data.insert(data.begin(),NULL);
    bitset.insert(bitset.begin()+1,NULL);
    bitset.insert(bitset.begin()+2,NULL);
    bitset.insert(bitset.begin()+4,NULL);
    bitset.insert(bitset.begin()+8,NULL);
    displayVector(data);
    displayVector(bitset);
}


int main()
{
    hammingCode ob;
    ob.getInput();
}
