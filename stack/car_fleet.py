from typing import List


class Solution:
    def buildPointsArray(self, position, speed):
        pointsArray = []
        for p, s in zip(position, speed):
            pointsArray.append((p, s))
        pointsArray = sorted(pointsArray, key = lambda x: x[0], reverse=True)
        return pointsArray
    
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # We need to calculate the time each car will 
        # take to reach the target and store that
        stack = []
        pointsArray = self.buildPointsArray(position, speed)
        numFleets = 0

        for point in pointsArray:
            distLeft = target - point[0]
            timeTaken = distLeft / point[1]

            # If the car behind takes less than or equal time
            # it is part of the same fleet
            if not stack:
                stack.append(timeTaken)
            
            # If the car is behind and takes
            # more than the one ahead, then it is
            # a different fleet
            elif stack and timeTaken > stack[-1]:
                stack.append(timeTaken)

        numFleets = len(stack)
        return numFleets




sol = Solution()
sol.carFleet(target = 10, position = [1,4], speed = [3,2])
sol.carFleet(target = 10, position = [4,1,0,7], speed = [2,2,1,1])
