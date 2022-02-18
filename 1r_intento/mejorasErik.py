class Yatzy:
    

    @staticmethod  #linea 5: dices esta mal escrito en ingles, se escribe:" Dice"
# linea 5: one deberia seria ONCES porque devuelve los unos.

    # los metodos de one a sixes son muy parecidos
    #se podria crear un metodo privado y llamar ese desde la interfaz publica
    def one(*dices):
        return dices.count(1)

    @staticmethod
    def twos(*dices):
        return dices.count(2) * 2 #meter los valores en contantes para que la modificación sea más facil lo 
    #lo mismo pasa con las def del 1-6

    @staticmethod
    def threes(*dices):
        return dices.count(3) * 3

    @staticmethod
    def fours(*dices):
        return dices.count(4) * 4
    
    @staticmethod
    def fives(*dices):
        return dices.count(5) * 5
    
    @staticmethod
    def sixes(*dices):
        return dices.count(6) * 6

    @staticmethod
    def chance(*dices): #utlizar sum
        total = 0
        for dice in dices:
            total += dice 
        return total

    @staticmethod
    def score_pair(*dices):
        for number in range(6, 0 ,-1):
            if dices.count(number) >= 2:
                return number * 2
        return 0

    @staticmethod #
    def two_pair(*dices):
        pairs=[]
        for number in range(1,7):
            if dices.count(number) >= 2:
                pairs.append(number*2)
        print(pairs) #eliminar estar este print,porque no aporta nada
        if len(pairs) > 1: #mejor poner que len=2 porque si son 6 dados ya no seria compatible
            return sum(pairs)
        else:
            return 0

    @staticmethod  #linea 56: habria que hacer pruebas para ver el tiempo de   que tarda. Mejor hacer: for number in set(dices)
    def three_of_a_kind(*dices):
        for number in range(6, 0 ,-1):
            if dices.count(number) >= 3:
                return number * 3
        return 0

    @staticmethod
    def four_of_a_kind(*dices): #simplificar el codigo 
        dice = list(set(dices)) # score_pair,three of a kind y este medoso son muy parecidos.
        #se podria crear un metodo privado y llamar ese desde la interfaz publica
        if len(dice) == 2:
            if dices.count(dice[0]) == 4:
                return dice[0] * 4
            else: 
                return dice[1] * 4
        else:
            return 0

    @staticmethod
    def small_straight(*dices): #
        for i in range(1,6):
            if dices.count(i) == 0:
                return 0
        return 15

    @staticmethod
    def large_straight(*dices):
        for i in range(2,7): # mejor utilizar un IF y un not in porque se lee mejor. 
            if dices.count(i) == 0:
                return 0
        return 20
            

    @staticmethod
    def full_house(*dices):
        dice = list(set(dices)) 
        if len(dice) > 2: # se puede simplificar utlizando el set(dices) dentro del len().
            #quitar linea 88 y modificar linea 89 son set dice
            return 0
        score = 0 #añadir linea 92 set y luego cambiar el if, elif en else
        for i in range(1,7):
            if dices.count(i) == 3:
                score += i * 3
            elif dices.count(i) == 2:
                score += i * 2
        return score

    @staticmethod
    def yatzy(*dice):
        for i in dice: #cambiar i por dice. y utilizar un set =1 return 50
            if dice.count(i) == 5:
                return 50
            else:
                return 0