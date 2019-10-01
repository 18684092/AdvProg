#include "DocSummary.h"

/*
Takes document name as input and initializes class variables
*/
DocSummary::DocSummary(const std::string file)
{
    fileName = file;
}

DocSummary::~DocSummary()
{
    //dtor
}

/*
Prints the number of sentences, the number of
words and each word with its frequency (see
format at the end of the assignment)
*/
void DocSummary::printSummary()
{

}

/*
Reads the document word by word and calls addWord,
removePunc, updateSentenceCount functions in the correct
order to fill in the object properties
*/
void DocSummary::analyseDocument()
{

}

/*
Adds a given word into the wordList vector if it does not exist in the
vector. Otherwise it increases the corresponding count entry in vector.
*/
void DocSummary::addWord(std::string)
{

}

/*
Takes a word as an input and increases the variable numberOfSentences
if the given word contains a “.”, ”!” or “?” symbol.
*/
void DocSummary::increaseSentenceCount(std::string)
{

}
