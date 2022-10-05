def maior_primo(q):
    if(isPrimo(q)):
        return q
    while(q > 0):
        q -= 1
        if(isPrimo(q)):
            return q

def isPrimo(p):
    counter = 1
    i = 0
    if(p == 2):
        return True
    while(p >= counter):
        if p % counter == 0:
            i +=1            
        counter += 1
    if i > 2:
        return False
    else:
        return True


