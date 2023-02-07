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