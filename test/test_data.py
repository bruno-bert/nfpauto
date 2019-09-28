from datetime import date, datetime

DIA_EXPIRA = 20

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

 
if __name__ == "__main__":
    test_data1("1909") 