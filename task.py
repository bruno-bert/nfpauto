from PyQt5.QtCore import QThread, pyqtSignal
from service_posting import NFPPosting
from database import  busca_script_padrao, busca_chaves_banco
from subscriberqt import QtSubscriber

class Task(QtSubscriber):

    sig_log = pyqtSignal(str)
    sig_result = pyqtSignal(str)

    def __init__(self, parent=None):
        QThread.__init__(self, parent)
    
    def show_log(self, message):
        self.sig_log.emit(message)
    
    def save_result(self, result):
      #TODO - atualiza status da nota no banco, de acordo com o retorno do resultado da postagem 
       self.sig_result.emit(result.value)

    def run(self):
        script_id = self.get_script_id() 
        chaves = self.seleciona_chaves()
        cnpj = self.seleciona_cnpj()
        descricao_entidade = self.seleciona_descricao_entidade()
        service = NFPPosting(script_id, cnpj, descricao_entidade, chaves)
        service.register(self)
        service.iniciar_postagem()


    def get_script_id(self):      
      result = busca_script_padrao()
      return int(result['script_id'])

    def seleciona_chaves(self):
      rows = busca_chaves_banco()
      return [col[1] for col in rows]
            

    def seleciona_cnpj(self):
      return '01.146.603/0001-69'

    def seleciona_descricao_entidade(self):
      return "GACC GRUPO DE ASSISTENCIA A CRIANCA COM CANCER"     

       