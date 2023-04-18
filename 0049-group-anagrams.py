class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #  Default Dictionary will default the key if the key has not been set yet.       
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
#                 Ord gives ascii values of char. Here subtarcting it from a will gives value to alphabets as a = 0 , b = 1 . 
#                   If Ord(a) = 76 , then ord('a') - ord('a') = 0 ...
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()
