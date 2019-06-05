# Create a class called party that has a insance cap and name list. 
# Create methods that welcomes guest into the party and methods that kicks out guest out of the party and a method that changes the size of the party
class Party:
    def __init__(self,cap):
        self.cap = cap
        self.n_list = []
    
    def welcome(self, guest):
        if len(self.n_list) < self.cap:
            self.n_list.append(guest)
        else:
            print('No more room')
    
    def kick_out(self, guest):
        if guest in self.n_list:
            self.n_list.remove(guest)

    def change_size(self, size):
        self.cap = size
        while len(self.n_list) > self.cap:
            self.n_list.pop()

rager = Party(5)
print(rager.cap)
rager.welcome('angelo')
rager.welcome('bob')
rager.welcome('david')
rager.welcome('kathy')
rager.welcome('jeared')
rager.kick_out('bob')
rager.change_size(8)
print(rager.n_list)
