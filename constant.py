NUM_CHAVE=44
DEFAULT_STATUS="1"
EMPTY_STR=""
QUERY_SAVE="INSERT INTO notas (chave, cnpj, data, uf, numero, codigo, modelo, serie, tipo_emissao, status, message)  VALUES (?,?,?,?,?,?,?,?,?,?,?)"
QUERY_SAVE_CNPJ="INSERT INTO cnpj (cnpj, uf, modelo, serie)  VALUES (?,?,?,?)"
VALIDA_CHAVE_PELO_DIGITO=True
SALVA_NOTA_EXPIRADA=True
LIMPA_CAMPO_QUANDO_INVALIDA=False
MESES_EXPIRACAO=1
DIA_EXPIRA=20
SALVA_CNPJ=True
TITULO_DIALOG_ARQUIVO="Selecionar arquivo"

MESES=('Janeiro','Fevereiro','Mar','Abril','Maio','Junho',
           'Julho','Agosto','Setembro','Outubro','Novembro','Dezembro')


#dev constants
INICIA_DB_INICIO=False

#chaves de acesso - exemplos
#35190928408897000106590004726960913876503564
#42100484684182000157550010000000020108042108
#35190903776210000407590001563141522384821761

#01563141522384821761