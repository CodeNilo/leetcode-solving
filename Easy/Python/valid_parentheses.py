class Solution:
    def isValid(self, s: str) -> bool:

        map = {")":"(", "]":"[", "}":"{"}

        stack = []

        for char in s:

            if char in map.values():

                stack.append(char)

            else:

                if not stack:

                    return False
            
                else:

                    if map[char] is not stack.pop():

                        return False
                
        
        if len(stack) > 0:

            return False

        else:

            return True

                

            


            
