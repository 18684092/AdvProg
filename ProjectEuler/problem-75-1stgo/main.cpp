#include <iostream>
#include <cmath>
#define SIZE 1500000

/*
Author: Andy Perrett
Brute force problem 75!
Takes 18 minutes or so.

*/

int main()
{
    // Buffer to store results
    int lengths[SIZE + 1] = { };
    // Needs to be a long
    long length;
    // Needs to be floaty types
    double hyp, opp, adj;
    // Make one side of the triangle
    for (opp = 1; opp < (int)(SIZE / 2); ++opp)
    {
        // make the second side - it must be smaller!
        for (adj = 1; adj < opp; ++adj)
        {
            // Now make the hypotenuse - 3rd side
            hyp = std::sqrt((opp * opp) + (adj * adj));

            // if it is an integer
            if ((long)hyp == hyp)
            {
                // Work out the length of the wire
                length = (long)hyp + opp + adj;
                // As long as it is within our size range
                if (length <= SIZE)
                {
                    // Store it and record how many times this length has been seen
                    lengths[length] += 1;
                }
            }
        }
    }

    // Count how many "single" right angled triangles there are
    int count = 0;
    for (int i; i < SIZE; ++i)
    {
        // Is it a single
        if (lengths[i] == 1) count++;
    }
    // Give the answer
    std::cout << "Total = " << count << std::endl;
}
