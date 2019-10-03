#ifndef DOCSUMMARY_H
#define DOCSUMMARY_H

#include <string>
#include <vector>
#include <iostream>
#include "WordCountPair.h"
#include <algorithm>

class DocSummary
{
    public:
        DocSummary(const std::string);
        virtual ~DocSummary();
        void printSummary();
        void analyseDocument();

    protected:

    private:
        //is an integer that indicates the number of words in the document
        int numberOfWords;

        // is an integer that indicates the number of sentences in the document
        int numberOfSentences;

        // is a string that shows the name of the document
        std::string fileName;

        // is a vector of WordFreqPair objects. Each entry of the vector holds a WordFreqPair
        // object that keeps the word and its count.
        std::vector<WordCountPair> wordList;

        void increaseSentenceCount(const std::string);
        void addWord(const std::string);
        void removePunc(std::string &);


};

#endif // DOCSUMMARY_H

