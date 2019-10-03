#include "WordCountPair.h"

// Defaults constructor. Sets word to null string and count to zero.
WordCountPair::WordCountPair() : word(""), count(0)
{

}

// Takes a word and its count as parameters and initialize the word and
// count member variables. Sets count to one if the second parameter is not
// supplied.
WordCountPair::WordCountPair(const std::string str, int c = 1) : word(str), count(c)
{

}

WordCountPair::~WordCountPair()
{
    //dtor
}

// Sets word variable with the input
void WordCountPair::setWord(const std::string str)
{
    word = str;
}

// Returns word
std::string WordCountPair::getWord()
{
    return word;
}

// Sets count variable with the input
void WordCountPair::setCount(int c)
{
   count = c;
}

// Set count variable with the input
int WordCountPair::getCount(const std::string str)
{
    return str.length();
}
