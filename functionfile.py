
from fnmatch import fnmatch

def chance(snils):
    otvet=""
    f=open('sfubase1.csv',encoding="cp866")
    fnew=[]
    for i in f:
        fnew.append(list(map(str, i.split(";"))))
    f=fnew

    def garant(snils,priority):
        for i in f:
            if priority=="1":
                return False
            if fnmatch(i[0][:8],"??.??.??")==True:
                mest=int(i[0].split()[-1])

            if i[1]==snils:
                if i[13]!="" and priority!="":
                    if int(i[13])<int(priority):
                        if int(i[0])<mest:
                            return True
        return False


    s=0
    lohi=0
    priority=0
    kolvopidorov=0
    pidor=[]
    napr=0
    for i in f:
        s+=1
        if fnmatch(i[0][:8],"??.??.??")==True:
            name=i[0]
            priority=0
            lohi=0
            nadoli=False
            pidor=[]
            kolvopidorov=0

        else:
            if i[1]==snils:
                napr+=1
                otvet+=("<b>"+str(name)+"</b>"+"\n")
                otvet+="бюджетных мест: "+str(int(name.split()[-1]))+"\n"
                otvet+="моё место: " + i[0]+"\n"
                mymesto=int(i[0])
                otvet+="людей с первым приоритетом передо мной: " + str(priority) +"\n"
                for i in pidor:
                    if garant(i[0],i[1])==True:
                        kolvopidorov+=1
                otvet+="------------"+"\n"
                otvet+="Люди передо мной, которые гарантированно поступят не сюда: " + str(kolvopidorov) + "\n"
                itog=mymesto-kolvopidorov
                if itog<=int(name.split()[-1]):
                    otvet+=f"Итоговое место: {itog} - <b>Точно поступил</b>✅"+"\n"
                else:
                    otvet+=f"Итоговое место: {itog} - Пока не поступил "+"\n"
                otvet+="------------------------"+"\n"
                otvet+="\n"
                nadoli=True
                if napr>=5:
                    break
            else:
                if i[13]=="1":
                    priority+=1
                pidor.append((i[1],i[-3]))
    return(otvet)