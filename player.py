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

#diluar kelas
pemain  = Player('Ronaldo', '99')
pemain2 = Player('Messi', '98')
print(pemain.getName() + ' punya kecepatan ' + pemain.getSpeed())
print(pemain2.getName() + ' punya kecepatan ' + pemain2.getSpeed())