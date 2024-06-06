class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        contador = 0
        aux = []
        hand.sort()
        if len(hand) == 1 and groupSize == 1:
            return True
        if len(hand)%groupSize != 0:
            return False
        else:
            while len(hand) > 0:
                card = hand[0]
                aux = []
                contador = 0
                while contador < groupSize:
                    if card+contador in hand:
                        aux.append(card+contador)
                        contador+=1
                    else:
                        return False
                for item in aux:
                    hand.remove(item)
        return True
s = Solution()
s.isNStraightHand([8,10],2)