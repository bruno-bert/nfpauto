from calendar import monthrange
from datetime import date, datetime, timedelta

DIA_EXPIRA = 20

def monthdelta(d1, d2):
    delta = 0
    while True:
        mdays = monthrange(d1.year, d1.month)[1]
        d1 += timedelta(days=mdays)
        if d1 <= d2:
            delta += 1
        else:
            break
    return delta



def verifica_data_expirada(data): 
 today = date.today() 
 print("today =", today) 
 data_hoje = today.strftime("%d/%m/%Y")
 print("data_hoje =", data_hoje)

 sub_ano = str(today.year)[0:2]
 print("sub_ano = {}".format(sub_ano))

 ano = data[0:2]
 mes = data[2:4]
 dia = 1
 print("ano = {}".format(sub_ano + ano))
 print("mes = {}".format(mes))
 data_nota = date(year = int(sub_ano + ano), month = int(mes), day = dia)
 data_nota = data_nota.strftime("%d/%m/%Y")
 print("data_nota = {}".format(data_nota))
 delta = monthdelta(datetime.strptime(data_nota,"%d/%m/%Y"), datetime.strptime(data_hoje,"%d/%m/%Y"))
 print("Delta is {}".format(delta))
 
 if (delta <= 1):
    if (delta == 0):
        return False
    else:
        #delta = 1
        if (today.day<=DIA_EXPIRA):
            return False
        else:
            return True          
 else:
    return True     


if __name__ == "__main__":
    result = verifica_data_expirada("1908") 
    print("result: {}".format(result))
    print("Expirada" if result else "OK")