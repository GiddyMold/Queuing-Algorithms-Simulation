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