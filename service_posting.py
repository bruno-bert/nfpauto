from seleniumdb.core import SeleniumDB
from seleniumdb.models import Step
from database import   busca_chaves_por_status
import time

class NFPPosting(SeleniumDB):
     
    def seleciona_chaves(self):
      rows = busca_chaves_por_status(1)
      return [col['chave'] for col in rows]
            

    def __init__(self, script_id, cnpj, descricao_entidade, palavras):      
      super().__init__(script_id)

      self.cnpj = cnpj
      self.descricao_entidade = descricao_entidade
      self.palavras = palavras
    
    def log(self, message, manual_action = 0):
      self.show_log(message, manual_action)
    
    def on_save_result(self, result): 
      self.save_result(result)
      
   

    def get_id_to_show(self, values ):
      return 'CNPJ: {} - Chave de Acesso: {}'.format(values['cnpj'],values['chave'])
    
    def get_id(self, values ):
      return values['chave']
    
    

    def iniciar_postagem(self):

      #pega primeira step 
      index = 0
      step = Step()      
      step = self.lista_steps[index]
      step_id = step.step_id
      steps_to_skip_on_next_run = None
      self.flag_cancelar = 0 
      values_on_expression =  { "descricao_entidade": self.descricao_entidade }    
      driver = None
      
      while True:
        
        chaves = self.seleciona_chaves()

        if (len(chaves) == 0 ) :
          self.log("Neste momento, não há mais notas pendentes de postagem no site", 1)

        if (self.flag_cancelar == 1):  
            if (driver): 
              driver.maximize_window()
              driver.set_window_position(0,0)        
            break
        
        for chave in chaves:        
          
          try:

            if (self.flag_cancelar == 1):   
              if (driver):
                driver.maximize_window()
                driver.set_window_position(0,0)          
              break
            
            #trigger for external listeners  
            self.init_value(chave)

            values = { "chave": chave, "cnpj": self.cnpj}      
            run_result = self.run_steps(values, values_on_expression, step_id, steps_to_skip_on_next_run)
            driver = run_result['driver']

            # com base no retorno do ciclo anterior, 
            # determina o step inicial e se precisa pular algum step no ciclo seguinte
            step_id = run_result['step_id']
            steps_to_skip_on_next_run = run_result['steps_to_skip_on_next_run']
          except Exception as err:
            print(err)
     
        time.sleep(5) 



