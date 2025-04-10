class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin = 0
        leftMax = 0
        for c in s:  # Iterate through each character in the string s
            if c == "(":
                leftMin += 1
                leftMax += 1
            elif c == ")":
                leftMin -= 1
                leftMax -= 1
            else:  # If the character is '*', decrement leftMin by 1 and increment leftMax by 1.
                leftMin -= 1
                leftMax += 1
            if leftMax < 0:
                return False  # return False since it means there are more closing parentheses than opening ones.
            if leftMin < 0:
                leftMin = 0  # reset it to 0 since we can't have negative open parentheses count
        return leftMin == 0
