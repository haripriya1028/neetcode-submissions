class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq={}
        for word in strs:
            sorted_word=tuple(sorted(word))
            if sorted_word not in freq:
                freq[sorted_word]=[]
            freq[sorted_word].append(word)
        return list(freq.values())
