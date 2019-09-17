#latihan python
class Player:
    name  = ''
    speed = ''

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
    def getSkill(self,):
        return 'cepat'

class IndonesiaPlayer(Player):
    pass

#diluar kelas
pemain  = PortugalPlayer('Ronaldo', '99')
pemain2 = IndonesiaPlayer('Boas', '96')

print(pemain.getName() + ' skillnya ' + pemain.getSkill())
print(pemain2.getName() + ' skillnya ' + pemain2.getSkill())
