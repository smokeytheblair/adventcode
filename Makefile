CC=g++
FLAGS= -std=c++-17 -Wall

advent1: advent1.cpp
	$(CC) $(FLAGS) advent1.cpp -o advent1

advent2: advent2.cpp
	$(CC) $(FLAGS) advent2.cpp -o advent2


