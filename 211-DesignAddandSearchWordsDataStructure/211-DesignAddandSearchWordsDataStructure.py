class TrieNode:
    def __init__(self):
        # store the children as hashmap => key -> child node (character), value => TreeNode
        self.children = {}
        self.isEndOfWord = False            # Check if the character is the end of the word

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        # if character not already in the hashmap
        for c in word:
            if c not in curr.children:
                # Add the character to the hashmap
                curr.children[c] = TrieNode()
            # if character already present in hashmap => move the current node to the child node
            curr = curr.children[c]
        # Mark last character of the word as the endOfWord
        curr.isEndOfWord = True

    def search(self, word: str) -> bool:
        # Depth First Search
        # Recursive function
        # j -> starting index, root => current node
        # if found a path that matches => immediately return True
        # if not found a path => keep going down all the path until we find one
        # if no path found at the end => return False
        def dfs(j, root):
            curr = root
            # Start at j
            for i in range(j, len(word)):
                c = word[i]
                # there can be 26 different paths
                # Recursive portion
                if c == ".":
                    # Use backtracking, recursion
                    for child in curr.children.values():
                        # we are going down a child => increment i
                        if dfs(i+1, child):
                            return True
                    return False
                # iterative portion - no "."
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            # Return whether the word completed
            return curr.isEndOfWord
        # Call the DFS function
        # start at index 0 => j=0 at the root node of Trie
        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)