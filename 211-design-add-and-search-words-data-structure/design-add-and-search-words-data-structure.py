class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.word = True

    def search(self, word: str) -> bool:

        def backtrack(i, curr):
            # if i >= len(word):
            #     return curr.word
            
            for j in range(i, len(word)):
                if word[j] == ".":
                    for curr in curr.children.values():
                        if backtrack(j + 1, curr):
                            return True
                    return False
                else:
                    if word[j] not in curr.children:
                        return False
                    curr = curr.children[word[j]]
            return curr.word
        return backtrack(0, self.root)
            
#bad mad dad 
# .ad







# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)