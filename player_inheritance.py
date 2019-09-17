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

class PortugalPlayer(Player):
    def setShot(self, shot):
        self.shot = shot
        return self.shot

#diluar kelas
pemain  = PortugalPlayer('Ronaldo', '99')

print(pemain.getName() + ' punya tendangan ' + pemain.setShot('90'))
