
#include <iostream>
#include <fstream>
#include <string>
#include "DocSummary.h"



int main()
{

	DocSummary doc1("input.txt");
	doc1.analyseDocument();
	doc1.printSummary();


}
