import random

Fin = open("C:/Users/XYZ/[FILL]t", "w")             # System wypisywania i zapisywania do pliku
Fout = open("C:/Users/XYZ/[FILL]", "r")           # Jeśli program się nie kompiluje proszę o wprowadzenie tutaj sciezki absolutnej do plikow Fin.txt oraz Fout.txt, znajduja sie w folderze z plikiem main.py
Fin.truncate(0)

def Choice():
    print("**********************************************")
    print("               1. Ustawienia Domyslne")
    print("               2. Ustawienia Wlasne")
    print("               0. Exit")
    print("**********************************************")
    x=int(input())
    if(x==1):
        return 1
    elif(x==2):
        return 0
    else:
        exit(0)


def Generator(lenght, option,timesX=0,timesY=40,workX=50,workY=20):
    tab = []
    times = []
    work = []
    deviation = 0
    priority = []
    for i in range(lenght):                             #1
        tab.append(random.randint(0, 9))
    for i in range(lenght):                             #2
        times.append(random.randint(timesX, timesY))
    for i in range(lenght):                             #3
        priority.append(i)
    for i in range(lenght):
        deviation = random.randint(0, workY)            #4
        if(random.randint(0,10)%2==0):
            deviation = workX - deviation
        else:
            deviation = workX + deviation
        if(deviation<0):
            deviation=0
        work.append(deviation)
    random.shuffle(priority)

    if(option==1):     #zwracam tablice z losowymi danymi
        return tab
    elif(option==2):   #zwracam losowe czasy przyjscia (us)
        return times
    elif(option==3):   #zwracam losowy priorytet
        return priority
    elif(option==4):   #zwracam czasy przetwarzania
        return work   
    else:
        exit(0)


def FIFO(tab,work):
    WorkTime = 0
    Hit = 0
    Fault = 0
    FH = 0
    Numbers = [0,0,0,0,0,0,0,0,0,0]
    Spots = [0,0,0]
    lines = ["Ciag:", str(tab),"\n"]
    Fin.writelines(lines)
    print("Ciag:",tab)
    for i in range(len(tab)): 
        if(i==0):
            print("Zadana strona:", tab[i])
            Spots[0]=tab[0]
            Spots[1]="-"
            Spots[2]="-"
            Numbers[Spots[0]]+=1
            Fault+=1
            FH=1
        if(i==1):
            print("Zadana strona:", tab[i])                 # Z uwagi ze sytuacja poczatka algorytmu dla dowolnego ciagu jest taka sama, pozwolilem sobie zrobic pierwsze trzy zalozenia recznie
            Spots[1]=tab[1]
            Numbers[Spots[0]]+=1
            Numbers[Spots[1]]+=1
            Fault+=1
            FH=1
        if(i==2):
            print("Zadana strona:", tab[i])
            Spots[2]=tab[2]
            Numbers[Spots[0]]+=1
            Numbers[Spots[1]]+=1
            Numbers[Spots[2]]+=1
            Fault+=1
            FH=1
        if(i>2):
            if(Spots[0]==tab[i] or Spots[1]==tab[i] or Spots[2]==tab[i]):           # Warunek czy dana ramka pasuje do jakiejs z dostepnych stron
                print("Zadana strona:", tab[i])
                Hit+=1
                FH=0
            else:
                Fault+=1
                FH=1
                print("Zadana strona:", tab[i])
                for j in range(len(Numbers)):
                    if(max(Numbers)==Numbers[j]):                           # Szukam liczby ktora powtorzyla sie najdawniej
                        if(Spots[0]==j):
                            Spots[0]=tab[i]
                            Numbers[j]=0
                            break
                        elif(Spots[1]==j):
                            Spots[1]=tab[i]
                            Numbers[j]=0
                            break
                        elif(Spots[2]==j):
                            Spots[2]=tab[i]
                            Numbers[j]=0
                            break
            Numbers[Spots[0]]+=1
            Numbers[Spots[1]]+=1
            Numbers[Spots[2]]+=1                                            # Na koncu zawsze dodaje akutalne liczby, w celu przyszlego dowiedzenia sie ktora najdawniej wystapila
            WorkTime+=work[i]

        lines = [str(Spots[0]),str(Spots[1]),str(Spots[2]),"      ",]           
        Fin.writelines(lines)
        print(Spots[0],Spots[1],Spots[2],"      ",end='')                   # Nastepuje wypisanie informacji na temat akturalnych stron
        if(FH==1):
            Fin.writelines("F")
            print("F")
        else:
            Fin.writelines("H")                                     # Nastepuje wypisanie informacji czy dana ramka trafila czy nie
            print("H")
        Fin.writelines("\n")

    lines = ["Czas pracy:",str(WorkTime),"\n"]
    Fin.writelines(lines)
    print("Czas pracy:",WorkTime)
    lines = ["Fault Pages=",str(Fault),"\n"]
    Fin.writelines(lines)
    print("Fault Pages=",Fault)
    lines = ["Hit=",str(Hit),"\n"]                                  # Podsumowanie zgromadzonych informacji
    Fin.writelines(lines)
    print("Hit=",Hit)


