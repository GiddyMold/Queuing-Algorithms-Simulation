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