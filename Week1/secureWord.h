#pragma once

/* SECURE_WORD_H
   Implements a Secure word class which contains a word in the form of a static character array.
   The length of the word is given
   If the boolean variable encrypted is set to true, the original word can be reciphered using the key.

   Note that all members in this class is public, which is not the suggested practice. However, we will
   not dig this now as this is your first lab.

   Create a SecureWord.cpp and define your functions in that file as we saw in class

   Author: Ayse Kucukyilmaz
*/
class secureWord {

public:
	char word[100];
	int size; //length of the word
	int key;
	bool encrypted;

	/*
		In this function you will set object variables, size,key, encrypted and word.
		Also you will encrypt the input and store in word, if it is not encrypted.
		There will be no file or input/output operation in this function.
		Also you can not change the structure of the function.

		You can use strlen function in string library.
	*/
	void encryptWord(char [100], int, bool );

	/*
		In this function, an unencrypted data will come and you will compare it with the word in the object
		Since word is encrypted you have to do some operation to compare.
		It will return 1 if they are equal

		you can use strcmp function in string library
	*/
	bool compare(char data[100]);
};
