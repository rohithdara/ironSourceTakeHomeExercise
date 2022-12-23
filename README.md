# Tapjoy/ironSource Take Home Project

I kept this project fairly simple while still meeting all of the requirements in the spec. I wrote a small test file to showcase what testing this program might look like. While writing the code, I could see a problem like this being a candidate for some parallel processing but for the sake of this take home project, I didn't go further into it. If that is a direction that you would like me to explore, please let me know and I can adapt accordingly.

Assumptions I made:
1. There are no nested brackets
2. Every open bracket will have a corresponding closing bracket


## How to run the program
Make sure you have python3 installed. If not please visit, https://www.python.org/downloads/.

Navigate to the parent directory `/Tapjoy`

To run the program, run the following command in your terminal:
`python3 main.py`

To change what file to run, change the argument in line 54 (`printValidStrings("big_input.txt")`) with the string of the desired file name

To run the tests, run the following command in your terminal:
`python3 testMain.py`


To create a big text file to use as input, uncomment line 53 (`createInputFile("provided_input.txt")`).


## High Level Solution
1. Open the file and read it line by line
2. Split the line into a list of stringContents using the brackets as delimiters
3. Iterate through the list of stringContents and check if it contains a valid sequence
    1. If it contains a valid sequence and is within brackets, break and continue to the next line
    2. If it contains a valid sequence and is outside of brackets, set a shouldPrint variable to True. Only print if it reaches the end of the line without having a valid sequence inside brackets. Count the number of strings that are printed.


## Thought Process:
The complexity in this problem arose from trying to make the program more efficient to handle larger text files. By using the createInputFile method, I made a file of about 600 megabytes to test the performance of my code against a large input. 

Attempt #1 uses regex twice: once to extract the bracket contents and once to extract the contents outside of the brackets. While this was a good attempt, using regex twice means processing the full string more than once. A couple of things I also learned when optimizing this method are:
* Determining the sequence validity within the function rather than passing it to another function made the program about 13% faster (106 seconds to 91 seconds)
* Taking out the string slicing and reversal made the program about 33% faster (91 seconds to 61 seconds)

The idea between attempt #2 was to take out all usage of regex and only go through the string once, with a condition when the loop hits an opening bracket. This wasn't as efficient as there was no early exit condition. Not knowing where the opening and closing brackets were based until running into them led to a lot of back and forth between the main function and the checkBrackets helper function. 

The idea between attempt #3 was to use a queue. Using a deque, appending and removing elements would be an O(1) operation. However, while it is efficient to access the first and last element in a deque, it is not as efficient as a list to access elements in the middle. This slowed the program down heavily.

While there was some sporadicness, a general estimate of how long each attempt took to run against a 600mb file is provided below:
* Final Method: 59.01037096977234
* Attempt 1: 72.77116799354553
* Attempt 2: 97.39228701591492
* Attempt 3: 146.69865107536316