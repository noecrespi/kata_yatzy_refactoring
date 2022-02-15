
class Yatzy:
    
    @staticmethod
    def chance(*dados):
        """
        Recoge todos los dados y
        devuelve la suma de los mismos
        """
        return sum(dados)

    @staticmethod
    def yatzy(dados):
        """ 
        Mira que todos los números sean iguales
        """
        for dado in dados: # [1, 2, 3]
            if dado != dados[0]:
                return 0
        
        return 50
    
    @staticmethod
    def ones(*dados):
        """ 
        Mira y devuelve la suma de los dados 1
        """
        return dados.count(1) * 1

    @staticmethod
    def twos(*dados):
        """ 
        Mira y devuelve la suma de los dados 2
        """
        return dados.count(2) * 2

    @staticmethod
    def threes(*dados):
        """ 
        Mira y devuelve la suma de los dados 3
        """
        return dados.count(3) * 3

    def __init__(self, *dados) -> None:
        self.dados = dados

    def fours(self):
        return self.dados.count(4) * 4
    
    def five(self):
        return self.dados.count(5) * 5
    
    def sixes(self):
        return self.dados.count(6) * 6
    
    @staticmethod
    def score_pair(*dados):
        """ 
        Mira los dados y si hay dos números iguales los suma
        """
        for dado in dados:
            if dado == dado[0]:
        
        return
""" 
PASOS HECHOS Y COMPLETADOS:

class Yatzy:

    # No es necesario.
    # Lo mantengo para no romper la interfaz
    # publica de la clase segun los
    # casos test originales.
    def __init__(self, *dice):
        self.dice = list(dice)

    @staticmethod
    def chance(*dice):
        score = 0
        for die in dice:
            score += die
        return score

    @staticmethod
    def yatzy(*dice):
        if dice.count(dice[0]) != len(dice):
            return 0
        return 50

    @staticmethod
    def ones(*dice):
        ONE = Pips.ONE.value
        return dice.count(ONE) * ONE

    @staticmethod
    def twos(*dice):
        TWO = Pips.TWO.value
        return dice.count(TWO) * TWO

    @staticmethod
    def threes(*dice):
        THREE = Pips.THREE.value
        return dice.count(THREE) * THREE

    def fours(self):
        FOUR = Pips.FOUR.value
        return self.dice.count(FOUR) * FOUR

    def fives(self):
        FIVE = Pips.FIVE.value
        return self.dice.count(FIVE) * FIVE

    def sixes(self):
        SIX = Pips.SIX.value
        return self.dice.count(SIX) * SIX
"""

""" 
PASOS QUE FALTAN PARA REFACTORIZAR:

    @staticmethod
    def pair(*dice):
        PAIR = 2
        for pip in Pips.reversedValues():
            if dice.count(pip) >= PAIR:
                return PAIR * pip
        return 0
    @classmethod
    def two_pairs(cls, *dice):
        PAIR = 2
        pips_pairs = cls.__filter_pips_repeated(dice, PAIR)
        return sum(pips_pairs) * PAIR if len(pips_pairs) == 2 else 0

    @classmethod
    def three_of_a_kind(cls, *dice):
        THREE = 3
        pip = cls.__biggest_pip_repeated(dice, THREE)
        return pip * THREE if pip else 0

    @classmethod
    def four_of_a_kind(cls, *dice):
        FOUR = 4
        pip = cls.__biggest_pip_repeated(dice, FOUR)
        return pip * FOUR if pip else 0

    @classmethod
    def __biggest_pip_repeated(cls, dice, times):
        pips = cls.__filter_pips_repeated(dice, times)
        return pips[0] if pips else []

    @classmethod
    def __filter_pips_repeated(cls, dice, times):
        return list(filter(lambda pip: dice.count(pip) >= times, Pips.reversedValues()))

    @classmethod
    def small_straight(cls, *dice):
        return cls.chance(*dice) if not Pips.minus(Pips.SIX) - set(dice) else 0

    @classmethod
    def large_straight(cls, *dice):
        return cls.chance(*dice) if not Pips.minus(Pips.ONE) - set(dice) else 0

    @classmethod
    def fullHouse(cls, *dice):
        if cls.two_of_a_kind(*dice) and cls.three_of_a_kind(*dice):
            return cls.two_of_a_kind(*dice) + cls.three_of_a_kind(*dice)
        else:
            return 0

    @classmethod
    def two_of_a_kind(cls, *dice):
        PAIR = 2
        for pip in Pips.reversedValues():
            if dice.count(pip) == PAIR:
                return PAIR * pip
        return 0
"""
