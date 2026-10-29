class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    
        #stack = []
        # res = [0] * len(temperatures)

        # for i in range(len(temperatures)):
        #     for j in range(len(temperatures)):
        #         if temperatures[i] < temperatures[j]:
        #             res[i] = j - i

        #             break
        # return res

        stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):

            while stack:
                end_day = stack[-1]

                if temperatures[i] > temperatures[end_day]:
                    stack.pop()
                    result[end_day] = i - end_day

                else:
                    break
            stack.append(i)
        return result

