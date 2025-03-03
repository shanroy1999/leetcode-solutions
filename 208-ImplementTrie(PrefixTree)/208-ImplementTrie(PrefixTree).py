class TrieNode:
    def __init__(self):
        self.children = {}          # use hashmap => key -> character, value -> word
        self.isEndOfWord = False    # Check if the character is the end of the word

        # we do not store character in Trie Node
        # children["a"] = TrieNode()

class Trie:
    def __init__(self):
        self.root = TrieNode()      # set the root of Trie

    def insert(self, word: str) -> None:
        curr = self.root                        # set current node to the root node
        # Iterate through each character of the word
        for c in word:
            # If the character is not the child of the root
            if c not in curr.children:
                # Add the character node in the Trie as child
                curr.children[c] = TrieNode()
            # If the character already exists => set the current node to the character node
            curr = curr.children[c]
        # once iteration through all characters completed => set last character as endofword
        curr.isEndOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root                # set current node to the root node
        # Iterate through each character of the word
        for c in word:
            # If the character is not the child of the root => word is not there in the Trie
            if c not in curr.children:
                # return False since word is not there
                return False
            # If character node already exists => Set current to the character node
            curr = curr.children[c]
        # See if the last character is marked as endoftheword => if yes -> return True else False
        return curr.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        # Same as "search" except that the isEndOfWord will not be marked True
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)