class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        result = []
        for i, w1 in enumerate(words):
            for j, w2 in enumerate(words):
                if i != j and w1 in w2:
                    result.append(w1)
                    break
        return result