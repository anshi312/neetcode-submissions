class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # 1 2 3 4 4 5 6 7
        # 1 1 1 2 2 1 1 1

        if len(hand) % groupSize != 0:
            return False

        hand.sort()
        count = defaultdict(int)
        for num in hand:
            count[num] += 1

        for num in hand:
            if count[num]:
                for i in range(num, num + groupSize):
                    if not count[i]:
                        return False
                    count[i] -= 1
        return True