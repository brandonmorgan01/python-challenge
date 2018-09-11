#import dependencies
import os
import re

#creatpath
text_path = os.path.join('..', 'resources', 'pyparagraph.txt')

#open and read textfile
textreader = open(text_path, 'r')
lines = textreader.readlines()

# assign empty list for wordcount
word_count = []
letter_count = []

#break paragraph into sentences by end punctuation 
sentence_count = len(re.split("(?<=[.!?]) +", str(lines)))

#loop through lines
for line in lines:

    #split lines by spaces to break into words
    words = line.split()

    #loop through words
    for word in words:

        #remove punctuation
         word = word.strip(".,!?:;'\"")

         for letter in word:
            letter_count.append(letter)

         #lowercase 
         word = word.lower()
         
         #avoid duplicates (way easier than set conversion)
         if word not in word_count:

             #add to word count list
             word_count.append(word)

print('Paragraph Analysis \n-----------------')

print(f'Approximate Word Count: {len(word_count)}')
print(f'Approximate Sentence Count: {sentence_count}')
print(f'Average Letter Count: {round((len(letter_count)/len(word_count)), 1)}')
print(f'Average Sentence Length: {round((len(word_count) / sentence_count), 1)}')

#make path for writing 
output_path = os.path.join('..', 'Resources', 'pyparagraph_output.txt')

#open text file and write
with open (output_path, 'w') as txtfile:
    txtfile.writelines(f'Paragraph Analysis \n----------------- \n')
    txtfile.writelines(f'Approximate Word Count: {len(word_count)} \n')
    txtfile.writelines(f'Approximate Sentence Count: {sentence_count} \n')
    txtfile.writelines(f'Average Letter Count: {round((len(letter_count)/len(word_count)), 1)} \n')
    txtfile.writelines(f'Average Sentence Length: {round((len(word_count) / sentence_count), 1)} \n')
    
   

