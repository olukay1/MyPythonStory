import random
import string

def pwdGen():
    al = string.ascii_lowercase +  string.ascii_uppercase + string.digits + string.punctuation
    p=5
    s = 8
    for j in range(p):
        passw = "".join(random.choice(al) for i in range (0, s))
        return passw

print(pwdGen())



 #r = random(for i in range v())
 