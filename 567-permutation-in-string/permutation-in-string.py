class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        counter = {}
        matches = 0 

        #create the count for each character in substring
        for char in s1:
          counter[char] = 1 + counter.get(char, 0)
        
        for i in range(len(s2)):
          char = s2[i]
          
          #if char in counter, always decrement by 1
          if char in counter:
            counter[char] -= 1
            #if char's value = 0, we have a match
            #this if statement is the optimisation
            if counter[char] == 0:
              matches += 1
          
          #check the window
          if i >= window and s2[i-window] in counter:
            
            #if the current count is 0, remove a match since we are disturbing a match
            #this if statement is the optimisation
            if counter[s2[i-window]] == 0:
              matches -= 1

            #increment the character leaving our window
            counter[s2[i-window]] += 1
          
          if matches == len(counter):
            return True

        return False
            
        

            