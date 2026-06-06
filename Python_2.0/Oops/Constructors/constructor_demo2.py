class Match :

    def __init__(self) :
        
        print("Default Constructor Match Class is Called!!")

        self.run = 161

        self.wicket = 10

    def getScore(self) :

        return self.run , self.wicket
    
m1 = Match()

r , w = m1.getScore()

print(r)

print(w)

m2 = Match()

r , w = m2.getScore()

print(r)

print(w)