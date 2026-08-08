class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq={}
        for word in strs:
            count=[0]*26
            for c in word:
                index=ord(c)-ord('a')
                count[index]+=1
            key=tuple(count)
            if key not in freq:
                freq[key]=[]
            freq[key].append(word)
        return list(freq.values())