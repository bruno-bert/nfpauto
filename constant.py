ENV="DEV"
TEST_USER="test@test.com"
TEST_PASSWORD="test"

NUM_CHAVE=44
DEFAULT_STATUS="1"
EMPTY_STR=""

QUERY_SAVE="INSERT INTO notas (chave, cnpj, data, uf, numero, codigo, modelo, serie, tipo_emissao, status, message)  VALUES (?,?,?,?,?,?,?,?,?,?,?)"
QUERY_SAVE_CNPJ="INSERT INTO cnpj (cnpj, uf, modelo, serie)  VALUES (?,?,?,?)"
QUERY_INSERT_CNPJ_PADRAO="INSERT INTO cnpj_padrao ('cnpj') VALUES ('{}')"
QUERY_UPDATE_CNPJ_PADRAO="UPDATE cnpj_padrao set cnpj='{}'"
QUERY_SELECT_CNPJ_PADRAO="select cnpj from cnpj_padrao"
QUERY_SELECT_CONFIG_ARQUIVO="select * from config_arquivo where id_text = '{}'"
QUERY_SELECT_CONFIG_ARQUIVO_PADRAO="select id_text from config_arquivo_padrao"
QUERY_SELECT_SCRIPTS="select * from scripts"
QUERY_SELECT_SCRIPT_PADRAO="select script_id from script_padrao"
QUERY_UPDATE_STATUS_NOTA="UPDATE notas set status = {} where chave = '{}'"
QUERY_UPDATE_STATUS_MESSAGE_NOTA="UPDATE notas set status = {}, message = '{}' where chave = '{}'"

VALIDA_CHAVE_PELO_DIGITO=True
SALVA_NOTA_EXPIRADA=True
LIMPA_CAMPO_QUANDO_INVALIDA=False
MESES_EXPIRACAO=1
DIA_EXPIRA=20
DEFAULT_NUMERO_NOTAS=50
MAX_NOTAS=100
MIN_NOTAS=1
SALVA_CNPJ=True
TITULO_DIALOG_ARQUIVO="Selecionar arquivo"



MESES=('Janeiro','Fevereiro','Mar','Abril','Maio','Junho',
           'Julho','Agosto','Setembro','Outubro','Novembro','Dezembro')



#FEATURE_FLAGS
VALIDA_CNPJ=True

#dev constants
INICIA_DB_INICIO=False
IMPORTA_PADRAO="TEXT_PADRAO" #id da configuracao do config_arquivo - usado na importacao do arquivo massivo

#chaves de acesso - exemplos
#35190828408897000106590004726960913876503564
#42100484684182000157550010000000020108042108
#35190903776210000407590001563141522384821761

#01563141522384821761