class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = {}
        for string in strs:
            sorted_str_list = sorted(string)
            digest = ""
            for char in sorted_str_list:
                digest += char

            if digest not in anagrams:
                anagrams[digest] = [string]
            else:
                anagrams[digest].append(string)
            solution = []
        for group in anagrams.values():
            solution.append(group)
        return solution