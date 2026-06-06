# 208. Implement Trie (Prefix Tree)

class TrieNode:
    def __init__(self, val=None):
        self.val = val
        self.childs = {}
        self.is_end_of_word = False

    def __str__(self):
        return f"<{self.val}> {repr(self.childs)}"

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        def idx(w: str):
            return ord(w.lower()) - 97
        
        def insert(word: str, root: TrieNode):
            if not word:
                return
            
            w = word[0]
            if not w in root.childs:
                node = TrieNode(w)
                root.childs[w] = node
            root = root.childs[w]
            if len(word) == 1:
                root.is_end_of_word = True
            insert(word[1:], root)
        
        insert(word, self.root)
        

    def search(self, word: str) -> bool:
        node = self.root
        for w in word:
            if w in node.childs:
                node = node.childs[w]
            else:
                return False
        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for w in prefix:
            if w in node.childs:
                node = node.childs[w]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


# n = TrieNode()
# print(n.val, n)
t = Trie()
print(t.insert('apple'))
print(t.search('apple'))
print(t.insert('app'))
print(t.search('app'))
print(t.startsWith('app'))