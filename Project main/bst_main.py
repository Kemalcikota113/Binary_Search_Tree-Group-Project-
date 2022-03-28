# from dataclasses import dataclass
import BstMap as bst
import count_words as cs
import os

#path = os.getcwd()
#path += "/100K_sentences_output.txt"
#path += "/Holy_grail_output.txt"
# Program starts
# Add pairs
d = {"Ella": 39, "Owen": 40, "Fred": 44, "Zoe": 41, "Adam": 27, "Ceve": 37}
#d = cs.count_occurrences(cs.del_4_letter_words(cs.add_words_lst(path)))
map = bst.BstMap()
for k, v in d.items():
    map.put(k, v)
print(map.to_string())        # { (Adam,27) (Ceve,37) (Ella,39) (Fred,44) (Owen,40) (Zoe,41) }
print("Size:", map.size())    # 6

# Override existing values
print("\nOverride existing values")
#map.put("Zoe", 99)
#map.put("Ceve", 100)
print(map.to_string())       # { (Adam,27) (Ceve,100) (Ella,39) (Fred,44) (Owen,40) (Zoe,99) }

# get
print("\nGet(Fred):", map.get("Fred"))    # 44
print("Get(Jonas):", map.get("Jonas"))  # None
print("Max depth:", map.max_depth())     # 3

"""
# Check max_depth
map.put("AA", 1)
map.put("AAA", 2)
map.put("AAAA", 3)
map.put("AAAAA", 4) """

print("\nSize:", map.size())              # 10
print("Max depth:", map.max_depth())    # 6
#print("To_string: ", map.to_string())    # { (AA,1) (AAA,2) (AAAA,3) (AAAAA,4) (Adam,27) (Ceve,100) (Ella,39) (Fred,44) (Owen,40) (Zoe,99) }

# as_list
lst = map.as_list()
print("\nList size and element type:", len(lst), type(lst[0]))  # 10 <class 'tuple'>
#print("List content:", lst)  # [('AA', 1), ('AAA', 2), ('AAAA', 3), ('AAAAA', 4), ('Adam', 27), ('Ceve', 100), ('Ella', 39), ('Fred', 44), ('Owen', 40), ('Zoe', 99)]



def most_occuring_words(lst):
    """ Sorting values in dictionary.
    Return top 10 most occuring words, larger than 4"""

    word_count = sorted(lst, key=lambda tpl: tpl[1])
    word_count.reverse()

    print("Top 10 occuring words!")

    for i in range(0, 10):
        counter = 1
        for k in word_count[i]:
            counter += 1
            if counter % 2 == 0:
                print("Word:", k, end=" ")
            else:
                print("Word:", k, "times")

    return None
