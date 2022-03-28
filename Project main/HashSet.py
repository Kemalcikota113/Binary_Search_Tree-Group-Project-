from dataclasses import dataclass
from typing import List


@dataclass
class HashSet:
    buckets: List[List] = None
    size: int = 0

    def init(self):
        self.size = 0
        self.buckets = [[] for i in range(8)]

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

    # Doubles size of bucket list
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

    # Adds a word to set if not already added
    def add(self, word):
        if self.contains(word) is False:
            self.size += 1
            value = self.get_hash(word)
            bucket_number = value % self.bucket_list_size()
            self.buckets[bucket_number].append(word)

        if self.get_size() == self.bucket_list_size():
            self.rehash()
        return None

    # Returns a string representation of the set content
    def to_string(self):
        hash_string = "{ "
        for bucket in self.buckets:
            for word in bucket:
                hash_string += word
                hash_string += " "
        hash_string += "}"
        return hash_string

    # Returns current number of elements in set
    def get_size(self):
        return self.size

    # Returns True if word in set, otherwise False
    def contains(self, word):
        value = self.get_hash(word)
        bucket_number = value % self.bucket_list_size()
        if word in self.buckets[bucket_number]:
            return True
        else:
            return False

    # Returns current size of bucket list
    def bucket_list_size(self):
        return len(self.buckets)

    # Removes word from set if there, does nothing
    # if word not in set
    def remove(self, word):
        value = self.get_hash(word)
        bucket_number = value % self.bucket_list_size()
        if word in self.buckets[bucket_number]:
            self.buckets[bucket_number].remove(word)
            self.size -= 1
        return None

    # Returns the size of the bucket with most elements
    def max_bucket_size(self):
        max_elements = 0
        for bucket in self.buckets:
            if len(bucket) > max_elements:
                max_elements = len(bucket)

        return max_elements
