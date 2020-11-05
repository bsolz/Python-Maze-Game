#include "maze.h"
#include <iostream>
#include <vector>
#include <utility>
#include <ctime>
#include <cstdlib>
#include <sstream>
#include <fstream>

int main(int argc, char *argv[])
{

    // 1st Argument: Random int seed
    // 2nd Argument: Number of rows
    // 3rd Argument: Number of cols
    // 4th Arguments: Output file name

    unsigned int seed = std::stoi(argv[1]);
    unsigned int n = std::stoi(argv[2]);
    unsigned int m = std::stoi(argv[3]);

    unsigned int iteration = 0;

    //Creates the 500 unique "maps" per level
    for(int i = 499; i >= 0; i--){
    std::srand(seed);
    std::string OutputFile = argv[4] + std::to_string(iteration);

    //Creates a maze object with a 2D vector for visited cells, and a 2d vector for the final output
    Maze Object(n,m);
    Object.RunAlgorithm();
    Object.OutPut(OutputFile, n, m);

    seed++;
    iteration++;
    }

    return 0;
}

