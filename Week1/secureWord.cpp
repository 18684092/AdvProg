#include "secureWord.h"
#include "string.h"

/*
Author: Andy Perrett (18684092)
Assignment: Week 1 workshop

Note that the function assignments / class definition secureWord.h
was given and couldn't be altered

*/


void secureWord::encryptWord(char input[100], int inputKey, bool flag)
{
	// Store details
	size = strlen(input);
	key = inputKey;

	// Encrypt or just store
	if (!flag)
	{
		// Encrypt & store
		for (int i = 0; i < size; i++)
		{
			word[i] = (((input[i] - 97) + inputKey) % 26) + 97;
		}
	}
	else
	{
		// Just store
		for (int i = 0; i < size; i++)
		{
			word[i] = input[i];
		}
	}

	// Terminate char array
	word[size] = '\0';

	encrypted = true;
}


// Compare data with stored word
bool secureWord::compare(char data[100])
{
	// Quick test
	if (strlen(data) != (unsigned int)size) return false;

	// Temp variable buffer
	char encryptedData[100];

	// Encrypt data
	for (int i = 0; i < size; i++)
	{
		encryptedData[i] = (((data[i] - 97) + key) % 26) + 97;
	}
	encryptedData[size] = '\0';

	// compare encrypted data with encrypted word
	for (int i = 0; i < size; i++)
	{
		// If one letter is different test fails!
		if (encryptedData[i] != word[i]) return false;
	}

	// Must be the same
	return true;
}
