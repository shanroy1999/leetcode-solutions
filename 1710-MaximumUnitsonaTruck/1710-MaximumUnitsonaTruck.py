class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # Sort the boxTypes based on the number of units which we want to maximize
        sortedBoxTypes = sorted(boxTypes, key = lambda x: x[1], reverse = True)
        countUnits = 0
        for box, unit in sortedBoxTypes:
            # Base condition => when truckSize reaches zero => cannot add more boxes => return count
            if truckSize==0:
                return countUnits
            # Need to keep taking the boxes while maximizing the number of units until truckSize reached
            boxes = min(box, truckSize)
            # Keep adding the units of the boxes selecting
            countUnits += boxes*unit
            # Decrement the trucksize by the number of boxes added
            truckSize -= boxes
        return countUnits