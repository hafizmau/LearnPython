#latihan python
class Player:
    name = ''

    def getName(self, name):
        self.name = name
        return name

#diluar kelas
pemain = Player()
print(pemain.getName('hafiz'))