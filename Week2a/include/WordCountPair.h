#ifndef WORDCOUNTPAIR_H
#define WORDCOUNTPAIR_H

#include <string>

class WordCountPair
{
    public:
        WordCountPair();
        WordCountPair(const std::string, int);
        virtual ~WordCountPair();

        void setWord(const std::string);
        std::string getWord();
        void setCount(int);
        int getCount(const std::string);

    protected:

    private:
        // is a string that holds a word
        std::string word;

        // is an integer that holds the number of occurrences of the word in the document
        int count;
};

#endif // WORDCOUNTPAIR_H
