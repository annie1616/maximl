
 
def sequence(st): 
    n = len(st) 
    m= 1
    distlen = 1  
    p = -1    
    i = 0   
    hasharr = [0] * 256 
    
   
    for i in range(n):
        if st[i]>='a' and st[i]<='z':
            p = hasharr[ord(st[i])] 
            if p == -1 or (i - m > p): 
                m+= 1
        
            else: 
           
                if m > distlen: 
                    distlen = m 
  
                m = i - p 
         
            hasharr[ord(st[i])] = i
        else:
            return 0
  
    
        if m > distlen: 
            distlen = m 
  
    return distlen 
  

st=input()
print(sequence(st))
