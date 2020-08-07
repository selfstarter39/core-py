class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        s2=0
        s1=0
        try:
            
            fcardnum = self.card_num.replace(" ","") # replacing space
            
            if len(fcardnum) <= 1:
                raise ValueError
            
            for val in range(len(fcardnum)-2,-1,-2): # looping through the card and tacking evry 2nd and 2nd+1 character
                pdt = int(fcardnum[val]) * 2
                if pdt > 9:
                    pdt -=9
                
                s2 +=pdt   
                s1 +=int(fcardnum[val + 1])
                
                if (len(fcardnum) %2) != 0: # handling the 1st digit of the card for cards of odd lengths
                    s1 +=int(fcardnum[0])
                    
                    
            if ((s1 + s2) %10) == 0:    # applying Luhn's logic
                return True
            else:
                return False
            
       
        except ValueError:
            return False
        
        


