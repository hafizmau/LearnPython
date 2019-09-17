#latihan python
class Player:
    def __init__(self, name):
        self.name  = name
        self.__speed = '89'

    def getName(self):
        return self.name

    def getSpeed(self):
        return self.__speed
    

class PortugalPlayer(Player):
    pass

#diluar kelas
pemain  = PortugalPlayer('Ronaldo')
pemain.name = 'Joao Felix'
pemain.__speed = '79'

print(pemain.getSpeed() + ' namanya ' + pemain.getName())
