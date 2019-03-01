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

#ask for input
letters = input ("What are your possible letters? ")
maxLength = input ("What is the length of the word? ")
existWord = input ("Do you want words that exist only?(y/n) ")
containLetters = str(input ("sepecific Letters in the word? "))
#change mode based on input
if "y" in str(existWord).lower():
	existWord = True
elif "n" in str(existWord).lower():
	existWord = False
else:
    raise ValueError("Wrong input")

#print result
result = findCombo(str(letters), int(maxLength))

print ("Possible combinations: ", len(result))
for combo in result:
    check = True
    if containLetters:
        for char in containLetters:
            if char not in combo:
                check = False
                break
    if check:
        #display result
        print (combo)
        #read out each result in terminal
        os.system ("say " + combo)