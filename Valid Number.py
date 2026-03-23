class Solution:
    def isNumber(self, s: str) -> bool:
        digit = dot = exp = False
        
        for i, char in enumerate(s):
            if char.isdigit():
                digit = True
            elif char in "+-":
                # Signs can only appear at the start or immediately after an 'e'
                if i > 0 and s[i-1] not in "eE":
                    return False
            elif char in "eE":
                # Exponent needs a preceding digit and can't be repeated
                if exp or not digit:
                    return False
                exp = True
                digit = False  # Reset digit to ensure something follows the 'e'
            elif char == ".":
                # Dots aren't allowed in exponents or if already seen
                if dot or exp:
                    return False
                dot = True
            else:
                return False
                
        return digit
