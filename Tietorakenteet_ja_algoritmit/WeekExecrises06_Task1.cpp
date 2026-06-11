#include <iostream>
#include <map>
#include <vector>
#include <set>

using namespace std;

struct person {
    int id;
    string name;
    int birth_year;
    int year_of_death;
    string sex;
    int mother;  // äidin id
    int father;
    set<int> children;
    set<int> spouses;
    set<int> relativs; // joukkoyhdiste children, spouses, mother, father
};

int main()
{
    map<int, person> family_tree;
}
