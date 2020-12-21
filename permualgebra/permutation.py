import sys
import copy as copy
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
        """
        Theorem. Every permutation on S = {1, ..., n} can be written as a product of **disjoint cycles**.
        i.e. no element of S repented in the cycle description.
        """
        S = self.getSet()       # set of preimage, i.e. domain; work as a queue
        res = Permutation()     # the result permutation in product of disjoint cycles
        while S:                # while S is not empty, keep goinf
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

    def simplify(self):
        """
        simply this Permutation itself
        """
        S = self.getSet()
        newList = []
        while S:                # while S is not empty, keep goinf
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
            newList.append(Cycle(currRes))

        # finished calculating the result
        self.cycles = newList
 
    def TeX(self, type="default") -> str:
        """
        Give the TeX(LaTeX) format in three ways:
            1. text
                $$ \text{(1 2 3)(4 5 6)} $$
                can be inserted into a math environment.
            2. math
                $$ (1\:2\:3)(4\:5\:6) $$
                can be inserted into a math environment without using \text{}
            3. default
                (1 2 3)
                if inserted into math environment, there will be no space inbetween.
        """
        TeX = ""
        if type == "text":
            return "\\text{" + str(self) + "}"
        elif type == "math":
            for cycle in self.cycles:
                TeX += cycle.TeX(type="math")
        else:
            TeX = str(self)
        return TeX

    def append(self, newCycle):
        """
        append a new cycle into this permutation,
        input: newCycle -> str
            or newCycle -> Cycle()
        """
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

    def __mul__(self, otherPerm):
        res = copy.deepcopy(self)
        for cycle in otherPerm.cycles:
            res.append(cycle)
        return res


 