def LRU(tab,work):
    WorkTime = 0
    Hit = 0
    Fault = 0
    FH = 0
    Spots = [0,0,0]
    lines = ["Ciag:", str(tab),"\n"]
    Fin.writelines(lines)
    print("Ciag:",tab)
    for i in range(len(tab)): 
        if(i==0):
            print("Zadana strona:", tab[i])
            Spots[0]=tab[0]
            Spots[1]="-"
            Spots[2]="-"
            Fault+=1
            FH=1
        if(i==1):
            print("Zadana strona:", tab[i])                 # Zalozenia analogicznie do algorytmu FIFO
            Spots[1]=tab[1]
            Fault+=1
            FH=1
        if(i==2):
            print("Zadana strona:", tab[i])
            Spots[2]=tab[2]
            Fault+=1
            FH=1
        if(i>2):
            if(Spots[0]==tab[i] or Spots[1]==tab[i] or Spots[2]==tab[i]):               # Warunek czy nasza ramka znajduje sie w juz gotowych stronach czy nie
                print("Zadana strona:", tab[i])
                Hit+=1
                FH=0
            else:
                Fault+=1
                FH=1
                print("Zadana strona:", tab[i])
                if(tab[i-3]==tab[i-1] and i!=3):                # Warunek w przypadku dostania na poczatku takich samych stron
                    if(tab[i-4]==Spots[0]):
                        Spots[0]=tab[i]
                    if(tab[i-4]==Spots[1]):
                        Spots[1]=tab[i]
                    if(tab[i-4]==Spots[2]):
                        Spots[2]=tab[i]
                elif(tab[i-3]==tab[i-1] and i==3):
                    Spots[1]=tab[i]
                else:
                    if(tab[i-3]==Spots[0]):                     # Nadpisanie przez otrzymana strony najdawniej otrzymanej strony
                        Spots[0]=tab[i]
                    if(tab[i-3]==Spots[1]):
                        Spots[1]=tab[i]
                    if(tab[i-3]==Spots[2]):
                        Spots[2]=tab[i]
            WorkTime+=work[i]

        lines = [str(Spots[0]),str(Spots[1]),str(Spots[2]),"      ",]
        Fin.writelines(lines)
        print(Spots[0],Spots[1],Spots[2],"      ",end='')
        if(FH==1):
            Fin.writelines("F")
            print("F")
        else:                                                           # Nastepuje wypisanie informacji czy dana ramka trafila czy nie
            Fin.writelines("H") 
            print("H")
        Fin.writelines("\n")

    lines = ["Czas pracy:",str(WorkTime),"\n"]
    Fin.writelines(lines)
    print("Czas pracy:",WorkTime)
    lines = ["Fault Pages=",str(Fault),"\n"]
    Fin.writelines(lines)                                       # Wypisanie zgromadzonych danych
    print("Fault Pages=",Fault)
    lines = ["Hit=",str(Hit),"\n"]
    Fin.writelines(lines)
    print("Hit=",Hit)


