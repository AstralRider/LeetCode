class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        basket = {}
        maxFruits = 0

        l = 0 
        for r in range(len(fruits)):
            basket[fruits[r]] = basket.get(fruits[r], 0) + 1
  
            while len(basket) > 2:
                if basket[fruits[l]] <= 1:
                    del basket[fruits[l]]
                else:
                    basket[fruits[l]] -= 1
                l += 1

            maxFruits = max(maxFruits, (r - l) + 1)
            
        return maxFruits
            
        #Time: O(N)
        #Space O(1)









        
        