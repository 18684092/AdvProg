/*
Author: Andy Perrett (18684092)
Assignment: Week 1 workshop

Note that the function assignments / class definition secureWord.h
was given and couldn't be altered

c++14

*/

#include "string.h"
#include <iostream>
#include <fstream>
#include "secureWord.h"


// Simple display of object
void displaySecureWord(secureWord secure)
{
	std::cout << "Secure word:   " << secure.word << std::endl;
	std::cout << "Size:          " << secure.size << std::endl;
	std::cout << "Key:           " << secure.key << std::endl;
	std::cout << "Encrypted:     " << (secure.encrypted ? "true" : "false") << std::endl;
	std::cout << std::endl;
}


int main()
{
	// Create array of secureWord
	//
	secureWord secureList[8];

	char word[100];
	bool flag;
	int key;

	// Load input file into array
	std::ifstream infile("input.txt");
	if (infile.is_open())
	{
		int count = 0;

		// multiple white spaces are treated as one
		// Let's presume file is in correct form BUT it should be checked for
		// validity in an ideal world !!!!
		while (infile >> word >> flag >> key)
		{
			// THERE SHOULD BE SOME SECURITY / SANITY CHECKING HERE
			// So this is a token effort for now
			if (strlen(word) <= 100)
			{
				std::cout << "Original word: " << word << std::endl;
				secureList[count++].encryptWord(word, key, flag);
				displaySecureWord(secureList[count - 1]);
			}
		}
		infile.close();
	}
	else
	{
		std::cout << "File Not Found: input.txt" << std::endl;
		// Throw exception is a nice way to tidy up and release memory
		throw std::exception();
		return -1;
	}

	// Get word from user - test if it is one of the secure words
	char input[100];
	bool found;

	// Main loop
	while (true)
	{

		std::cout << "Enter an unencrypted word to test. (Q to exit)" << std::endl;
		std::cin >> input;

		// Exit?
		if (input[0] == 'Q' || input[0] == 'q') return 0;

		// Check against each word
		found = false;
		for (int i = 0; i < 8; i++)
		{
			if (secureList[i].compare(input))
			{
				found = true;
				break;
			}
		}

		// Inform user
		if (found)
		{
			std::cout << "Match!!! That is a secure word." << std::endl << std::endl;
		}
		else
		{
			std::cout << "That is NOT a secure word!" << std::endl << std::endl;
		}
	}

	return 0;
}

