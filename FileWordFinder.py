import os

os.system("curl https://raw.githubusercontent.com/ksu-is/FileWordFinder/main/Example -o Paragraphs.txt")

paragraphs = open('Paragraphs.txt', 'r')

paragraphs_contents = paragraphs.read()

words = ""
allwords = []

for i in paragraphs_contents:
    
    if i.isalpha():
        words = words + i
    elif i == " ":
        words = words.lower()
        allwords.append(words)
        words = ""



inp = input("Please enter a word to find: ")

while inp.isalpha() == False:
    inp = input("Please enter a word to find: ")

count2 = 0
found = False
count = 0


for i in allwords:
    if i.lower() == inp.lower():
        found = True
        count = count + 1
    if inp.lower() in i and i.lower() != inp.lower():
        count2 = count2 + 1
        found = True

if found == True:
    print(inp + " has been found\n" + str(count) + " instances of " + inp + "\n" + str(count2) + " Partial instances of " + inp + " found")


elif found == False:
    print(inp + " cannot be found")

