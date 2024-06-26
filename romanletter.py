# class Solution:
#     def romanToInt(self, s: str) -> int:
#         translations = {
#             "I": 1,
#             "V": 5,
#             "X": 10,
#             "L": 50,
#             "C": 100,
#             "D": 500,
#             "M": 1000
#         }
#         number = 0
#         print(f"Original string: {s}")
#         s = s.replace("IV", "IIII").replace("IX", "VIIII")
#         s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
#         s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
#         print(f"Modified string: {s}")
#         for i in s:
#             number += translations[i]
#             print(f"Adding {translations[i]} for {i}, total now {number}")
#         return number

# sol = Solution()
# print(sol.romanToInt("CDXXXV"))


class Solution:
    def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        total = 0
        prev_value = 0
        
        for char in s:
            current_value = translations[char]
            if current_value > prev_value:
                # Subtract twice the previous value because it was added before
                total += current_value - 2 * prev_value
            else:
                total += current_value
            prev_value = current_value
        
        return total

# Example usage
sol = Solution()
print(sol.romanToInt("III"))       # Output: 3
print(sol.romanToInt("LVIII"))     # Output: 58
print(sol.romanToInt("MCMXCIV"))   # Output: 1994
