#%%
import numpy as np

class stringcount():
    def __init__(self,chuoi):
        self.chuoi = chuoi
    def counts(self):
        
        return len(self.chuoi)
    
    def countktdb(self):
        for ky_tu in '~!@#$%^&*()':
            for i in self.chuoi:        
                if ky_tu == i:
                    print(i)
   # def countupper(self):
        
A = stringcount(chuoi='ha thanh khiet')
A.counts()
A.countktdb()            
        
        

# %%
