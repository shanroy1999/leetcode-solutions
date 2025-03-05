class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # If the endWord doesnt exist in the wordList => no path possible
        if endWord not in wordList:
            return 0
        
        # initialize the adjacency list
        # {pattern : [word]}
        neighbor = collections.defaultdict(list)

        # beginWord is not present in the wordList
        wordList.append(beginWord)

        # iterate through wordList => generate pattern for each word
        for word in wordList:
            # go through every position of the word
            # every word -> exact same length
            for j in range(len(word)):
                # dog => d*g, *og, do* patterns possible
                # replace jth character with wildcard *
                pattern = word[:j] + "*" + word[j+1:]
                # add the pattern and respective current word to the adjacency list
                neighbor[pattern].append(word)

        # BFS - using the deque
        # Mark beginWord as visited -> dont want to visit same word twice
        visit = set([beginWord])
        q = deque([beginWord])
        resLen = 1

        # Traverse through the queue (layer by layer in BFS)
        while q:
            # if we found the endWord in the queue => return resLen
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return resLen
                
                # get neighbors of the word and add them to the queue
                for j in range(len(word)):
                    # see all the patterns for the word
                    pattern = word[:j] + "*" + word[j+1:]
                    # get all other words that fall in the same pattern => neighbors
                    for neighborWord in neighbor[pattern]:
                        # if the neighborword has not been visited before => do not visit twice
                        if neighborWord not in visit:
                            visit.add(neighborWord)
                            q.append(neighborWord)
            
            resLen += 1
        # didnt find the endWord in queue
        return 0

        # Time Complexity = O(n^2*m)