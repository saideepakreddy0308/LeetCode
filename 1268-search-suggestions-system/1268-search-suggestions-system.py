class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        products.sort()
        result = []
        
        for i in range(1, len(searchWord) + 1):
            prefix = searchWord[:i]
            suggestions = [product for product in products if product.startswith(prefix)]
            suggestions.sort()
            result.append(suggestions[:3])
            
        return result
    
    # T.C: O(len(searchword) * m * n)) , n producsts,m is avg length, their sorting.
    # S.C: O(len(searchWord) * k * m), k no.of suggestions, m its avf len.
    # code is not implementing binary search directly; instead, it relies on sorting the products and using list comprehension to find suggestions for each prefix