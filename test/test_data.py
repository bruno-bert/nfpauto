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



def test_data1(data): 
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
 
if __name__ == "__main__":
    test_data1("1908") 