#include "DocSummary.h"


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
    for ( auto &wordPair : wordList )
    {
        std::cout << wordPair.getWord() << (std::string (15 - wordPair.getCount(wordPair.getWord()), ' ')) << " : " << wordPair.getCount(wordPair.getWord()) << std::endl;
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
    WordCountPair word(std::string("word"),1);
    wordList.push_back(word);
    word.setWord("happy");
    wordList.push_back(word);

}

/*
 Remove punctuation

 Note I have made it an "inplace" replacement because of the meaning of the
 function name. It suggests removing chars from string rather than returning a new string
*/
void DocSummary::removePunc(std::string &word)
{
    char c;
    // make i same type as word.length()
    for(size_t i = 0; i < word.length(); ++i)
    {
        c = word[i];
        if (c == '.' || c == '?' || c == '!' || c == ',' || c == ':' || c == ';')
            {
                word.erase(i, 1);
            }
    }
}

/*
Adds a given word into the wordList vector if it does not exist in the
vector. Otherwise it increases the corresponding count entry in vector.
*/
void DocSummary::addWord(const std::string word)
{

}

/*
Takes a word as an input and increases the variable numberOfSentences
if the given word contains a “.”, ”!” or “?” symbol.
*/
void DocSummary::increaseSentenceCount(const std::string word)
{

}
