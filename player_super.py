#latihan python
class Player:
    def __init__(self, name, speed):
        self.name  = name
        self.speed = speed

    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed
    
    def getSkill(self):
        return 'normal'

class PortugalPlayer(Player):
    def __init__(self, name, speed):
        super().__init__(name, speed)
        print('Hello Portugal!')

#diluar kelas
pemain  = PortugalPlayer('Ronaldo', '99')

print(pemain.getName() + ' skillnya ' + pemain.getSkill())
