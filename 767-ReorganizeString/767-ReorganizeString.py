class Solution:
    def reorganizeString(self, s: str) -> str:
        # Count each character and create a hashmap using Counter
        count = Counter(s)
        # Use a MaxHeap to get max frequency of char
        # Put count first => heapify sorts based on first val by default
        maxHeap = [[-count, char] for char, count in count.items()]

        # convert list to heap - O(N)
        heapq.heapify(maxHeap)

        # Keep track of the previous character used - dont reuse it
        prev = None
        res = ""
        while maxHeap or prev:
            # if maxHeap is empty but we have a value in prev => cannot create a valid string
            if prev and not maxHeap:
                return ""
            # Get most frequent character
            count, char = heapq.heappop(maxHeap)
            # Append the character to result
            res += char
            # Decrement the count since we used the char - count is negative so add 1
            count += 1
            # If previous value is already set to some value => push it back to the heap
            if prev:
                heapq.heappush(maxHeap, prev)
                # Once pushed back to maxHeap => set prev back to None
                prev = None
            # If the char has been used just now => dont want to reuse the same char
            # Set that character to prev only when count is not zero
            if count!=0:
                prev = [count, char]
        return res

        # Time Complexity = O(NlogN)
