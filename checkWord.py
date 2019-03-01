import enchant
import os

#init dictionary
d = enchant.Dict("en_US")
existWord = True

#function that start find possible word combinations recursively
def findCombo(letters, maxChar):
	return findComboHelper(letters.upper(), "", maxChar)
	#else: return findComboHelperExist(letters.upper(), "", maxChar)

#function to find all possible word combninations recursively
def findComboHelper(letters, str, maxChar):
    if (not letters) or (maxChar <= 0):
        if existWord:
            global d
            if (not d.check(str)):  return set()
        return {str}
    result = set()
    for i in range(len(letters)):
        result = result.union(findComboHelper(letters[0: i] + letters[i+1: len(letters)], str+letters[i], maxChar - 1))
    return sorted(result)

#function to find word combninations that exist only
"""def findComboHelperExist(letters, str, maxChar):
    if (not letters) or (maxChar <= 0):
    	global d
    	if (d.check(str)):
        	return {str}
    	else:
        	return set()
    result = set()
    for i in range(len(letters)):
        result = result.union(findComboHelperExist(letters[0: i] + letters[i+1: len(letters)], str+letters[i], maxChar - 1))
    return sorted(result)
    """

#ask for input
letters = input ("What are your letters? ")
maxLength = input ("What is the max length of the word? ")
existWord = input ("Do you want words that exist only?(y/n) ")

#change mode based on input
if "y" in str(existWord).lower():
	existWord = True
else:
	existWord = False

#print result
result = findCombo(str(letters), int(maxLength))
print ("Possible combinations: ", len(result))
for combo in result:
    #display result
    print (combo)
    #read out each result in terminal
    os.system ("say " + combo)