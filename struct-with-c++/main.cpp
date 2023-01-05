#include <iostream>

using namespace std;

struct Person {
    string first_name;
    string last_name;
    string country;
    string city;
    int age; 
    
};


Person getPersonData(Person p){
    cout << "Enter Person's first name:";
    getline(cin, p.first_name);
    
    cout << "Enter Person's last name: ";
    getline(cin, p.last_name);
    
    cout << "Enter Person's country: ";
    getline(cin, p.country);
    
    cout << "Enter Person's city: ";
    getline(cin, p.city);
    
    cout <<"Enter Person's age: ";
    cin >> p.age;
    return p;
}
void printPersonData(Person p){
    // Salum implements this function to display person data 
}
int main()
{
    Person p1, p2;
    
    p1 = getPersonData(p2);
    
    cout << p1.first_name;
    return 0;
}