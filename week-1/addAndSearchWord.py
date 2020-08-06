from collections import defaultdict

class WordDictionary:

    def __init__(self):
        Trie = lambda : defaultdict(Trie)
        self.root = Trie()

    def addWord(self, word: str) -> None:
        currNode = self.root
        for letter in word:
            currNode = currNode[letter]
        currNode['end'] = True

    def search(self, word: str) -> bool:
        
        def findWordInTrie(word, i, currNode):
            if i == len(word):
                return 'end' in currNode
            elif word[i] == '.':
                return any(
                    findWordInTrie(word, i+1, currNode[letter])
                    for letter in currNode 
                    if letter != 'end'
                            )
            elif word[i] in currNode:
                return findWordInTrie(word, i+1, currNode[word[i]])
            else:
                return False
        
        return findWordInTrie(word, 0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)