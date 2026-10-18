class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # n = len(temperatures)
        # stack = []
        # for i in range(n):
        #     count = 1
        #     j = i + 1
        #     while j < n:
        #         if temperatures[j] > temperatures[i]:
        #             break
        #         j += 1
        #         count += 1
        #     count = 0 if j == n else count
        #     stack.append(count)
        # return stack

        res = [0] * len(temperatures)
        stack = [] # store index of days

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                prev_day = stack.pop()
                res[prev_day] = i - prev_day
            
            stack.append(i)
        
        return res





            
        