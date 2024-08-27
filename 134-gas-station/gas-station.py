class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        tank = 0
        res = 0
        for i in range(len(gas)):
            tank += (gas[i] - cost[i])

            #if tank ever dips below 0 we cannot make the journey so reset 
            if tank < 0:
                tank = 0

                #we are guaranteed a solution so we can
                #set res to be the next idx
                res = i + 1
        
        return res
            

            

