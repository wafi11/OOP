# class and object
class Player:
    def __init__(self,name,Kelamin,):
        self.name = name
        self.kelamin = Kelamin

    def Name (self):
        print ('nama    : ', self.name)

    def Kelamin(self):
        print ('kelamin : ',self.kelamin)

n = Player('wafi','Laki-laki')
n.Name()
n.Kelamin()
