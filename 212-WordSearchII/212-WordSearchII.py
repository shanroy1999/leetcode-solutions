# Implement a TrieNode (prefixTree) to check for prefixes of the words in the word list
class TrieNode:
    def __init__(self):
        self.children = {}          # Hashmap => key - character, value - child node of the character
        self.isEndofWord = False         # mark if the node is the end of the word
    
    # Add word to the Trie
    def addWord(self, word):
        # set our current node to the root node
        current = self
        # iterate through the word character by character and add the characters
        for char in word:
            # if character does not exist in the Trie node
            if char not in current.children:
                # Add the character as a child to the Trie node
                current.children[char] = TrieNode()
            # if the character already exists in the Trie node
            # point the current node to that character node
            current = current.children[char]
        # mark end of the word
        current.isEndofWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Create a root Trie Node from the TrieNode class
        root = TrieNode()
        # For every word in the input => add each word to the Trie
        for word in words:
            root.addWord(word)
        
        rows, cols = len(board), len(board[0])
        # res - set of words => might visit the same word twice in board => dont want duplicate
        # visit - dont want to repeat same character twice
        res, visit = set(), set()

        # Depth first search recursive
        # go through every position - pass row, col as coordinates
        # pass the currNode - to see what character we have already visited before
        # pass the word - to see what is the word so far (eg - "ac")
        # if node we are visiting happens to be the end of the word => add word to result
        def dfs(row, col, currNode, word):
            # Base case - out of bounds
            # (row, col) - has already been visited
            # character that we are at - character is not even in the trie at the current position of trie node
            if row<0 or col<0 or row>=rows or col>=cols or (row, col) in visit or board[row][col] not in currNode.children:
                return
            
            # Mark position as visited
            visit.add((row, col))

            # update currNode variable as we get to new character we visited on board
            currNode = currNode.children[board[row][col]]
            # update the word - add the character we visited
            word += board[row][col]
            # check if its the end of the word
            if currNode.isEndofWord:
                # Add the string word to the result
                res.add(word)

            dfs(row+1, col, currNode, word)     # Right
            dfs(row-1, col, currNode, word)     # Left
            dfs(row, col+1, currNode, word)     # Up
            dfs(row, col-1, currNode, word)     # Down

            # After we are done - mark it as unvisited - cant visit same twice
            visit.remove((row, col))
        
        # Go through every single starting position in the grid
        for row in range(rows):
            for col in range(cols):
                dfs(row, col, root, "")

        # Convert set of result to a list
        return list(res)
