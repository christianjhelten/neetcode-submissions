'''


'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        memory = {}

        def dfs(i):
            if i == len(s):
                return True
            if i in memory:
                return memory[i]

            for end in range(i+1, len(s)+1):
                piece = s[i:end]

                if piece in words and dfs(end):
                    memory[i] = True 
                    return True 
            memory[i] = False 
            return False


        return dfs(0)
