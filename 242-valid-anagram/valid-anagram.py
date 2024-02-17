class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hashT = {}
        hashS = {}
        
        if len(s) != len(t):
          return False
        
        for charS in s:
          if not hashS.get(charS):
            hashS[charS] = 1
          else:
            hashS[charS] += 1
        
        for charT in t:
          if not hashT.get(charT):
            hashT[charT] = 1
          else:
            hashT[charT] += 1
        
        for char in hashS:
          if not hashT.get(char):
            return False
          elif hashT.get(char) != hashS.get(char):
            return False
        return True
          

        
