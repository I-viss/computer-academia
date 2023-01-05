#include <iostream>

using namespace std;

struct Phone {
    string brand;
    string name;
    string os;
    int ram_memory;
    int memory;
    double price;
    
    //let me introduice getters 
    string getBrand(){ return brand; }
    
    string getName() { return name;}
    
    string getOS() { return os; }
    
    int getRamMemory() { return ram_memory;}
    
    int getMemory() { return memory; }
    
    double getPrice() { return price; }
    
    // let me introduice setters 
    void setName(string phoneName) { name  = phoneName; }
    
    void setBrand(string phoneBrand) {brand = phoneBrand;}
    
    void setOS(string phoneOs){os = phoneOs; }
    
    void setRamMemory(int ramMemory){ ram_memory = ramMemory;}
    
    void setMemory(int phoneMemory){ memory = phoneMemory;}
    
    void setPrice(double phonePrice){ price = phonePrice;}
    
    // all these functions are called methods 
    
    void printPhoneInformation(){
        
        cout << "\nBrand :" << getBrand();
        
        cout << "\nName :" << getName();
        
        cout << "\nOS :" << getOS();
        
        cout << "\nRam memory :" << getRamMemory();
        
        cout << "\nMemory :" << getMemory();
        
        cout << "\nPrice :" << getPrice();
    }
    
};

int main()
{
    
    Phone p;
    p.setName("Iphone 14");
    p.setBrand("Apple");
    p.setOS("Mac os");
    p.setRamMemory(4);
    p.setMemory(64);
    p.setPrice(1500);
    
    p.printPhoneInformation();
    return 0;
}
