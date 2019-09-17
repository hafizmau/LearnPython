#latihan python
class Player:
    name = 'Bang do'

    def __init__(self, speed):
        self.speed = speed

    @staticmethod
    def retiredIn(age):
        return str(40 - age)

    @classmethod
    def generalInfo(cls, age):
        return cls.name + ' akan pensiun dalam ' + cls.retiredIn(age) + ' tahun'
    
print(Player.generalInfo(23))
    

