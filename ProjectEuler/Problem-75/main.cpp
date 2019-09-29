#include <iostream>
#include <cmath> // sqrt
#include <algorithm> // gcd
/*
THIS BRUTE FORCE WAY WORKS!!!!

How ever, it takes about 15 minutes so needs rewriting. At least the logic is correct.
I need to introduce a bit more maths as per
https://en.wikipedia.org/wiki/Pythagorean_triple

New way below works under 1 second!

*/

#define SIZE 1500000

int main()
{
    int opp = 2, adj = 1;
    // NOTE = { } inits all to zero, without it you get rubbish (ie, wrong count)
    int lengths[SIZE + 1] = { };
    long length, a, b, c;
    // biggest side can be max of sqrt(size / 2) because
    // biggest hypotenuse is when opp and adj are same and we only need 1 off them
    while (opp < (int)std::sqrt(SIZE / 2.0f)) // m
    {
        // wiki page "If m and n are two odd integers such that m > n, then"
        for (adj = 1; adj < opp; ++adj) // n
        {
            // we have odd & coprime
            if ( (((opp + adj) % 2) == 1) && (std::__gcd(opp, adj) == 1) )
            {
                // wiki page "a=m^2-n^2, b=2mn, c=m^2+n^2 with m and n coprime and of opposite parities."
                // These are primitive Pythagorean triple
                // (3, 4, 5) when m = 2, n = 1
                a = (opp * opp) - (adj * adj);  // adj
                b = 2 * (opp * adj);            // opp
                c = (opp * opp) + (adj * adj);  // hyp
                length = a + b + c;
                // Once we have an odd + coprime all others will be multiples
                // up to our size
                while (length <= SIZE)
                {
                    lengths[length] += 1;
                    length += a + b + c;
                }
            }
        }
        ++opp; // ++opp is technically quicker than opp++
    }

    // Count single integer right angle triangles that have length of wire less or
    // equal to 1500000
    int count = 0;
    for(int len = 1; len <= SIZE; ++len)
    {
        if (lengths[len] == 1) count++;
    }
    std::cout << "total = " << count << std::endl;
}
