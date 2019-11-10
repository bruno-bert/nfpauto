from PyQt5.QtCore import QThread, pyqtSignal
from service_posting import NFPPosting
from database import  busca_script_padrao, busca_chaves_por_status, busca_cnpj_padrao_valor, busca_cnpj_padrao
from subscriberqt import QtSubscriber
from seleniumdb.cycle_result import CycleResult 

import time

class Log:
    def __init__(self, message, manual_action = 0 ):
        self.message = message 
        #print('no construtor log:{}'.format(str(manual_action)))
        self.manual_action = manual_action

class Task(QtSubscriber):

    sig_log = pyqtSignal(Log)
    sig_result = pyqtSignal(CycleResult)
    sig_chave = pyqtSignal(str)

    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.service = None
        self.cancelar = 0
    
    #listener
    def show_log(self, message, manual_action = 0):
        self.sig_log.emit(Log(message, manual_action))
    

    #listener
    def save_result(self, result):
        print('emitindo chave' + result.value)
        self.sig_result.emit(result)

    
    #listener
    def init_value(self, value):
        self.sig_chave.emit(value)

    def cancel_posting(self, cancelar):
        self.cancelar = cancelar
        if (cancelar == 1):
          self.service.flag_cancelar = 1
          self.sig_log.emit(Log('Postagem Cancelada'))

  

    def run(self):
        script_id = self.get_script_id() 
        chaves = self.seleciona_chaves()

        
        row = busca_cnpj_padrao()
        
        row = dict(row)
        cnpj = row['cnpj']    
        descricao_entidade = row['descricao']    
        palavras = row['palavras']   

        self.service = NFPPosting(script_id, cnpj, descricao_entidade, palavras, chaves)
        self.service.register(self)
        self.service.iniciar_postagem()


    def get_script_id(self):      
      result = busca_script_padrao()
      return int(result['script_id'])

    def seleciona_chaves(self):
      rows = busca_chaves_por_status(1)
      return [col['chave'] for col in rows]
            

 
       