'''
To change the overall look of your document. To change the look available in the gallery.
'''
sentence=input("Enter a sentence:")
word_list=sentence.lower().replace('.','').split()
word_count={} #Initialize an empty dictionary.The key is the word and  value is the count
for word in word_list:
    word_count[word]=word_count.get(word,0)+1
# Print word occurrences
print("word occurrences: ",word_count)
# Print total number of words
total_words=sum(word_count.values())
print("Total number of words",total_words)