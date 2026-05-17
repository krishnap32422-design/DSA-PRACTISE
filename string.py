#3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        ans=set()
        max_count=0
        for right in range(len(s)):
            while s[right]  in ans:
                ans.remove(s[left])
                left+=1

            ans.add(s[right])
            max_count=max(max_count,right-left+1)
        return max_count
                

                
