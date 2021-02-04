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
Graph = namedtuple()

