// Online C++ compiler to run C++ program online
#include <iostream>
using namespace std;
int main() {
    int sn=6;
    int ln=7;
    int lcm;
    for (int i=ln;;i=i+ln)
    {
        if(i%sn==0 && i%ln==0)
    {
        lcm=i;
        break;
    }
    
    }
    cout<<lcm;
}
    
