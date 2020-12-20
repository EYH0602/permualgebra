import sys
from copy import copy
from .cycle import Cycle

class Permutation:
    def __init__(self, cycles = []):
        """
        Inputs: cycles
            ["1 2 3", "4 5 6", "8 9 10"]
            -> (1 2 3)(4 5 6)(8 9 10)
        """
        self.cycles = []
        self.setmax = 0     # if this is 6, it indicates that the preimage and image are {1,2,3,4,5,6}
        for cycleStr in cycles:
            newCycle = Cycle(cycleStr)
            self.cycles.append(newCycle)
            currMax = newCycle.getHighest()
            if currMax > self.setmax:
                self.setmax = currMax

    def getSimplify(self):
        S = self.getSet()   # set of preimage, i.e. domain; work as a queue
        res = Permutation()           # format: [1, 2, 3, "B", 8, 6] -> (1 2 3)(8 6)
        while S:    # while S is not empty    
            currElement = S.pop(0)  # front of queue
            currRes = [currElement]
            while True:
                for cycle in reversed(self.cycles): # we traverse a permutation cycle notation from left to right, so stack
                    if currElement not in cycle:
                        continue
                    currElement = cycle.map(currElement)
                if currElement not in currRes:
                    S.remove(currElement)
                    currRes.append(currElement)
                else:
                    break
            res.append(Cycle(currRes))

        # finished calculating the result
        return res
            

    def append(self, newCycle):
        if type(newCycle) is str:
            newCycle = Cycle(newCycle)
        self.cycles.append(newCycle)
        self.setmax = max(newCycle.getHighest(), self.setmax)

    def getSet(self) -> list:
        return [i + 1 for i in range(self.setmax)]

    def __str__(self) -> str:
        permuStr = ""
        for cycle in self.cycles:
            permuStr += str(cycle)
        return permuStr

    def __repr__(self) -> str:
        return str(self)

    def __len__(self) -> int:
        return len(self.cycles)
 
