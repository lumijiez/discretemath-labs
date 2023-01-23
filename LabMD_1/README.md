# Subsets
Given an integer array set of unique elements, return all possible subsets (the power set).
Return the solution in any order.

# XNOR
Create a program that would ask for two boolean values (true or false, 0 or 1) and would output the result for the XNOR operation performed on them.
You're allowed to use only `and`, `or` and `not` operations.

# Longest substring
You have a string T. In this exercise you need to write two programs that work with subsets of the string t. The first program consists of having the string t, and you need to check all duplicated substring: (contiguous) substrings of t that occur 2 or more times. The occurrences may overlap. Return any duplicated substring that has the longest possible length. If t does not have a duplicated substring, the answer is "".The second program consists of having the string t and you need to find the length of the longest substring without repeating characters.

# Truth table solver
You have to write a program that computes the truth table for various expressions. The set of expressions are limited to:
- `and` operation
- `or` operation
- `not` operation
- supports parenthesis

# Sierpinski triangle
Write a program that prints the Sierpinski triangle for the depth `n`, where `n` is an input value.

# Bonus: A game of life foreplay (aka [Elementary cellular automaton]
In this problem we're going to take a look at elementary cellular automaton. Every cell is like a small microorganism with a few primitive rules. When combining with other cells they form interesting patterns. There also is an interesting ted talk  given by Stephen Wolfram that touches on this topic.
Your task is to randomly generate a list (let's say of length 200, it's up to you in the end, just make sure to be long enough) containing only the numbers `0` and `1`. Then you start iterating over the list in order to compute the *next generation*. The rules that apply for the next generation are the following. 

111 0
110 1
101 1
100 0
011 1
010 1
001 1
000 0


For instance if the cells `1`, `2` and `3` have the value `1 1 0` the 2nd cell of the next generation will be  `1`.
 
Note:
For computing the first and the last cell you can consider the missing parent to be `0`.
Now you have to compute the next 100 generations and print the resulting matrix with colour for value `1` and with white for value `0`. Once You've done that, try to change the first generation from randomly generated numbers to all values to be `0` and the last element is `1`. Observe the result. 
The rule applied above is called rule 110, there is actually a list of rules that renders quite interesting patterns.
Change arbitrary the initial rule and observe the differences.
Maybe you can find a new interesting pattern for Bunica's covor.
 - Bonus task:
Make your program in a way that it would be easy to change the number of pixels rendered for every cell. For instance my cell is 1 x 1 pixels. And by changing one or two variables my cell would change to 5 x 5 pixels.
