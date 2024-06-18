def printBiggest(First):

    for f in range(5):

        if len(First) > 0:

            biggest = max(First, key=First.get)

            print(f"{biggest}: {First[biggest]}", end =" ")

           

            del First[biggest]

 

def findXletter(words, i):

    for word in words:

        letter = word[i]

        #print(word[i])

        if letter in First:

            First[letter] += 1

        else:

            First[letter] = 1

 
# Dictionary for letters, gets reused.
First = {}

try:
    with open("Words.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("Error: The file 'Words.txt' was not found.")
    exit(1)

#Split it into words
words = content.split()
numWords = len(words)
print(f"Number of words: {numWords}")

 #printing the 5 most common letters per spot
for i in range(5):
    print("Slot ",i+1,":")
    findXletter(words, i)
    printBiggest(First)
    print("")
    First.clear()

 