class Yatzy:
    #Constructor de la clase
    def __init__(self, d1, d2, d3, d4, _5):
        self.dice = [0]*5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = _5
    
    @staticmethod
    def chance(d1, d2, d3, d4, d5):
        total = sum([d1,  d2,  d3,  d4,  d5])
        return total
    @staticmethod
    def sumar_la_cara(dice, cara):
        counts=[0]*(len(dice)+1)
        for die in dice:
            counts[die-1]+=1
        return counts[cara-1]*cara

    @staticmethod
    def sumar_par_mayor(caras_que_muestran_los_dados):

        pos=6
        contador_de_caras=[0]*6 # 6 es lo mismo que len(caras_que_muestran_los_dados)+1

        for cara_actual in caras_que_muestran_los_dados:
            contador_de_caras[cara_actual-1]+=1
            
        for numero_repeticiones in contador_de_caras:
            pos-=1
            if contador_de_caras[pos]>=2:
                return (pos+1)*2

        return 0

    @staticmethod
    def sumar_dos_pares(caras_de_los_dados):
        num_pares=0
        suma=0
        pos=-1
        contadores_de_caras=[0]*6

        for cara in caras_de_los_dados:
                contadores_de_caras[cara-1]+=1

        for veces_de_la_cara in contadores_de_caras:
                pos+=1
                if veces_de_la_cara >=2:
                        suma+=(pos+1)*2
                        num_pares+=1

        if num_pares==2:
                return suma
        else:
                return 0

    @staticmethod
    def tres_cuatro_de_un_tipo(caras_de_los_dados,cantidad):
        pos=-1
        contadores_de_caras=[0]*6

        for cara in caras_de_los_dados:
                contadores_de_caras[cara-1]+=1

        for veces_de_la_cara in contadores_de_caras:
            pos+=1
            if veces_de_la_cara >= cantidad:
                return (pos+1)*cantidad

        return 0

    @staticmethod
    def small_large_straight(caras_de_los_dados,small_large): #small_large ==1 significa escalera pequeña
        pos=-1
        es_escalera=True
        resultado=False
        contadores_de_caras=[0]*6

        for cara in caras_de_los_dados:
                contadores_de_caras[cara-1]+=1
        
        for contador in contadores_de_caras:
            pos+=1
            if small_large==1:
                resultado=pos<5
            else:
                resultado=pos>0
                
            if resultado==True:                     #pos>0:   #pos<5
                if contador!=1:
                    es_escalera=False
            else:
                if contador!=0:
                    es_escalera=False
        if es_escalera== True:
            if small_large==1:
                return 15
            else:
                return 20
        else:
            return 0

    @staticmethod
    def full_house(caras_de_los_dados):
        pos=-1
        pos_dos=-1
        pos_tres=-1
        
        contadores_de_caras=[0]*6

        for cara in caras_de_los_dados:
                contadores_de_caras[cara-1]+=1

        for contador in contadores_de_caras:
        pos+=1
        if contador==2:
        pos_dos=pos
        else:
            if contador==3:
                pos_tres=pos

        if pos_dos!=-1 and  pos_tres!=-1:
            return (pos_dos+1)*2+(pos_tres+1)*3
        else:
            return 0
        

        

#juego=Yatzy(1,2,3,4,5)
#print("Prueba de chance()")
#print(Yatzy.chance(1,1,1,1,1))
#print(Yatzy.sumar_la_cara([1,2,1,3,2],6))
#print(Yatzy.sumar_par_mayor([3,3,3,3,1]))
#print(Yatzy.sumar_dos_pares([4,4,4,4,4]))
#print(Yatzy.tres_cuatro_de_un_tipo([2,2,2,2,5],3))
#print(Yatzy.small_large_straight([4,2,6,3,5],2))
print(Yatzy.full_house([1,1,2,2,2]))