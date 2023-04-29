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
        allwords.append(words)
        words = ""


inp = input("Please enter a word to find: ")