def FCFS(work, times, priority):
    totalWorkTIME=0
    totalWaitTIME=0
    for i in range(len(work)):
        lines = ["Process nr:",str(i+1),"\n"]
        Fin.writelines(lines)
        print("Process nr:",i+1)
        lines = ["Priority:",str(priority[i]),"\n"]
        Fin.writelines(lines)
        print("Priority:",priority[i])                                      # Wypisanie informacji o aktualnym procesie
        lines = ["Arrival time:",str(times[i]),"\n"]
        Fin.writelines(lines)
        print("Arrival time:",times[i])
        lines = ["Work time:",str(work[i]),"\n"]
        Fin.writelines(lines)
        print("Work time:",work[i])
        if(i==0):
            Fin.writelines("Wait time: 0")
            print("Wait time:",0)
        else:
            lines = ["Wait time:",str(work[i-1])]                           # Zgodnie z zalozeniami algorytmu, wyswietlamy pierwszy otrzymany proces
            Fin.writelines(lines)
            print("Wait time:",work[i-1])
            totalWaitTIME+=work[i-1]+times[i]
        Fin.writelines("\n------------------\n")
        print("------------------")
        totalWorkTIME+=work[i]

    lines = ["\n","Total working time:",str(totalWorkTIME),"\n"]
    Fin.writelines(lines)
    print("Total working time:",totalWorkTIME)
    lines = ["Total waiting time:",str(totalWaitTIME),"\n"]
    Fin.writelines(lines)
    print("Total waiting time:",totalWaitTIME)
    lines = ["Average working time:",str(totalWorkTIME/len(work)),"\n"]                 # Wypisanie informacji po zakonczonym cyklu procesow
    Fin.writelines(lines)
    print("Average working time:",totalWorkTIME/len(work))
    lines = ["Average waiting time:",str(totalWaitTIME/len(work)),"\n"]
    Fin.writelines(lines)
    print("Average waiting time:",totalWaitTIME/len(work))
    Fin.writelines("------------------\n")
    print("------------------")


def LCFS(work, times, priority):
    totalWorkTIME=0
    totalWaitTIME=0
    times.sort(reverse=True)                            # Tu nastepuje posortowanie otrzymanej w calosci listy procesow OD KONCA, zgodnie z zalozeniami algorytmu
    for i in range(len(work)):
        lines = ["Process nr:",str(i+1),"\n"]
        Fin.writelines(lines)
        print("Process nr:",i+1)
        lines = ["Priority:",str(priority[i]),"\n"]
        Fin.writelines(lines)
        print("Priority:",priority[i])                                       # Wypisanie informacji o aktualnym procesie
        lines = ["Arrival time:",str(times[i]),"\n"]
        Fin.writelines(lines)
        print("Arrival time:",times[i])
        lines = ["Work time:",str(work[i]),"\n"]
        Fin.writelines(lines)
        print("Work time:",work[i])
        if(i==0):
            Fin.writelines("Wait time: 0")
            print("Wait time:",0)
        else:
            lines = ["Wait time:",str(work[i-1])]                   # Sposob wypisania informacji analogiczny do FCFS, jedynie na odwrot
            Fin.writelines(lines)
            print("Wait time:",work[i-1])
            totalWaitTIME+=work[i-1]+times[i]
        Fin.writelines("\n------------------\n")
        print("------------------")
        totalWorkTIME+=work[i]

    lines = ["\n","Total working time:",str(totalWorkTIME),"\n"]
    Fin.writelines(lines)
    print("Total working time:",totalWorkTIME)
    lines = ["Total waiting time:",str(totalWaitTIME),"\n"]
    Fin.writelines(lines)
    print("Total waiting time:",totalWaitTIME)
    lines = ["Average working time:",str(totalWorkTIME/len(work)),"\n"]                       # Wypisanie informacji po zakonczonym cyklu procesow
    Fin.writelines(lines)
    print("Average working time:",totalWorkTIME/len(work))
    lines = ["Average waiting time:",str(totalWaitTIME/len(work)),"\n"]
    Fin.writelines(lines)
    print("Average waiting time:",totalWaitTIME/len(work))
    Fin.writelines("------------------\n")
    print("------------------")


