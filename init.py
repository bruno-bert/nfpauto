from seleniumdb.core import SeleniumDB
from seleniumdb.models import Step

class NFPPosting(SeleniumDB):

    def __init__(self, script_id, cnpj, descricao_entidade, chaves):      
      super().__init__(script_id)

      self.cnpj = cnpj
      self.descricao_entidade = descricao_entidade
      self.chaves = chaves

    def log(self, message):
        print(message)

   
    def iniciar_postagem(self):

      #pega primeira step 
      index = 0
      step = Step()      
      step = self.lista_steps[index]
      step_id = step.step_id
      steps_to_skip_on_next_run = None

      values_on_expression =  { "descricao_entidade": self.descricao_entidade }    
      
      for chave in self.chaves:        
        
        values = { "chave": chave, "cnpj": self.cnpj}      
        run_result = self.run_steps(values, values_on_expression, step_id, steps_to_skip_on_next_run)

        # com base no retorno do ciclo anterior, 
        # determina o step inicial e se precisa pular algum step no ciclo seguinte
        step_id = run_result['step_id']
        steps_to_skip_on_next_run = run_result['steps_to_skip_on_next_run']

      self.show_results()  
      self.quit_browser()

def get_script_id():      
      return 2

def seleciona_chaves():
   return ['35191007424394000154590005988310737378424829',
           '22222222222222222222222222222222222222222222',
           '33333333333333333333333333333333333333333333']

def seleciona_cnpj():
   return '01.146.603/0001-69'

def seleciona_descricao_entidade():
   return "GACC GRUPO DE ASSISTENCIA A CRIANCA COM CANCER"     

   
if __name__ == "__main__":
   
  script_id = get_script_id() 
  chaves = seleciona_chaves()
  cnpj = seleciona_cnpj()
  descricao_entidade = seleciona_descricao_entidade()
  service = NFPPosting(script_id, cnpj, descricao_entidade, chaves)
  service.iniciar_postagem()


