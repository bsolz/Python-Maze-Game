#include <utility>
#include <vector>
#include <string>
#ifndef _MAZE_H
#define _MAZE_H

class Maze{
    private:
        int n;
        int m;

    public:
        std::vector<std::vector<int> > Visited;
        std::vector<std::vector<int> > FinalMaze;
        Maze(int rows, int cols);
        void RunAlgorithm();
        void OutPut(std::string File, int n, int m);
        ~Maze();
};


#endif

//2 2d grids, 1 with values, 1 with visited
// Set 1 = to 15s
// Grid[0][0] -= 8
// Grid[0][0] -= 4