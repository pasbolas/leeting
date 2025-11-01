# Ugly Solution // Didnt use stack

class Solution:
    def isValid(self, s: str) -> bool:

        keydict = {
            "(": 0,
            ")":0,
            "{": 0,
            "}": 0,
            "[": 0,
            "]": 0
        }

        previous_word = s[0]

        match previous_word:
            case "(":
                keydict["("] += 1
            case ")":
                keydict[")"] += 1
            case "[":
                keydict["["] += 1
            case "]":
                keydict["]"] += 1
            case "{":
                keydict["{"] += 1
            case "}":
                keydict["}"] += 1
        

        for word in s[1:]:

            match previous_word:
                case "(":
                    if word == "]" or word == "}":
                        return False
                case "[":
                    if word == ")" or word == "}":
                        return False
                case "{":
                    if word == ")" or word == "]":
                        return False
                        
            previous_word = word

            match word:
                case "(":
                    keydict["("] += 1
                case ")":
                    keydict[")"] += 1
                case "[":
                    keydict["["] += 1
                case "]":
                    keydict["]"] += 1
                case "{":
                    keydict["{"] += 1
                case "}":
                    keydict["}"] += 1
        
        if (keydict["("] - keydict[")"]) != 0  or (keydict["["] - keydict["]"]) != 0 or (keydict["{"] - keydict["}"]) != 0:
            return False
        else:
            return True
        

# Beautiful Solution we used stacks here:

class StackSolution:
    def isValid(s: str) -> bool:

        stack = []
        pairs = {"(":")", "{":"}", "[":"]"}

        for character in s:
            if character in pairs:
                stack.append(character)
            elif character in pairs.values():
                if not stack or character != pairs[stack[-1]]:
                    return False
                stack.pop()
        
        if len(stack) != 0:
            return False
        
        return True

print(StackSolution.isValid("("))