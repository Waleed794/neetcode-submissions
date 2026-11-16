import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean_str = ''.join(s.split())
        # clean_str = ''.join(char for char in s.split() if char.isalnum())
        clean_str = re.sub(r'[^a-zA-Z0-9]','',s).lower()
        rev = clean_str[::-1].lower()
        if clean_str==rev:
            return True
        else:
            return False