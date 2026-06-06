class Match :

    def __init__(self , r , w) :
        
        self.r = r  
        
        self.w = w

    def getScoreInfo(self) :

        return self.r , self.w

m1 = Match(5006 , 690)

print(m1.getScoreInfo())

m2 = Match(3624 , 785)

print(m2.getScoreInfo())