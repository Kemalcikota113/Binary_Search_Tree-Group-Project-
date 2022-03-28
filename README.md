# Mini-project report 
Members: Kemal Cikota, Theo Davnert, Michael Daun   
Program: Software Technology    
Course: 1DT901  
Date of submission: 2021-11-02 

## Introduction  
This project is a final remark for the course "Introduction to programming" where we; Michael, Kemal and Theo have got together to get a deeper understanding about data structures, specifically Binary search trees (BST) and hashing. We will be using the output of a solution from a previous assignment as a reference for this project. The output contained the number of words in two text files, we will call them "100K" and "Holy_Grail". The purpose of this project is to prepare us for greater tasks and to increase our general knowledge about coding as a whole. We decided to aim for a G grade and has solved three of the following G parts accordingly.

- Count unique words using Python's set and dictionary
- Implement two data structures suitable for working with words as data: a) A hash based set, and b) a binary search tree (BST) based map (dictionary). 
- Use your two data structures to repeat Part 1 (counting unique words)

## Part 1: Count unique words 1

The first part of the project was to use python's set and dictionary to count the amount of unique words in our output files (100K and Holy_Grail). We chose to use Kemal Cikotas output file because that was the closest one to the +-5% margin that we had to keep to pass the assignment prior to the project.

the total number of words were :

Holy_Grail - 10693 words

100K - 1881096 words

### *Quick run through the program:*
- We start by inputting our output files from the assignment by pathing.
- We have a "add_words_lst" function that reads the chosen output file and reformats it to a list making it easier to deal with later on.
- We have a function that runs through this list, removing all words that have 4 characters or less.
- We have a function "count_occourences" function that counts every single word in the list and adds it to a dictionary. Essentially, we iterate through the whole list that we created with a simple if/else statement. *if* we find a new word we give it a value "1" and *if* we find that word again and we increase that value by "+1".
- Now we want a top-10 list of the most occurring words in the list.
- we use the sorted function in our dictionary to sort the words with the largest value first. We then iterate over the list one last time with a "count" variable to count up and create a top-10 list of the most occurring words from our chosen input(being the output from 100K and Holy_Grail).

### *Unique words per file*
- Holy_Grail - 1869 unique words
- 100K - 83307 unique words
### *Top-10 most occouring words per file*
- Holy_Grail
    1. Arthur - 256 times
    2. launcelot - 101 times
    3. knight - 82 times
    4. galahad - 80 times
    5. father - 74 times
    6. bedevere - 68 times
    7. knights - 65 times
    8. guard - 58 times
    9. robin - 58 times
    10. right - 57 times
- 100K
    1. their - 6112 times
    2. about - 4569 times
    3. would - 3861 times
    4. people - 3627 times
    5. there - 3597 times
    6. which - 3524 times
    7. after - 2956 times
    8. first - 2854 times
    9. years - 2718 times
    10. other - 2713 times

## Part 2: Implementing data structures
The second part of the project was to implement our own data structures with two techniques; Binary Search Tree (BST) and HashMap. We had a set of rules and limitations that we had to follow to get a passing grade in this part of the project. 
- The limitations were: 
    * The **BST** had to be a linked implementation where each node had four fields: Key, value, left-child, right-child.
    * The **HashMap** had to contain buckets where each bucket is a python-list. The initial bucket size had to be eight and that number would double when the number of elements equals the number of buckets.
    * We were provided code skeletons that we would use as reference for how our code would look and work like. We were also provided a demo output showing us how the finished result would look like if the code was done correctly. We were not allowed to make any changes of the method signatures however we were free to add more functions and methods if needed. 
<p>

### Hash-set run-through
<p>

The main parts of our Hash-set, `Rehash`, `Get_hash` and `Add` will here be briefly explained.

* The `Rehash` function is used when the number of elements in our bucket list is equal to the number of total buckets. When our Rehash function is called it will first copy our current bucket list, double the number of current buckets and re-add the old words with new updated Hash-values.

```python
def rehash(self):
        old_hash_set = []
        for bucket in self.buckets:
            old_hash_set.append(bucket)
        new_buckets = self.bucket_list_size() * 2
        self.buckets = [[] for i in range(new_buckets)]
        for bucket in old_hash_set:
            for word in bucket:
                bucket_number = self.get_hash(word) % new_buckets
                self.buckets[bucket_number].append(word)
        return None
```
*  The `get_hash` function outputs a specific value for every word that gets put into the function. Our Hash-value is calculated by adding up every Ascii-value in our word, letter by letter and multiplying every letter with a specific number. 

    ```python 
    # Computes hash value for a word (a string)
    def get_hash(self, word):
        key = word
        value = 0
        i = 0
        for letter in key:
            i += 1
            value += ord(letter)
            value += value * (len(key) - i)
        return value
    ```

The Hash-set's `Add` main function as its title might imply is that it "adds" words to our Hash-set. The add function uses the following steps.

1. Check if a given word already is added. If the word is new to the Hash-set it will update its size by + 1.

2. If the word is new it will call upon `Get_hash` and find a bucket for the word by using modulus Hash-value with the number of buckets.

3. Lastly the add function will compare the number of elements in our buckets with how many buckets we have. If the number of elements is equal to the number of buckets it will call upon our `Rehash` to update the number of buckets.

Lastly, a short comment on our deviation when using `To_string` compared to our teacher's desired output that was showcased in the demo-program. Most likely the difference occurs because we have a different algorithm for calculating our Hash-value.

