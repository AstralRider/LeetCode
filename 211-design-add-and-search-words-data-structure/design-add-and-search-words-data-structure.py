class TrieNode():
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True
        
    def search(self, word: str) -> bool:
        

        def dfs(i, node):
            curr = node
         
            for j in range(i, len(word)):
                if word[j] == ".":
                    for n in curr.children.values():
                        if dfs(j + 1, n):
                            return True
                    return False
                else:
                    if word[j] not in curr.children:
                        return False
                    curr = curr.children[word[j]]

            return curr.word
        
        return dfs(0, self.root)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)