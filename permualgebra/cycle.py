import sys

class Cycle:
    def __init__(self, cycle):
        """
        Create a new Cycle object in 2 options.
        Option 1: from string, format "1 2 3"
        Option 2: from list, format [1,2,3]
        Result: (1 2 3)
        """
        self.elements = []  # store a cycle in a list, (1 2 3) -> [1, 2, 3]
    
        # option 1: from string
        if type(cycle) is str:
            cycleCharList = cycle.split(" ")
            self.elements = [int(element) for element in cycleCharList]
        # option 2: from list
        elif type(cycle) is list and all(type(element) is int for element in cycle):
            self.elements = cycle
        else:
            sys.stderr.write("Invalid Cycle Initialization: TypeError\n");
            exit(-1)
        
        # check for duplicated elements
        if len(self.elements) > len(set(self.elements)):
            sys.stderr.write("Invalid Cycle Initialization: Duplicate Element in a Cycle\n");
            exit(-1)

    def map(self, elementIn: int):
        """
        map an element to another
        """
        if elementIn not in self.elements:
            return "N/A"
        
        # since now we are guaranteed to have this input element, feel free to find its index
        index = self.elements.index(elementIn)

        # case 1: input element is the last element in this Cycle
        #   then this input elements get mapped to the first element in this cycle
        if index == len(self.elements) - 1:
            return self.elements[0]
        # case 2: the input element is not the last one
        #   then map to the next element
        else:
            return self.elements[index + 1]

    def append(self, newElement) -> bool:
        if newElement in self.elements:
            return False

        self.elements.append(newElement)
        return True

    def getHighest(self) -> int:
        return max(self.elements)

    def TeX(self, type = "defualt") -> str:
        if len(self) == 0 or len(self) == 1:
            return ""

        TeX = ""
        if type == "text":
            TeX = "\\text{" + str(self) + "}"
        elif type == "math":
            TeX = "("
            for element in self.elements:
                TeX += str(element) + "\\:"
            TeX = TeX[:-2]
            TeX += ")"
        else:
            TeX = str(self)

        return TeX


    def __str__(self) -> str:
        if len(self) == 0 or len(self) == 1:
            return ""

        # otherwise give the cyclic notation of this Cycle
        cycleStr = "("
        for element in self.elements:
            cycleStr += str(element) + " "
        cycleStr = cycleStr[:-1]
        cycleStr += ")"
        return cycleStr
    
    def __repr__(self) -> str:
        return str(self)

    def __len__(self) -> int:
        return len(self.elements)

    def __contains__(self, element: int) -> bool:
        return element in self.elements


        
