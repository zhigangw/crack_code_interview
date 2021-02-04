'''
Write a function that returns a possible alphabet given a sorted list of strings
Input: ["ct", "bt", "tb"]
Output: ['c', 'b', 't']

Input: ["cc", "cb", "bb", "ac"]
Output: ['c', 'b', 'a']

Counter example: assigning each character a rank
input: ["cb", "cg", "db", "dx", "dg", "bg"]
output: ['c', 'd', 'b', 'x', 'g']

Counter example: travers list of words by charactoer index ordex
iterat over the list of strings by charactoer(starting with the first character) and output characters in order, skipping over characters that have already been seen.
This fails because it does not take into account if the ordering when first-seen (here x-y) is correct. The relationship may in fac be inverse and 
information gather on in the list of strings will provide this. Fundamentally, we need to extract information about the relationship 
between characters first before putputing characters in order

input: ["axc", "byc", "ccy", "ccx"]
output: ['a', 'b', 'c', 'y', 'x']

The list of strings is completely sorted and will not contain errornous input
Inputs will always have enough information to extract an alphabet. (all letters will have a priority)
The function need only return a valid alphabet. There may be multiple valid plhabets but we only need to return one of them
All words have the same lenght and the list will not contain any duplicates. (these restraints may be removed if desirable)

Solution: Topological sort of a priority graph
1. Contstruct a priority graph by finding the first character difference bewtween strings pairwise
2. Topologically sort the priority graph (using Kahn's algorithm -- wikipedia)

Follow up: remove the constraint that words are all of the same length that the list may not contain any duplicate
'''

from collections import namedtuple
from typing import Dict, List

Graph = namedtuple('Graph', ['priority_graph', 'in_degree'])

def init_graph(words:List[str]) -> Graph:
    priority_graph: Dict[str, List[str]] = {}
    in_degree: Dict[str,int] = {}

    for word in words:
        for char in word:
            if char not in priority_graph:
                priority_graph[char] = []
                in_degree[char] = 0
    return Graph(priority_graph=priority_graph, in_degree=in_degree)

def fill_graph(words:List[str], graph: Graph) -> None:
    for i in range(len(words) -1):
        word_a = words[i]
        word_b = words[i+1]

        for j in range(len(word_a)):
            char_a = word_a[j]
            char_b = word_b[j]

            if char_a != char_b:
                graph.priority_graph[char_a].append(char_b)
                graph.in_degree[char_b] += 1
                break


def topological_sort(graph:Graph) ->List[str]:
    priority_graph = graph.priority_graph
    in_degree = graph.in_degree
    fringe:List[str] = [char for char in in_degree if in_degree[char] == 0]
    output: List[str] = []

    while fringe:
        char = fringe.pop()
        output.append(char)

        for other_char in priority_graph.get(char, []):
            in_degree[other_char] -= 1
            if in_degree[other_char] == 0:
                fringe.append(other_char)
    return output

def extract_alphabet(words:List[str]) -> List[str]:
    graph: Graph = init_graph(words)
    fill_graph(words, graph)
    return topological_sort(graph)

TEST_CASE = [
    {
        'input': ["ct", "bt", "tb"],
        'output': ['c', 'b', 't']
    },
    {
        'input': ["cc", "cb", "bb", "ac"],
        'output': ['c', 'b', 'a']
    },
    {
        'input': ["cb", "cg", "db", "dx", "dg", "bg"],
        'output': ['c', 'd', 'b', 'x', 'g']
    },
    {
        'input': ["axc", "byc", "ccy", "ccx"],
        'output': ['y', 'x', 'a', 'b', 'c']
    }
]
for test in TEST_CASE:
    input = test['input']
    expected = test['output']
    real = extract_alphabet(input)
    print('input:' ,input, "expected:", expected,  "real:", real, "SUCCEEDED" if expected == real else "FAILED")


