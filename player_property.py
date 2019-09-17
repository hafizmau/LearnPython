#latihan python
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    #@property
    def infoPlayer(self):
        return self.name + ' berumur ' + self.age
    
    #@infoPlayer.setter
    # def infoPlayer(self, data):
    #     name, age = data.split(' ')
    #     self.name = name
    #     self.age = age

player = Player('bang do', '32')
print(player.infoPlayer())

    

