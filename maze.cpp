#include "maze.h"
#include <iostream>
#include <vector>
#include <utility>
#include <ctime>
#include <cstdlib>
#include <sstream>
#include <fstream>

Maze::Maze(int rows, int cols)
{
    this->n = rows;
    this->m = cols;

    Visited.resize(rows + 2);
    for (int i = 0; i < rows + 2; ++i){
        Visited[i].resize(cols + 2);
    }

    FinalMaze.resize(rows + 2);
    for (int i = 0; i < rows + 2; ++i)
    {
        FinalMaze[i].resize(cols + 2);
    }

    for(int i = 0; i < n + 2; i++){
        for(int j = 0; j < m + 2; j++){
            if(i == 1 && j == 1){
                FinalMaze[i][j] = 7;
            }
            else if(i == n && j == m){
                FinalMaze[i][j] = 11;
            }
            else{
                FinalMaze[i][j] = 15;
            }
        }
    }

    for (int i = 0; i < n + 2; i++)
    {
        for (int j = 0; j < m + 2; j++)
        {
            if(i == 0 || j == 0 || i == n + 1 || j == m + 1){
                Visited[i][j] = 2;
            }
            else{
                Visited[i][j] = 0;
            }
            
        }
    }
}

Maze::~Maze(){

}

void Maze::RunAlgorithm(){
    std::pair<int, int> Init;
    Init.first = 1;
    Init.second = 1;

    std::vector<std::pair<int, int> > A;
    Visited[1][1] = 1;
    A.push_back(Init);
    while (A.size() > 0)
    {
        std::pair<int, int> Current = A.back();
        std::pair<int, int> Temp;
        A.pop_back();

        std::vector<std::pair<int, int> > Neighbors;

        if (Visited[Current.first - 1][Current.second] == 0)
        {
            Temp.first = Current.first - 1;
            Temp.second = Current.second;
            Neighbors.push_back(Temp);
        }
        if (Visited[Current.first + 1][Current.second] == 0)
        {
            Temp.first = Current.first + 1;
            Temp.second = Current.second;
            Neighbors.push_back(Temp);
        }
        if (Visited[Current.first][Current.second + 1] == 0)
        {
            Temp.first = Current.first;
            Temp.second = Current.second + 1;
            Neighbors.push_back(Temp);
        }
        if (Visited[Current.first][Current.second - 1] == 0)
        {
            Temp.first = Current.first;
            Temp.second = Current.second - 1;
            Neighbors.push_back(Temp);
        }

        std::pair<int, int> Neigh;

        if(Neighbors.size() > 0){
            A.push_back(Current);
            int idx = std::rand() / ((RAND_MAX + 1u) / Neighbors.size());
            Neigh = Neighbors[idx];

            //Remove Walls
            if(Neigh.first == Current.first - 1 && Neigh.second == Current.second){
                FinalMaze[Neigh.first][Neigh.second] -= 4;
                FinalMaze[Current.first][Current.second] -= 8;
            }
            else if (Neigh.first == Current.first + 1 && Neigh.second == Current.second)
            {
                FinalMaze[Neigh.first][Neigh.second] -= 8;
                FinalMaze[Current.first][Current.second] -= 4;
            }
            else if (Neigh.first == Current.first && Neigh.second == Current.second + 1)
            {
                FinalMaze[Neigh.first][Neigh.second] -= 1;
                FinalMaze[Current.first][Current.second] -= 2;
            }
            else
            {
                FinalMaze[Neigh.first][Neigh.second] -= 2;
                FinalMaze[Current.first][Current.second] -= 1;
            }

            Visited[Neigh.first][Neigh.second] = 1;
            A.push_back(Neigh);
        }
        Neighbors.clear();
    }
    if(n == 1 && m == 1){
        FinalMaze[1][1] = 3;
    }

    
}

void Maze::OutPut(std::string File, int n, int m){
    std::ofstream outPut(File + ".txt");
    if (outPut.is_open())
    {
        for (int i = 1; i < n + 1; i++)
        {
            for (int j = 1; j < m + 1; j++)
            {
                outPut << FinalMaze[i][j] << " ";
            }
            outPut << '\n';
        }
        outPut.close();
    }
}