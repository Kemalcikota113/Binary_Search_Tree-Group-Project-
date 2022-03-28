
def count_different_words(lst_words):
    """ Function that counts number of different
    words by adding them to a set. Return number of unique words"""
    word_set = set()
    for word in lst_words:
        word_set.add(word)

    return len(word_set)


def add_words_lst(path):

    with open(path, "r") as file:
        clean_lst = []
        lst_words = file.read()  # Reads from path
        lst_words = lst_words.splitlines()  # Split lines, creats list

    for sentence in lst_words:  # iterate over words in sentence
        temp_sentence = sentence.split(" ")  # split into words
        clean_lst += temp_sentence

    return clean_lst


def del_4_letter_words(word_lst):
    new_lst = []
    for word in word_lst:
        if len(word) > 4:
            new_lst.append(word)

    return new_lst


def count_occurrences(word_lst):
    """ Function that counts words and adds to dictionary
    function return a dictionary w. count/words """
    word_count_dict = {}

    for word in word_lst:
        if word in word_count_dict:
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1
    return word_count_dict


def most_occuring_words(word_dict):
    """ Sorting values in dictionary.
    Return top 10 most occuring words, larger than 4"""

    word_dict = list(word_dict.items())
    word_dict = sorted(word_dict, key=lambda tpl: tpl[1])
    word_dict.reverse()

    print("Top 10 occuring words!")

    for i in range(0, 10):
        counter = 1
        for k in word_dict[i]:
            counter += 1
            if counter % 2 == 0:
                print("Word:", k, end=" ")
            else:
                print("Occures:", k, "times")

    return None


def counted_map(map, word_lst):
    """ Function that get words and puts them in BST
        for every duplicate value updates with += 1"""
    for w in word_lst:
        if len(w) > 4:
            n = map.get(w)

            if n is None:
                map.put(w, 1)
            else:
                map.put(w, n+1)

    return map
