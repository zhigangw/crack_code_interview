'''
Write a function that returns a list of strings is sorted given a specific alphabet
A list of N words and the K-sized alphabet are given.
input: words = ["cat", "bat", "tab"]
       alphabet = ['c', 'b', 'a', 't']
Note that we want to determine if the *list* of words is sorted, not the individual words
input: words = ["alice", "eve", "bob"]
       alphabet= ['a', 'b', ..., 'z']
output: False

input: words = ["alice", "bob", "eve"]
       alphabet = ['a', 'b', ..., 'z']
output: True

We want to determine if the list of strings is sorted in an ascending lexicographic ordering. 
So, the words should be sorted in order character by character. However for workds that are 
prefixes of the words, the shorter words should come first
input: words = ["cca", "cc", "cba"]
       alphabet = ['c', 'b', 't']
output: False

input: workds = ["cc", "cca", "cba"]
       alphabet = ['c', 'b', 'a', 't']
output: False

The alphabet parameter is provided ordered. Hence for ['c', 'b', 'a', 't']
The strings in words may not all be of the same length
Assume alphabet is a resonable input (alphabet will always contian all characters present in words. 
It is of a reasonable size(can be held in memory easily), etc)
'''
from typing import List, Tuple
def verify_ordering_a(words:List[str], alphabet:List[str]) -> bool:
    if(words is None or len(words) <= 1):
        return True
    if alphabet is None or len(alphabet) == 0:
        return True
    
    for i in range(len(words) - 1):
        word = words[i]
        next = words[i + 1]
        if not is_sorted_a(word, next, alphabet):
            return False
    return True

def is_sorted_a(word_a:str, word_b:str, alphabet:List[str]):
    for i in range(len(word_a)):
        if(i >= len(word_b)):
            return False
        elif word_a[i] != word_b[i]:
            return alphabet.index(word_a[i]) <= alphabet.index(word_b[i])
    
    print(word_a, word_b, True)
    return True


def verify_ordering_b(words:List[str], alphabet:List[str]) -> bool:
    if(words is None or len(words) <= 1):
        return True
    if alphabet is None or len(alphabet) == 0:
        return True

    alphabet_map:Dict[str, int] = {}
    for index, char in enumerate(alphabet):
        alphabet_map[char] = index
    
    for i in range(len(words) - 1):
        word_a = words[i]
        word_b = words[i + 1]
        for j in range(len(word_a)):
            if(j >= len(word_b)):
                return False
            elif word_a[j] != word_b[j]:
                return alphabet_map[word_a[j]] <= alphabet_map[word_b[j]]
    return True

def verify_ordering_s(words:List[str], alphabet:List[str]) -> bool:
    if not words: return True

    order = {ch: i for i, ch in enumerate(alphabet)}
    print(order)
    assert len(order) == len(alphabet)
    
    def _word_to_tuple(word:str) -> Tuple[int, ...]:
        return tuple(order[ch] for ch in word)

    tuples_gen = [_word_to_tuple(word) for word in words]
    print(tuples_gen)

    return sorted(tuples_gen) == tuples_gen

TEST_CASES = [(
    ["cc", "cca", "cba"],
    ['c', 'b', 'a', 't'],
    True
),(
    ["cca", "cc", "cba"],
    ['c', 'b', 'a', 't'],
    False
),(
    ["cca", "cc", "cba"],
    ['a', 'b', 'c'],
    False,
),(
    ["alice", "bob", "eve"],
    ['a', 'b',  'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],
    True,
)
]

for words, alphabet, expected_result in TEST_CASES:
    if verify_ordering_a(words, alphabet) != expected_result :
        print("FAILED:a", words, alphabet, expected_result, sep='\n')    
    if verify_ordering_b(words, alphabet) != expected_result :
        print("FAILED:b", words, alphabet, expected_result, sep='\n')    
    if verify_ordering_s(words, alphabet) != expected_result :
        print("FAILED:s", words, alphabet, expected_result, sep='\n')