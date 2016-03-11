#	Mark Wency P. Yambao, AB-7L
#	References:
#	http://www.tutorialspoint.com/python/python_functions.htm
#	http://www.pythonforbeginners.com/


#Define Functions

def getHammingDistance(str1, str2):
	dist = 0

	if type(str1) != str or type(str2) != str:	#if not strings
		return "Error! Inputs are not strings!"
	if len(str1) != len(str2):	#if not of the same length
		return "Error! Strings are not equal!"
	for i in range (0, len(str1)):	#sets the range from 0 to length of st1
		if str1[i] != str2[i]:	#checks every character in each string. if not equal, increment dist
			dist += 1
	return dist


def countSubstrPattern(original, pattern):
	check = 1
	counter = 0

	if type(original) != str or type(pattern) != str:	#inputs are not string, return error
		return "Error! Inputs are not strings!"
	for i in range (0, len(original)-len(pattern)+1):	#sets range of i from 0 to length of original - (length of pattern -1)
		for j in range (0, len(pattern)):	#sets range of j from 0 to length of pattern
			if original[i+j] != pattern[j]:	#checks if the char in current original is not equal to current pattern
				check = 0	#if not equal, set check to 0
		if check == 1:	#if not equal isn't encountered, increment counter
			counter += 1
		check = 1	#update check for next loop
	return counter


def isValidStrings(str1, alphabet):
	if type(str1) != str or type(alphabet) != str:	#inputs are not string, return error
		return "Error! Inputs are not strings!"
	for i in range (0, len(str1)):	#sets range of i to be 0 to length of string1
		if str1[i] not in alphabet:	#if current char of str1 is not in alphabet, return false
			return False
	return True	#else, return true


def getSkew(str1, n):
	numG = 0
	numC = 0
	x = 0

	if type(str1) != str or type(n) != int or isValidStrings(str1, "GCUTA") == False:	#checks if str1 is a string, n is int, and str1 is in ACGTU. if not, return error
		return "Error! Inputs are invalid!"
	if n > len(str1) or n < 1:	#if n is less than 1, or greater than length of str1, print error
		return "Error, n is invalid!"
	else:
		for i in range (0, n):	#set range of i to be 0 to n
			if str1[i] == "G":	#if g is encountered, increment numG and update x
				numG = numG + 1
				x = numG - numC
			if str1[i] == "C":	#if c is encountered, increment numc and update x
				numC = numC + 1
				x = numG - numC
		return x


def getMaxSkewN(str1, n):
	maxFound = "NotFound"
	maxHolder = 0;
	holder = 0;

	if type(str1) != str or type(n) != int or isValidStrings(str1, "GCUTA") == False:	#checks if str1 is a string, n is int, and str1 is in ACGTU. if not, return error
		return "Error! Inputs are invalid!"
	if n > len(str1) or n < 1:	#if n is less than 1, or greater than length of str1, print error
		return "Error, n is invalid!"
	for i in range(1, n+1):	#set range of i from 1 to n+1
		holder = getSkew(str1, i)	#calls getskew, then save the return value to holder
		if maxFound is "NotFound":	#if max is not found, save holder to max
			maxFound = "Found"			
			maxHolder = holder
		if maxHolder < holder:	#if holder is larger tham maxHolder, save holder to maxHolder
			maxHolder = holder
	return maxHolder


def getMinSkewN(str1, n):
	minFound = "NotFound"
	minHolder = 0;
	holder = 0;

	if type(str1) != str or type(n) != int or isValidStrings(str1, "GCUTA") == False:	#checks if str1 is a string, n is int, and str1 is in ACGTU. if not, return error
		return "Error! Inputs are invalid!"
	if n > len(str1) or n < 1:	#if n is less than 1, or greater than length of str1, print error
		return "Error, n is invalid!"
	for i in range(1, n+1):	#set range of i from 1 to n+1
		holder = getSkew(str1, i)	#calls getskew, then save the return value to holder
		if minFound is "NotFound":	#if min is not found, save holder to min
			minFound = "Found"			
			minHolder = holder
		if minHolder > holder:	#if holder is less than tham minHolder, save holder to minHolder
			minHolder = holder
	return minHolder
