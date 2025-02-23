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





