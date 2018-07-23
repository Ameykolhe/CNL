#include <bits/stdc++.h>
using namespace std;

class sender
{
	int c;
	vector<bool> bitset;
	bool  *data;
	int dataSize;
	int parityBits;
	friend class receiver;
	public:
	sender()
	{
		data = NULL;
	}

	void getInput();
	void generateParity(int );
	void alterBit()
	{
		int pos;
		cout<<"Enter positon of bit to alter"<<endl;
		cin>>pos;
		if(bitset.size()>pos)
			bitset[pos] = ! bitset[pos];
		else
			cout<<"Invalid Position"<<endl;
	}


	vector<bool> getBitset(){return bitset;}
	bool* getData(){return data;}

	void displayData(vector<bool> v)
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

	void displayData(bool v[])
	{
		cout<<setw(10)<<"Data : ";
		for( int i = 1 ; i<dataSize ; i++ )
		{
			cout<<setw(5)<<v[i];
		}
		cout<<endl;
		cout<<setw(10)<<"Index : ";
		for(int i=1;i<dataSize;i++)
		{
			cout<<setw(5)<<i;
		}
		cout<<"\n"<<endl;
	}
};


class receiver
{
	vector<bool> bitset;
	bool *correctData;
	int dataSize;
	int parityBits;
	bool pass;

	public:
	receiver(sender &o)
	{
		this->bitset = o.bitset;
		this->dataSize = o.dataSize;
		this->parityBits = o.parityBits;
		pass = true;
	}


	void checkParity(int );
	void extractData()
	{
		correctData = new bool[dataSize];
		for(int i = 0 , j = 0 , p = 0 ; i<bitset.size() ; i++)
		{
			if(i == pow(2,p))
				p += 1;
			else
			{
				correctData[j] = bitset[i];
				j+=1;
			}
		}
	}


	vector<bool> getBitset(){return bitset;}
	bool* getCorrectData(){return correctData;}
	
	void displayData(vector<bool> v)
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

	void displayData(bool v[])
	{
		cout<<setw(10)<<"Data : ";
		for( int i = 1 ; i<dataSize ; i++ )
		{
			cout<<setw(5)<<v[i];
		}
		cout<<endl;
		cout<<setw(10)<<"Index : ";
		for(int i=1;i<dataSize;i++)
		{
			cout<<setw(5)<<i;
		}
		cout<<"\n"<<endl;
	}

};


void sender :: getInput()
{
	cout<<"\n\nEnter Input : ";
	cin>>c;

	cout<<endl;
	int temp = c;
	while(temp!=0)
	{
		int r = temp%2;
		temp /= 2;
		bitset.push_back(r);
	}
	reverse(bitset.begin(),bitset.end());

	bitset.insert(bitset.begin(),NULL);
	
	dataSize = bitset.size();
	data = new bool[dataSize];
	copy(bitset.begin(),bitset.end(),data);

	int p = 0;
	for( int i = 0 ; i < 10 ; i++ )
	{
		if( pow(2,i) >= (dataSize + i ) )
		{	
			p = i;
			break;
		}
	}
	parityBits = p;
	for(int i = 0 ; i < p ; i++)
	{
		int t = pow(2,i);
		bitset.insert(bitset.begin() + t , NULL);
	}
	cout<<"Entered Data : \n"<<endl;
	displayData(data);
}


void sender :: generateParity(int x)							// x = 0 even parity     x = 1 odd parity
{
	for(int i = 0;i<parityBits;i++)
	{
		bool fl;
		if(x == 0)
			fl = false;
		else if(x == 1)
			fl = true;
		int t = pow(2,i);
		cout<<"Parity : "<<t<<"\tpos : ";
		for(int j = t + 1 ; j<bitset.size() ; j++)
		{
			if( t&j )
			{
				cout<<" "<<j;
				if(bitset[j] == 1)
					fl = !fl; 
			}
		}
		cout<<"\t\tbit : "<<fl<<endl<<endl;
		bitset[t] = fl;
	}
}


void receiver :: checkParity(int x)
{
	vector <bool> st;
	for(int i = 0;i<parityBits;i++)
	{
		bool fl;
		if(x == 0)
			fl = false;
		else if(x == 1)
			fl = true;
		int t = pow(2,i);
		cout<<"Parity : "<<t<<"\tpos : ";
		for(int j = t ; j<bitset.size() ; j++)
		{
			if( t&j )
			{
				cout<<" "<<j;
				if(bitset[j] == 1)
					fl = !fl; 
			}
		}
		cout<<"\t\tbit : "<<fl<<endl<<endl;
		st.push_back(fl);
		if(fl != 0)
		{
			pass = false;
		}
	}
	int pos = 0;
	for(int i = 0 ; i < st.size() ;i++ )
	{
		if(st[i] == 1)	
		{
			pos += pow(2,i);
		}
	}
	if(!pass)
	{
		cout<<"Error Detected \n Position : "<<pos<<endl<<endl;
		bitset[pos] = !bitset[pos];
		cout<<"Corrected Error\n"<<endl;
	}
	else
	{
		cout<<"Hamming pass\n"<<endl;
	}
}


int main()
{
	sender ob;
	cout<<"-------------------------------------Sender Side----------------------------------------\n"<<endl;
	cout<<"-----------------Input----------------\n";
	ob.getInput();
	cout<<"-------Calculating Parity Bits--------\n"<<endl;
	ob.generateParity(1);
	ob.displayData(ob.getBitset());
	cout<<"-------------Transmission-------------\n"<<endl;
	char ch;
	cout<<"Alter Data ? y/n : ";
	cin>>ch;
	if(ch == 'y' || ch == 'Y')
		ob.alterBit();
	cout<<"---------------Data Sent--------------\n"<<endl;
	ob.displayData(ob.getBitset());
	cout<<"Transmission Complete\n"<<endl;
	cout<<"------------------------------------Receiver Side----------------------------------------\n"<<endl;
	cout<<"-------------Received data------------\n"<<endl;
	receiver r(ob);
	r.displayData(r.getBitset());
	cout<<"-------------checking Parity----------\n"<<endl;
	r.checkParity(1);
	cout<<"-------------received Data------------\n"<<endl;
	r.extractData();
	r.displayData(r.getCorrectData());
}
