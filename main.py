import re

# Iterate through a file line by line and print out the lines that contain a valid sequence according to the spec
def printValidStrings(filename):
    validStringCount = 0
    with open(filename) as f:
        for line in f:
            
            # split the line into a list with open and closed brackets as the delimiters
            stringContents = re.split('\[|\]', line.strip())
            shouldPrint = False
            
            for i in range(len(stringContents)):
                if not stringContents[i]:
                    continue
    
                # check string inside of bracket
                if i%2 != 0 and hasValidSequence(stringContents[i]):
                    shouldPrint = False
                    break
                    
                # check string outside of bracket   
                elif hasValidSequence(stringContents[i]):
                    shouldPrint = True
                            
            if shouldPrint:
                validStringCount+=1
                print(line.strip())
                
    print(f"This file had {validStringCount} valid string(s)")
 

# Given a string, determine if it contains any 4 char sequence which has a pair of two different characters followed by the reverse of that pair
def hasValidSequence(s):
    for i in range(len(s) - 3):
        if s[i] == s[i+3] and s[i+1] == s[i+2] and s[i] != s[i+1]:
            return True
    return False 


# Given a text file, read the file and write the contents to a new text file repeatedly to create a large text file
def createInputFile(filename):
    f = open(filename, 'r')
    inputContent = f.readlines()
    print(inputContent)
    with open("big_input.txt", "a") as big_input:
        for _ in range(500000):
            for line in inputContent:
                big_input.write(line)


if __name__ == "__main__":
    #createInputFile("provided_input.txt")
    printValidStrings("big_input.txt")
        

# ==================================================================================================================================
# Previous working versions of this code that were scrapped due to finding more efficient ways to do the task at hand

# import time
# from collections import deque


# def attempt1(filename):
#     start = time.time()
#     validCount = 0
#     with open(filename) as f:
#         for line in f:
#             bracketContents = re.findall(r'\[(.*?)\]', line)
#             if checkBracketContents(bracketContents):
#                 newLine = re.sub("[\(\[].*?[\)\]]", "", line)
#                 for i in range(len(newLine) - 3):
#                     if newLine[i] == newLine[i+3] and newLine[i+1] == newLine[i+2] and newLine[i] != newLine[i+1]:
#                     #if newLine[i:i+2] == newLine[i+2:i+4][::-1] and newLine[i] != newLine[i+1]:
#                         validCount += 1
#                         print(line.strip())
#                         break
#     end = time.time()
#     print(end-start)
    
    
# def attempt2(filename):
#     start = time.time()
#     validCount = 0
#     with open(filename) as f:
#         for line in f:
#             charPos = 0
#             invalid = False
#             shouldPrint = False
#             lineCopy = line.strip()
#             while charPos < len(line) - 3:
#                 if line[charPos+3] == '[':
#                     invalid, line = checkBracketContents2(line[charPos+3:])
#                     if invalid:
#                         shouldPrint = False
#                         break
#                     charPos = 0
#                     continue
#                 elif line[charPos] == line[charPos+3] and line[charPos+1] == line[charPos+2] and line[charPos] != line[charPos+1]:
#                 #isValidSequence(line[charPos:charPos+4]):
#                     shouldPrint = True 
#                 charPos += 1

#             if shouldPrint:
#                 validCount += 1
#                 print(lineCopy)
#     end = time.time()
#     print(end-start)
                

# def attempt3(filename):
#     start = time.time()
#     validCount = 0
#     with open(filename) as f:
#          for line in f:
#             bracketContents = re.findall(r'\[(.*?)\]', line)
#             if checkBracketContents(bracketContents):
#                 queue = deque()
#                 insideBracket = False
#                 for i in range(len(line)):
#                     if line[i] == '[':
#                         insideBracket = True
#                         queue.clear()
#                     elif insideBracket and line[i] == ']':
#                         insideBracket = False
#                     else:
#                         queue.append(line[i])
#                         if len(queue) < 4:
#                             continue
#                         elif queue[0] == queue[-1] and queue[1] == queue[2] and queue[0] != queue[1]:
#                             print(line.strip())
#                             validCount+=1
#                         queue.popleft()
#     end = time.time()
#     print(end-start)


# ==================================================================================================================================
# Helper Functions I did not end up using due to change in approach or efficiency   

# def checkBracketContents(bracketContents):
#     for s in bracketContents:
#         if len(s) < 4:
#             continue
#         for i in range(len(s) - 3):
#             if s[i:i+2] == s[i+2:i+4][::-1] and s[i] != s[i+1]:
#                 return False
#     return True

                
# def isValidSequence(sequence):
#     return sequence[0:2] == sequence[2:4][::-1] and sequence[0] != sequence[1]
        

# def checkBracketContents2(content):
#     charPos = 0
#     while content[charPos + 3] != ']':
#         if content[charPos:charPos+2] == content[charPos+2:charPos+4][::-1] and content[charPos] != content[charPos+1]:
#             return True, ""

#         charPos += 1
#     return False, content[charPos+3:]
