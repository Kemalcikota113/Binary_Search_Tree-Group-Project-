import os
import Various_functions as cs
import HashSet as hset
import BstMap as bst

path_eng_100k = os.getcwd()
path_eng_100k += "/100K_sentences_output.txt"
path_monty = os.getcwd()
path_monty += "/Holy_grail_output.txt"

""" Part 1 """

# Count unique words using Pythons set and dictionary

"""Part 1.1 """
word_lst = cs.add_words_lst(path_eng_100k)
print("--" * 20)
print(f"Unique words in Eng_100k is: {cs.count_different_words(word_lst)}")
print("\n")

"""Part 1.2 """
word_lst = cs.del_4_letter_words(word_lst)
word_dict = cs.count_occurrences(word_lst)
print("\n")
cs.most_occuring_words(word_dict)
print("\n")

"""Part 2.1 """
word_lst = cs.add_words_lst(path_monty)
print(f"Unique words in Monty is: {cs.count_different_words(word_lst)}")
print("\n")

""" part 2.2 """
word_lst = cs.del_4_letter_words(word_lst)
word_dict = cs.count_occurrences(word_lst)
print("\n")
cs.most_occuring_words(word_dict)
print("\n")

""" Part 3 """

"""Part 3 Bst 1.1 """
# Add dictinary to BST
map = bst.BstMap()
words_eng_100k = cs.add_words_lst(path_eng_100k)
count_bst = cs.counted_map(map, words_eng_100k)
count_bst_lst = count_bst.as_list()

print("TOP LIST FROM BST")
count_bst_lst.sort(key=lambda y: y[1])
count_bst_lst.reverse()

print("Top 10 occuring words!")

for i in range(0, 10):
    counter = 1
    for k in count_bst_lst[i]:
        counter += 1
        if counter % 2 == 0:
            print("Word:", k, end=" ")
        else:
            print("Occures:", k, "times")

print("\n")
print("Map Size (ENG_100K): ", map.size(), "\n")
print("Max Depth (ENG_100K): ", map.max_depth(), "\n")

""" Part 3 Bst 1.2 """
# Add dictinary to BST
map = bst.BstMap()
words_monty = cs.add_words_lst(path_monty)
count_bst = cs.counted_map(map, words_monty)
count_bst_lst = count_bst.as_list()
count_bst_lst.sort(key=lambda y: y[1])
count_bst_lst.reverse()

print("Top 10 occuring words!")

for i in range(0, 10):
    counter = 1
    for k in count_bst_lst[i]:
        counter += 1
        if counter % 2 == 0:
            print("Word:", k, end=" ")
        else:
            print("Occures:", k, "times")

print("\n")
print("Map Size (Monty): ", map.size(), "\n")
print("Max Depth (Monty): ", map.max_depth(), "\n")

""" Part 3 Hash-set 2.1 """

words = hset.HashSet()
words.init()

# Adding words
for word in words_eng_100k:
    words.add(word)

mx = words.max_bucket_size()
size_words = words.get_size()
print("\n")
print("Max bucket size (ENG_100K): ", mx, "\n")
print("Word count (ENG_100K): ", size_words, "\n")

""" Part 3 Hash-set 2.2 """

words = hset.HashSet()
words.init()

# Adding words
for word in words_monty:
    words.add(word)

mx = words.max_bucket_size()
size_words = words.get_size()
print("Max bucket size (MONTY): ", mx, "\n")
print("Word count (MONTY): ", size_words, "\n")
print("--" * 20)
