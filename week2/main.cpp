#include <iostream>

// Removed global using namespace std in favour of being specific at the time

// A sad non-functional sorting algorithm :(
// Can you locate and fix the error?

int main()
{
    // Added const because it is
    // Made uppercase because it signifies a constant
	const int SIZE = 10;
    // Added
    bool changed;
    // Declared temp, i & j here so that they don't get remade loads of times
    int temp, i, j;
	// replace 10 with SIZE
	int arr[SIZE] = { 9,0,7,6,8,4,3,2,1,5 };

    // Don't need to go as high as size
	for (i = 0; i < SIZE - 1; i++)
	{
        // Added
        changed = false;
        // added -1-i enhancement
        // the actual bug was not having minus 1
        // as it goes past end of array
		for (j = 0; j < SIZE - 1 - i ; j++)
		{
			if (arr[j] > arr[j + 1])
			{
				temp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = temp;
				// added
				changed = true;
			}
		}
		// added
		if (!changed) break;
	}

    // Removed int from here so we reuse a variable
    for (i = 0; i < SIZE; i++)
    {
        std::cout << arr[i] << "  ";
    }
    // added so that the command prompt is nice and orderly
    std::cout << std::endl;
}
