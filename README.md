codekata
========

codekata2
---------

Write a binary chop method that takes an integer search target and a sorted array of integers. It should return 
the integer index of the target in the array, or -1 if the target is not in the array. The signature will logically 
be:

   chop(int, array_of_int)  -> int

You can assume that the array has less than 100,000 elements. For the purposes of this Kata, time and memory 
performance are not issues (assuming the chop terminates before you get bored and kill it, and that you have enough 
RAM to run it).

Python implementation in binary_chop.py
JS implementation with karma test runner in folder js_binary_chop


codekata4
---------

Part One: Weather Data

In weather.dat you’ll find daily weather data for Morristown, NJ for June 2002. Write a program to output the day 
number (column one) with the smallest temperature spread (the maximum temperature is the second column, the minimum 
the third column).

Part Two: Soccer League Table

The file football.dat contains the results from the English Premier League for 2001/2. The columns labeled ‘F’ and 
‘A’ contain the total number of goals scored for and against each team in that season (so Arsenal scored 79 goals 
against opponents, and had 36 goals scored against them). Write a program to print the name of the team with the 
smallest difference in ‘for’ and ‘against’ goals.

Part Three: DRY Fusion

Take the two programs written previously and factor out as much common code as possible, leaving you with two 
smaller programs and some kind of shared functionality.

Python implementation in weather.py