def SJF(work, times, priority):
    totalWorkTIME=0
    totalWaitTIME=0
    work.sort()                                     # Tu nastepuje posortowanie otrzymanej listy procesow wzgledem czasow ich dzialania
    for i in range(len(work)):
        lines = ["Process nr:",str(i+1),"\n"]
        Fin.writelines(lines)
        print("Process nr:",i+1)
        lines = ["Priority:",str(priority[i]),"\n"]
        Fin.writelines(lines)
        print("Priority:",priority[i])                                               # Wypisanie informacji o aktualnym procesie
        lines = ["Arrival time:",str(times[i]),"\n"]
        Fin.writelines(lines)
        print("Arrival time:",times[i])
        lines = ["Work time:",str(work[i]),"\n"]
        Fin.writelines(lines)
        print("Work time:",work[i])
        if(i==0):
            Fin.writelines("Wait time: 0")
            print("Wait time:",0)
        else:
            lines = ["Wait time:",str(work[i-1])]                   # Posiadajac informacje na temat czasow dzialania, nastepuje wypisanie procesow od najkrotszego do najdluzszego
            Fin.writelines(lines)
            print("Wait time:",work[i-1])
            totalWaitTIME+=work[i-1]+times[i]
        Fin.writelines("\n------------------\n")
        print("------------------")
        totalWorkTIME+=work[i]

    lines = ["\n","Total working time:",str(totalWorkTIME),"\n"]
    Fin.writelines(lines)
    print("Total working time:",totalWorkTIME)
    lines = ["Total waiting time:",str(totalWaitTIME),"\n"]
    Fin.writelines(lines)
    print("Total waiting time:",totalWaitTIME)
    lines = ["Average working time:",str(totalWorkTIME/len(work)),"\n"]                 # Wypisanie informacji po zakonczonym cyklu procesow
    Fin.writelines(lines)
    print("Average working time:",totalWorkTIME/len(work))
    lines = ["Average waiting time:",str(totalWaitTIME/len(work)),"\n"]
    Fin.writelines(lines)
    print("Average waiting time:",totalWaitTIME/len(work))
    Fin.writelines("------------------\n")
    print("------------------")


print("************** Wybierz algorytm **************")
print("                    1. FIFO")
print("                    2. LRU")
print("                    3. FCFS")
print("                    4. LCFS")
print("                    5. SJF")
print("                    6. Eksperyment z pliku")                     # Gotowy plik z przygotowanymi danymi jest analizowany przez oskryptowany proces
print("                    0. Exit")
print("**********************************************")
x=int(input())
if(x==1):
    if(Choice()):
        FIFO(Generator(10,1),Generator(10,4))
    else:
        x=int(input("Wpisz dlugosc ciagu odwolan: "))
        y=int(input("Wpisz sredni czas pracy jaki przypada na proces: "))
        z=int(input("Wpisz odchylenie standardowe od tego czasu: "))
        FIFO(Generator(x,1,0,40,y,z),Generator(x,4,0,40,y,z))
elif(x==2):
    if(Choice()):
        LRU(Generator(10,1),Generator(10,4))
    else:
        x=int(input("Wpisz dlugosc ciagu odwolan: "))
        y=int(input("Wpisz sredni czas pracy jaki przypada na proces: "))
        z=int(input("Wpisz odchylenie standardowe od tego czasu: "))
        LRU(Generator(x,1,0,40,y,z),Generator(x,4,0,40,y,z))
elif(x==3):
    if(Choice()):
        FCFS(Generator(10,4),Generator(10,2),Generator(10,3))
    else:
        x=int(input("Wpisz ilosc przywolywanych procesow: "))
        y1=int(input("Wpisz minimalna wartosc czasu przyjscia: "))
        z1=int(input("Wpisz maksymalna wartosc czasu przyjscia: "))
        y=int(input("Wpisz sredni czas pracy jaki przypada na proces: "))
        z=int(input("Wpisz odchylenie standardowe od tego czasu: "))
        FCFS(Generator(x,4,y1,z1,y,z),Generator(x,2,y1,z1,y,z),Generator(x,3,y1,z1,y,z))
