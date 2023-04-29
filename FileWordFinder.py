import os

os.system("curl https://raw.githubusercontent.com/ksu-is/FileWordFinder/main/Example -o Paragraphs.txt")

paragraphs = open('Paragraphs.txt', 'r')

paragraphs_contents = paragraphs.read()

print(paragraphs_contents)