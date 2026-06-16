class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank_map = {char: i for i, char in enumerate(order)}

        for i in range(len(words) - 1):
            word_1 = words[i]
            word_2 = words[i + 1]

            for j in range(min(len(word_1), len(word_2))):
                if rank_map[word_1[j]] > rank_map[word_2[j]]:
                    return False
                if rank_map[word_1[j]] < rank_map[word_2[j]]:
                    break

            else:
                if len(word_1) > len(word_2):
                    return False

            
        return True
                    