#include <iostream>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <random>
#include <set>
#include <string> 

#include "test.hh"
using namespace std;

const int LIMIT = 50;
int getRandom(int upper)
{
	std::random_device rd;
	std::mt19937 gen(rd());
	std::uniform_int_distribution<> dis(0, upper);
	// To generate a number:
	return dis(gen);
}

int *getRandomArray(unsigned int size)
{

	std::set<int> s;
	const int OFFSET = getRandom(5) + 1;
	int counter = 1;
	while (s.size() < size)
	{
		if (s.size() < size - OFFSET)
			s.insert(getRandom(size + int(size / 2)) + OFFSET);
		else
			s.insert(*s.begin() + counter++);
	}
	static vector<int> v(s.begin(), s.end());
	return &v[0];
}

int *getSequence(int size)
{
	static vector<int> v(size);
	const int rnd = getRandom(size);
	for (int x = 0; x < size; ++x)
		v[x] = rnd + x;
	return &v[0];
}

void test(int size, bool isIter, bool isRnd)
{
	int *arr = isRnd ? getRandomArray(size) : getSequence(size);
	// print out the array
	for (int i = 0; i < size && i < LIMIT; i++)
		cout << arr[i] << (i != size - 1 && i != LIMIT - 1 ? ", " : "");
	cout << endl;

	// student's missing calculated - our missing2 for comparison
	const int missing = isIter ? searchSmallestMissingIteration(arr, size) : searchSmallestMissing(arr, 0, size-1);
    cout << (missing==NO_VALUE_MISSING?"No value ":std::to_string(missing)) << "missing!" << endl;
}

int main(int argc, char *argv[])
{
    // size must be given as the first command line param
    if (argc >= 2)
    {
        // if the second command line param exists, then this is recursion
        bool isIter = argc > 2 ? false : true;
        char *p;
        long l_size = strtol(argv[1], &p, 10);
        int size = (int)l_size;
        test(size, isIter, true);
        return EXIT_SUCCESS;
	}
    // running the default tests for both functions
    bool isIter = true;
    cout << "testing missing.cc"<<endl;
    std::vector<int> sizes ={10, 100, 1000, 10000};
    for (unsigned int size : sizes){
        test(size, isIter, true);
    }
    cout << endl<<"testing missing2.cc"<<endl;
    isIter = false;
    for (unsigned int size : sizes){
        test(size, isIter, true);
    }
}
