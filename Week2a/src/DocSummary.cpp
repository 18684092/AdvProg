#include "DocSummary.h"
#include <fstream>
#include <string>
#include <iostream>

/*
Takes document name as input and initializes class variables
*/
DocSummary::DocSummary(const std::string file) : numberOfWords(0), numberOfSentences(0), fileName(file)
{

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
    std::cout << "File name stats : " << fileName << std::endl;
    std::cout << "------------------" << (std::string (fileName.length(), '-' )) << std::endl;
    std::cout << "No of sentences : " << numberOfSentences << std::endl;
    std::cout << "No of words     : " << numberOfWords << std::endl;

    // Bjarne Stroustrup says use auto as compiler makes less mistakes
    for ( auto &wordPair : wordList )
    {
        int s = wordPair.getWord().length(); // beautify, just make the effort
        std::cout << wordPair.getWord() << (std::string (10 - s, ' '));
        std::cout << wordPair.getCount("") << std::endl;
    }

    std::cout << std::endl;
}

/*
Reads the document word by word and calls addWord,
removePunc, updateSentenceCount functions in the correct
order to fill in the object properties
*/
void DocSummary::analyseDocument()
{
    std::string str;
    std::ifstream myFile(fileName);

    // get each word and add its details
    if (myFile.is_open())
    {
        while (myFile >> str) addWord(str);
        myFile.close();
    }
    else
    {
        // This is here to get used to using exceptions. Without it the program
        // would operate (not crash) but main would return the wrong value!!!
        std::cout << "File: " << fileName << " is missing." << std::endl;

        // This gets caught in main() so that we can return properly
        throw std::exception();
    }
}

/*
 Remove punctuation

 Note I have made it an "inplace" replacement because of the meaning of the
 function name. It suggests removing chars from string rather than returning a new string
*/
void DocSummary::removePunc(std::string &word)
{
    // Check each character, remove punctuation
    for(size_t i = 0; i < word.length(); ++i)
    {
        char c = word[i];
        // Could have used ispunct(word[i]) but we are only told about these 3 chars
        if (c == '.' || c == '?' || c == '!' || c == ',')
        {
            word.erase(i, 1);
        }

    }
}

/*
Adds a given word into the wordList vector if it does not exist in the
vector. Otherwise it increases the corresponding count entry in vector.
*/
void DocSummary::addWord(const std::string str)
{
    // 2 copies of the word, one with and one without punctuation
    std::string word = str;
    removePunc(word);

    bool found = false;

    // Check all words - we don't want a duplicate
    for(size_t i = 0; i < wordList.size(); ++i)
    {

        // Have we seen this word before?
        if (wordList[i].getWord() == word)
        {
            found = true;
            wordList[i].setCount(1);
            break;
        }

    }

    // Only add if necessary
    if (!found)
    {
        WordCountPair newWP(word, 1);
        wordList.push_back(newWP);
    }

    // Any Difference is punctuation
    if (word != str) increaseSentenceCount(str);

    // There must be a word otherwise we wouldn't be here!
    ++numberOfWords;
}

/*
Takes a word as an input and increases the variable numberOfSentences
if the given word contains a “.”, ”!” or “?” symbol.
*/
void DocSummary::increaseSentenceCount(const std::string word)
{
    // any punctuation is a sign of a sentence, so act upon first
    // hit only
    for(size_t i = 0; i < word.length(); ++i)
    {
        char c = word[i];

        if (c == '.' || c == '?' || c == '!')
        {
            // pre increment better than post increment!
            ++numberOfSentences;
            break;
        }

    }
}
