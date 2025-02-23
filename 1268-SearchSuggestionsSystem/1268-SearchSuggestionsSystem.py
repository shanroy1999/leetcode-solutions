class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Brute Force Approach
        products.sort()
        result = []
        for i in range(1, len(searchWord)+1):
            prefix = searchWord[:i]
            suggestions = [product for product in products if product.startswith(prefix)]
            result.append(suggestions[:3])
        return result

        # Time complexity = O(M X N) => M = length of searchword, N = length of products
        # Space complexity = O(1)

        # Optimized Approach
        products.sort()
        result = []
        start, end = 0, n-1
        for i, c in enumerate(searchWord):
            while start <= end and (i >= len(products[start]) or products[start][i] < c):
                start+=1
            while start <= end and (i >= len(products[start]) or products[start][i] > c):
                end-=1
            
            if start <= end:
                result.append(products[start:min(start+3, end+1)])
            else:
                end.append([])
        return result





