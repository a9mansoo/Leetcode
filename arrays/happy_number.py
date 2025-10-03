class Solution:
    def isHappy(self, n: int) -> bool:
        numbers_seen = set()

        curr_num = n
        while True:
            str_num = str(curr_num)
            s = 0
            for num in str_num:
                s += int(num)**2
            print(numbers_seen)
            if s in numbers_seen:
                return False
            elif s == 1:
                return True
            numbers_seen.add(s)
            curr_num = s
            
        
sol = Solution()
sol.isHappy(19)