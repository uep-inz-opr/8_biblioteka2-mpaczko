liczbaEgz=int(input())
ans = []
biblioteka = []
wypozyczone = {}

for i in range(liczbaEgz):
    operation = eval(input())
    opeartionType = operation[0].strip() 
    if opeartionType == "dodaj":
        biblioteka.append(operation[1])
        ans.append(True)
    elif opeartionType == "wypozycz":
        klient = operation[1]
        ksiazka = operation[2]
        if ksiazka in biblioteka:
            if klient not in wypozyczone:
                wypozyczone[klient] = [ksiazka]
                biblioteka.remove(ksiazka)
                ans.append(True)
            else:
                if ksiazka not in wypozyczone[klient] and len(wypozyczone[klient])<3:
                    wypozyczone[klient].append(ksiazka)
                    biblioteka.remove(ksiazka)
                    ans.append(True)
                else:
                    ans.append(False)
        else:
            ans.append(False)

    elif opeartionType == "oddaj":
        klient = operation[1]
        ksiazka = operation[2]
        
        if ksiazka not in wypozyczone[klient]:
            ans.append(False)
        else:
            wypozyczone[klient].remove(ksiazka)
            biblioteka.append(ksiazka)
            ans.append(True)



for result in ans:
    print(result)