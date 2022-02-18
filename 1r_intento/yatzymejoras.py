def n_of_a_kind(dice, n):
        score = 0
        for value in range(6+1):
            if dice.count(value) >= n:
                score = n * value
        return score
    
class Yatzy:
    def __init__(self, d1, d2, d3, d4, d5):
        self.dice = [0]*5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = d5
    # def __init__(self, dice):
    #     self.dice = dice

    @staticmethod
    def chance(*dice):
        total = sum(dice)
        return total

    @staticmethod
    def yatzy(dice):
        for die in dice:
            if die == dice[0]:
                continue
            else:
                return 0
        return 50

    @staticmethod
    def ones(d1,  d2,  d3,  d4,  d5):
        diceList = [d1, d2, d3, d4, d5]
        numeroDados = diceList.count(1)
        return numeroDados
        


    @staticmethod
    def twos(d1,  d2,  d3,  d4,  d5):
        diceList = [d1, d2, d3, d4, d5]
        numeroDados = diceList.count(2)
        return numeroDados * 2
    
    @staticmethod
    def threes(d1,  d2,  d3,  d4,  d5):
        diceList = [d1, d2, d3, d4, d5]
        numeroDados = diceList.count(3)
        return numeroDados * 3
    

    # def __init__(self, d1, d2, d3, d4, _5):
    #     self.dice = [0]*5
    #     self.dice[0] = d1
    #     self.dice[1] = d2
    #     self.dice[2] = d3
    #     self.dice[3] = d4
    #     self.dice[4] = _5
    
    def fours(self):
        numeroDados = self.dice.count(4)
        return numeroDados * 4
    

    def fives(self):
        numeroDados = self.dice.count(5)
        return numeroDados * 5
    

    def sixes(self):
        numeroDados = self.dice.count(6)
        return numeroDados * 6
    

    
    
    @staticmethod
    def score_pair(d1,  d2,  d3,  d4,  d5):
        diceList = [d1, d2, d3, d4, d5]
        return n_of_a_kind(diceList,2)
    
    @staticmethod
    def two_pair(d1,  d2,  d3,  d4,  d5):
        diceList = [d1, d2, d3, d4, d5]
        score = 0
        numberPairs = 0
        for value in range(6+1):
            if diceList.count(value) >= 2:
                numberPairs += 1
                score += 2 * value
                if numberPairs == 2:
                    return score 
        return 0
    
    @staticmethod
    def three_of_a_kind(d1,  d2,  d3,  d4,  d5):
        diceList = [d1, d2, d3, d4, d5]
        return n_of_a_kind(diceList,3)
    
    @staticmethod
    def four_of_a_kind(d1,  d2,  d3,  d4,  d5):
        diceList = [d1, d2, d3, d4, d5]
        return n_of_a_kind(diceList,4)


    @staticmethod
    def smallStraight(d1,  d2,  d3,  d4,  d5):
        diceList = [d1, d2, d3, d4, d5]
        orderedDices = sorted(diceList) #aqui ordenamos los dados
        count = 0 
        for die in range(len(orderedDices)):
            if die != len(orderedDices)-1 and orderedDices[die] == orderedDices [die + 1] - 1:
                count += 1
                if count == 3:
                    return 15
        return 0
        

    @staticmethod
    def largeStraight(d1,  d2,  d3,  d4,  d5):
        diceList = [d1, d2, d3, d4, d5]
        orderedDices = sorted(diceList) #aqui ordenamos los dados
        count = 0 
        for die in range(len(orderedDices)):
            if die != len(orderedDices)-1 and orderedDices[die] == orderedDices [die + 1] - 1:
                count += 1
                if count == 4:
                    return 20
        return 0
    

    @staticmethod
    def fullHouse(d1,  d2,  d3,  d4,  d5):
        diceList = [d1, d2, d3, d4, d5]
        triple = n_of_a_kind(diceList,3)
        dice_without_triple = []
        #en el momento que encontramos un triple lo eliminamos
        for die in range(len(diceList)):
            if diceList[die] != triple/3:
                dice_without_triple.append(diceList[die])
        pair = n_of_a_kind(dice_without_triple,2) 
        
        if pair > 0 and triple > 0:
            return pair + triple
        else:
            return 0
        