# 1268. Search Suggestions System

import bisect

class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []

class Solution:
    def suggestedProducts_approach1(self, products: list[str], searchWord: str) -> list[list[str]]:
        products.sort()

        result = []
        for i in range(1, len(searchWord)+1):
            pre_fix = searchWord[:i]
            curr = []
            idx = bisect.bisect_left(products, pre_fix)
            for j in range(3):
                if idx + j < len(products):
                    if products[idx+j].startswith(pre_fix):
                        curr.append(products[idx+j])
            result.append(curr)
        return result

    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        products.sort()

        root = TrieNode()

        # Build Trie
        for product in products:
            node = root

            for ch in product:
                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

                if len(node.suggestions) < 3:
                    node.suggestions.append(product)

        # Search prefixes
        result = []
        node = root

        for ch in searchWord:
            if node and ch in node.children:
                node = node.children[ch]
                result.append(node.suggestions)
            else:
                node = None
                result.append([])

        return result



inputs = [
    (["mobile","mouse","moneypot","monitor","mousepad"], "mouse", [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]),
    (["havana"], "havana", [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]),
]
s = Solution()
for products, searchWord, result in inputs:
    my_result = s.suggestedProducts(products, searchWord)
    print(my_result, my_result==result)