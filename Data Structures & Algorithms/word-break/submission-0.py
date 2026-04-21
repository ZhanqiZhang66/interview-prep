class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # catsincars cat sin car s
        # catsincars cats in car s
        n = len(s)

        def dp(ss):
            if ss in wordDict:
                return True
            for j in range(0, len(ss)):
                print(f"{ss[:j+1]} and {dp(ss[j+1:])}")
                if ss[:j+1] in wordDict and dp(ss[j+1:]):
                    return True
            return False
        return dp(s)
            

        