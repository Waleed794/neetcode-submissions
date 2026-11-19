import re
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_start = 0
        str_end = 0
        substring = ''


        # while str_end<len(s):
        #     temp_str = s[str_start:str_end]
        #     remainder_str = s[str_end] #s[str_end:]

        #     if remainder_str[0] not in temp_str:
        #         str_end+=1
                    
        #     else:
        #         if len (temp_str)> len(substring):
        #             substring = max(substring, temp_str, key=len)
        #         str_start +=1


        # return len(substring)

        while str_end < len(s):
            temp_str = s[str_start:str_end]
            remainder_str = s[str_end]

            if remainder_str not in temp_str:
                str_end += 1
                candidate = s[str_start:str_end]
                if len(candidate) > len(substring):
                    substring = candidate
            else:
                if str_start < str_end:
                    str_start += 1
                else:
                    str_end += 1

        return len(substring)
            
