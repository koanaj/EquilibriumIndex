def equilibrium(tab): 
    lewo = 0
    prawo = 0
    n = len(tab) 
  
    # sprawdzaj indexy jeden po drugim
    for i in range(n): 
        lewo = 0
        prawo = 0
      
        # znajdz lewą sumę
        for j in range(i): 
            lewo += tab[j] 
          
        # znajdz prawą sumę
        for j in range(i + 1, n): 
            prawo += tab[j] 
          
        #jeżeli lewa strona rowna z prawą daj wynik
        if lewo == prawo: 
            return i 
      
    # wróć -1 jeżeli nie znajdziemy środka
    return -1
              
# test liczb z tablicy
tab = [5, 4, 1, 2, 3, 0, 1, 2, 3, 4, 5]
print (equilibrium(tab)) 