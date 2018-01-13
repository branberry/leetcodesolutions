class Solution:
    def JudgeCircle(self, moves):
        xVal = 0
        yVal = 0
        print(len(moves))
        for i in range(len(moves)):
            
            if moves[i] == "U":
                yVal = yVal + 1
                print("yVal: ", yVal)
                print("xVal: ", xVal)
            elif moves[i] == "D":
                yVal = yVal - 1
                print("yVal: ", yVal)
                print("xVal: ", xVal)
            elif moves[i] == "R":
                xVal = xVal + 1
                print("yVal: ", yVal)
                print("xVal: ", xVal)
            elif moves[i] == "L":
                print(moves[i])
                xVal = xVal - 1
                print("yVal: ", yVal)
                print("xVal: ", xVal)
        if xVal == 0 and yVal == 0:
            return True
        else:
            return False
            


s = Solution()
print(s.JudgeCircle("UD"))
print("Y" == "Y")