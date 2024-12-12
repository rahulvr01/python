// Online C++ compiler to run C++ program online
#include <iostream>
using namespace std;
int main() {
    int sn=6;
    int ln=18;
    int hcf,lcm;
    for (int i=1;i<=sn;++i)
    {
        if(sn%i==0 && ln%i==0)
    {
        hcf=i;
    }
    }
    cout<<hcf;
    lcm=(sn*ln)/hcf;
    cout<<lcm;
}
    
