
class Ksiazka:
    def __init__(self, tytul, autor, rok):
        self.tytul = str(tytul)
        self.autor = str(autor)
        self.rok = int(rok)

    def __repr__(self):
        return f"{self.tytul}, {self.autor}, {self.rok}"

class Czytelnik:
    wypozyczone_ksiazki=[]

    def __init__(self, imie):
        self.imie = str(imie)

    def __repr__(self):
        return self.imie
        
    def dodaj(self,obj):
        Czytelnik.wypozyczone_ksiazki.append(obj)
    
    def remove(self,obj):
        Czytelnik.wypozyczone_ksiazki.remove(obj)


class Biblioteka:
    lista_ksiazek=[" Bartek Perkowski ",'pawel']
    czytelnicy=[]

    @property
    def lista(self):
        return Biblioteka.lista_ksiazek

    @property
    def listaCzytelnicy(self):
        return Biblioteka.czytelnicy

    def dodaj(self,obj):
        Biblioteka.lista_ksiazek.append(obj)
    
    def dodajCzytelnika(self,obj):
        Biblioteka.czytelnicy.append(obj)


biblioteka = Biblioteka()

liczbaEgz=int(input())
isOperationSucccesfull = []

for i in range(liczbaEgz):
    operation = eval(input())
    opeartionType = operation[0].strip()

    if(opeartionType == "dodaj"):
        tytul = operation[1]
        autor = operation[2]
        rok = operation[3]
        ksiazka = Ksiazka(tytul, autor, rok)
        biblioteka.dodaj(ksiazka)
        isOperationSucccesfull.append(True)
    
    elif(opeartionType == "wypozycz"):
        name = operation[1]
        tytul = operation[2]
        print(biblioteka.listaCzytelnicy)
        if name not in biblioteka.listaCzytelnicy:
            czytelnik = Czytelnik(name)
            biblioteka.dodajCzytelnika(czytelnik)
        print(biblioteka.listaCzytelnicy)

        



    elif(opeartionType == "oddaj"):
        print('oddaj operation type')


for result in isOperationSucccesfull:
    print(result)
    