### BST run-through
<p>

The `put` function as the name says puts values and keys in nodes. It is quite easy to understand just by reading it. We iterate over our tree with if-statements and check what our key is. If the key we want to input is the same as the key we are on then we just get a new value. If our key is smaller than the one we are on then we put it on the current node's left side since we move down-left for each smaller key. If the key is larger than the previous then we move to the right since we move down-right every time we get a larger key than the previous.
```python
def put(self, key, value):
        if key == self.key:
            self.value = value
        if key < self.key:
            if self.left:
                self.left.put(key, value)
            else:
                self.left = Node(key, value, None, None)
        elif key > self.key:
            if self.right:
                self.right.put(key, value)
            else:
                self.right = Node(key, value, None, None)
```
<p>

The `max_depth` function is a bit more complex than the put function as we aren't moving through the tree like before.  
We set two local variables; left and right to zero.
We now iterate over the whole tree again but now everytime we see that the right side is larger than the left we return the a +1 to one of the variables. Because the function is recursive we will just keep returning values until the tree is done.
```python
 def max_depth(self):
        left = 0
        right = 0
        if self.left:
            left = self.left.max_depth()
        if self.right:
            right = self.right.max_depth()
        if right > left:
            return right + 1
        else:
            return left + 1
```

## Part 3: Count unique words 2
We have a function that we call "counted-map" that gets words from a list from the word-files. The function will not count in the words that have less than four characters. The function receives a word from the list and checks if it already exists and if it does exist then we update it's value by +1. if it does not already exist then it's given a value of just 1. 

The updated list that we got from "counted-map" is run through our "count" and "as_list" function where we get a list of tuples that gets listed in a top-10 most occurring order. The list has no deviation from the set-class top-10 list so we will refer you to section *Top-10 most occurring words per file* on line 86.

- The max bucket size per file was: 
    * Holy_Grail - 7
    * 100K - 30
- Max depth per file was:
    * Holy-Grail - 22
    * 100K - 41

## Project conclusions and lessons learned
We separate technical issues from project related issues.

### Technical issues 
We did face a couple of technical difficulties during the project. The most time consuming task that we had to do was the BST. It took a lot of time because of the logic that we had to apply before starting to code. We tried applying a kind of logic that would not work when put in a coding-context. It also took a lot of time to learn new things that were not a part of the lectures. We had roughly two weeks to complete the project where the BST took roughly 75% of that time.

We learned a lot of new stuff about programming as a whole but not alot in terms of scheduling and dividing the problems into different pieces because we already had a solid approach when it came to that. We think that we could have solved more tasks and also gotten a higher grade if we had more time on our hands.

### Project issues
We faced very little issues when looking at it from an internal group-chemistry perspective. We got together and started communicating as soon as we got the list of team members and started going to work as soon as the tasks were released to us. Our communication was very consistent both on-call and when it came down to meeting and interacting professionally. We set up a group-chat for us to communicate simultaneously through a platform called discord and we did so every day, we set up times to meet as a group on campus every day as well and spent about 3-4 hours every day on the project getting an average of 26 hours per week. We don't believe that there were any problems within our group itself, however the project was very hard for us and it was time consuming. We learnt a lot of things by just coding and communicating which we will definitely bring with us for future projects.

- Kemal Cikota's statement
    * The group used my output files from assignment 3 because that was the closest one to the +-5% margin i have later in part 2 together with Theo written the BST map, we split the work roughly 50/50. I think that a big contributor to us completing the project was our dedication to sit for long hours to learn a lot of new things under a short amount of time as we did not have any major background experience with Python or programming generally. Another key factor was our stable communication, everyone was equally as invested in meeting and doing work to collectively complete this project. We faced many technical issues and made many mistakes, especially in Part 2 which by far was the hardest part of the project but I believe that our determination created a sphere of motivation which made us complete it.
<p>

- Michael Daun's statement
    * Since day one have made efforts to keep our workload evenly dispersed among our team we haven't really found ourselves in a position where we soley worked with a part of the project. However there are parts in the assignment where some of us have had more responsibility than others. I have mainly been responsible for writing code, designing our Hash-set, designing and coding our main_program and in some sense coordinating our git repository.

    * I have spent roughly 5-6 hours daily every day of the week on the project. During nights I have been finding myself lucidly coding parts of the project in my mind. Funnily enough, how we compute our Hash-set came to me in a dream.

    * In hindsight I wish I would have been more invested in our BST-map in an earlier phase. Since we encountered more hardships in coding that part of the assignment.
- Theo Davnert's statement
    * In the beginning of the project Kemal and I worked mostly on the binary search tree whereas Michael worked mostly on the hash-set. That could hypothetically be a factor to why we encountered a lot of problems in our code. None of the members in our group had prior experience of coding so one extra mind could have made a difference. Later on in the project I think we realized that because then we attacked each problem more as a team. I was mainly responsible for the put and to_string method in the bstMap, Kemal was mostly responsible for the rest of the methods in the bst and most of the report. What we all did though was discussing each problem with each other to find the best solution for the problem. The estimated time that was spent on the project is around 25 hours per week. The lesson I've learned is that good communication between the team members in combination with frequent follow ups and help from the helpdesks is a key-concept for success. Our communication was very good but we could have used the python helpdesk a lot more in the beginning to make sure that we were on the right track.
<p>
