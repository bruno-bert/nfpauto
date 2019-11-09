from seleniumdb.core import SeleniumDB
from seleniumdb.models import Step


class NFPPosting(SeleniumDB):

    def __init__(self, script_id, cnpj, descricao_entidade, palavras, chaves):      
      super().__init__(script_id)

      self.cnpj = cnpj
      self.descricao_entidade = descricao_entidade
      self.palavras = palavras
      self.chaves = chaves
      

    def log(self, message, manual_action = 0):
      print(message + ' - ' + str(manual_action))
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
      
      for chave in self.chaves:        
        
        try:

          if (self.flag_cancelar == 1):           
            break

          #trigger for external listeners  
          self.init_value(chave)

          values = { "chave": chave, "cnpj": self.cnpj}      
          run_result = self.run_steps(values, values_on_expression, step_id, steps_to_skip_on_next_run)


          # com base no retorno do ciclo anterior, 
          # determina o step inicial e se precisa pular algum step no ciclo seguinte
          step_id = run_result['step_id']
          steps_to_skip_on_next_run = run_result['steps_to_skip_on_next_run']
        except Exception as err:
          print(err)
     
      self.quit_browser()





