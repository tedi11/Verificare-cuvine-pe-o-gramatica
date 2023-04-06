lista = []
l1 = []
l2 = []
ll1 = []
ll2 = []

f = open("cuvinte.txt", 'r')
for linie in f:
    for cuv in linie.split():
        lista.append(cuv)
        
f2 = open("gramatici.txt", 'r')
for linie in f2:
    l1.append(linie.split()[0])
    l2.append(linie.split()[2])
    ll1.append(int(linie.split()[3]))
    ll2.append(int(linie.split()[1]))
for cuv in lista:
    nr = 0
    precedent = '~'
    forma1 = []
    forma2 = []
    for i in range(len(cuv)):
        if cuv[i] == precedent or i == 0:
            nr+=1  
            precedent = cuv[i]
        else:
            forma1.append(precedent)
            forma2.append(nr)
            precedent = cuv[i]
            nr = 1
    forma1.append(precedent)
    forma2.append(nr)
    ok = 1
    if len(forma1) > len(l1):
        continue
    for element in forma1:  
        if element not in l1:
            ok = 0
    j = 0
    l3 = []
    for i in range(len (forma1)):
        while l1[j] != forma1[i] and j < len(l1):
            l3.append(0)
            j+=1 
        if l1[j] == forma1[i]:
            l3.append(forma2[i])
            j+=1
        if i == len(forma1)-1 and j < len(l1):
            for k in range(j, len(l1)):
                l3.append(0)
    #print (l3)
    for p in range(len(l2)):
        for o in range(len(l2)):
            if l2[p] == l2[o]:
                if l3[p]/ll2[p] != l3[o]/ll2[o]:
                    ok = 0
    for i in range(len(ll1)):
        if l3[i] < ll1[i]:
            ok = 0
    for i in range(len(ll1)):
        if l3[i] % ll2[i] != 0:
            ok = 0
    if ok == 1:
        print(cuv)
        pass
    #print(l3)
    #print(forma1, forma2)


    