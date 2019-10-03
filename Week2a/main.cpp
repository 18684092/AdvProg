#include "DocSummary.h"

int main()
{
    // Note, if the file is missing we still need to
    // exit / return in am orderly fashion!
    try
    {
        DocSummary doc1("input.txt");
        doc1.analyseDocument();
        doc1.printSummary();
        return EXIT_SUCCESS;
    }
    catch (const std::exception&)
    {
        return EXIT_FAILURE;
    }
}
