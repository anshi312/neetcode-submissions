class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 4 1 0 7     0  1. 4. 7
        # 2 2 1 1 
        # 3 8 10 3.   10  8 3  3
        # pos = [0 4 2]
        # sp =  [2 1 3]
        # pairs = [0,2.  2,3.   4,1]
        # time = [5, 2.4, 6]



        pairs = []
        for i in range(len(position)):
            pairs.append((position[i], speed[i]))

        stack = []
        pairs.sort(key=lambda x:x[0], reverse = True)

        for pos, sp in pairs:
            time = (target - pos) / sp

            if stack and (time > stack[-1]):
                stack.append(time)
            if not stack:
                stack.append(time)
        
        return len(stack)



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # pairs = []
        # for i in range(len(position)):
        #     pairs.append((position[i], speed[i]))
        # pairs.sort(reverse=True)

        # stack = []
        # for p, s in pairs:
        #     stack.append((target - p) / s)

        #     if len(stack) >= 2 and stack[-1] <= stack[-2]:
        #         stack.pop()

        # return len(stack)