elif(x==4):
    if(Choice()):
        LCFS(Generator(10,4),Generator(10,2),Generator(10,3))
    else:
        x=int(input("Wpisz ilosc przywolywanych procesow: "))
        y1=int(input("Wpisz minimalna wartosc czasu przyjscia: "))
        z1=int(input("Wpisz maksymalna wartosc czasu przyjscia: "))
        y=int(input("Wpisz sredni czas pracy jaki przypada na proces: "))
        z=int(input("Wpisz odchylenie standardowe od tego czasu: "))
        LCFS(Generator(x,4,y1,z1,y,z),Generator(x,2,y1,z1,y,z),Generator(x,3,y1,z1,y,z))
elif(x==5):
    if(Choice()):
        SJF(Generator(10,4),Generator(10,2),Generator(10,3))
    else:
        x=int(input("Wpisz ilosc przywolywanych procesow: "))
        y1=int(input("Wpisz minimalna wartosc czasu przyjscia: "))
        z1=int(input("Wpisz maksymalna wartosc czasu przyjscia: "))
        y=int(input("Wpisz sredni czas pracy jaki przypada na proces: "))
        z=int(input("Wpisz odchylenie standardowe od tego czasu: "))
        SJF(Generator(x,4,y1,z1,y,z),Generator(x,2,y1,z1,y,z),Generator(x,3,y1,z1,y,z))
elif(x==6):
    tab = []
    tab2 = []
    other = []
    other2 = []
    for i in range(10):
        tab.append(int(Fout.readline()))
    for i in range(10):
        tab2.append(int(Fout.readline()))
    for i in range(100):
        other.append(int(Fout.readline()))
    for i in range(100):
        other2.append(int(Fout.readline()))

    Fin.writelines("Eksperyment algorytmu FIFO z dlugoscia ciagu 10 oraz czasem pracy 20 z odchyleniem standardowym 5\n")
    print("Eksperyment algorytmu FIFO z dlugoscia ciagu 10 oraz czasem pracy 20 z odchyleniem standardowym 5")
    FIFO(tab,tab2)
    Fin.writelines("\nEksperyment algorytmu LRU z dlugoscia ciagu 10 oraz czasem pracy 20 z odchyleniem standardowym 5\n")
    print("Eksperyment algorytmu LRU z dlugoscia ciagu 10 oraz czasem pracy 20 z odchyleniem standardowym 5")
    LRU(tab, tab2)
    Fin.writelines("\nEksperyment algorytmu FCFS 100 procesow, z czasem przyjscia o zakresie 0-100 oraz czasem pracy 20 z odchyleniem standardowym 5\n")
    print("Eksperyment algorytmu FCFS 100 procesow, z czasem przyjscia o zakresie 0-100 oraz czasem pracy 20 z odchyleniem standardowym 5")
    FCFS(other,other2,Generator(100,3))
    Fin.writelines("\nEksperyment algorytmu LCFS 100 procesow, z czasem przyjscia o zakresie 0-100 oraz czasem pracy 20 z odchyleniem standardowym 5\n")
    print("Eksperyment algorytmu LCFS 100 procesow, z czasem przyjscia o zakresie 0-100 oraz czasem pracy 20 z odchyleniem standardowym 5")
    LCFS(other,other2,Generator(100,3))
    Fin.writelines("\nEksperyment algorytmu SJF 100 procesow, z czasem przyjscia o zakresie 0-100 oraz czasem pracy 20 z odchyleniem standardowym 5\n")
    print("Eksperyment algorytmu SJF 100 procesow, z czasem przyjscia o zakresie 0-100 oraz czasem pracy 20 z odchyleniem standardowym 5")
    SJF(other,other2,Generator(100,3))
else:
    exit(0)

Fin.close()
Fout.close()