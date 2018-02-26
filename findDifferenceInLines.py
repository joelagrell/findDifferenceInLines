# # Sample Input
# 3
# ATCCGCTTAGAGGGATT
# GTCCGTTTAGAAGGTTT
# abcdefghijklmnopqrstuvwxyz
# bcdefghijklmnopqrstuvwxyza
# abcdefghijklmnopqrstuvwxyz0123456789
# abcdefghijklmnopqrstuvwxyz0123456789

## Information on sys.stdin
#  You run the file from cmd/ps with: "type data.file | python program.py"

import sys

# # Scan all lines/rows/inputs 
#for line in sys.stdin:
Ar = sys.stdin.readlines() 	# Import data from stdin to array Ar.
N = int(Ar[0])				# Store N testcases
# For debugging
# Line1 = Ar[1]
# Line2 = Ar[2]
# print('Stored Value of N')
# print(type(N))
# print(N)
# print('Stored value of array Ar')
# print(type(Ar))
# print(Ar)
# print('')
# print('Stored value of line 1 and 2')
# print(type(Line1))
# print(Line1)
# print(Line1[4])
# print(len(Line1))		

	
# # # Solve the problem: a for loop that will run as many times as test cases there will be.
findTestCaseToRead = 1 	# Set where to start reading for the testlines in the array Ar.

for i in range(0, N): # Loop over N many test cases.
	testLine1 = Ar[findTestCaseToRead] 			# Ar[1]
	testLine2 = Ar[(findTestCaseToRead + 1)] 	# Ar[2]
	compList = []								# Predefine list
		
	findCharToCompare = 0	# Set and reset starting character to read for every loop
		
	# Function to read, compare and build new line
	charsToRead = len(testLine1) - 1 
		
	for j in range(0, charsToRead): # Loof over characters in testLine
		if testLine1[findCharToCompare]==testLine2[findCharToCompare]: # Test if true that characters are equal.
			compList.append('.') #add "." for equal character.			
		
		else:
			compList.append('*') #add "*" for unequal character.
	
		findCharToCompare = findCharToCompare +1	# Step the char to find.

	findTestCaseToRead = findTestCaseToRead + 2		# Step the test case to find the next in the array Ar.
	compLine = ''.join(compList)	# Convert List to String.
	
	print(testLine1, end='')	#print line 1
	print(testLine2, end='')	#print line 2
	print(compLine)				#print comparison line
	print('') 					#print a blank line