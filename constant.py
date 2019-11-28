ENV="DEV"
TEST_USER="test@test.com"
TEST_PASSWORD="test"

NUM_CHAVE=44
DEFAULT_STATUS="Postagem Pendente"
DEFAULT_STATUS_CODIGO=1
EMPTY_STR=""

EMITIR_SOM_ERRO=True
EMITIR_SOM_SUCESSO=True
SOM_ERRO_FILE="assets/sounds/error.mp3"
SOM_SUCESSO_FILE="assets/sounds/success.mp3"

QUERY_SELECT_NOTAS_STATS_COLETADAS_HOJE="select status, count(chave) as contador from notas where date(datahora) = date('now') group by status"
QUERY_SELECT_NOTAS_STATS_POSTADAS_HOJE="select status, count(chave) as contador from notas where date(datapostagem) = date('now') group by status"
QUERY_SELECT_NOTAS_STATS_POSTADAS_TOTAL="select status, count(chave) as contador from notas group by status"
QUERY_SELECT_MESSAGES_RETRY="select * from messages_retry"
QUERY_SELECT_NOTAS_PRINCIPAL="select datapostagem, datahora, x.id as id, chave, cnpj, data, uf, numero, modelo, serie, x.codigo as codigo, tipo_emissao,descricao as status, valor, message, cnpj_entidade from notas x, status y where x.status = y.codigo ORDER BY datahora DESC"
QUERY_SELECT_NOTAS_PRINCIPAL_POR_STATUS="select datapostagem, datahora, x.id as id, chave, cnpj, data, uf, numero, modelo, serie, x.codigo as codigo, tipo_emissao,descricao as status, valor, message, cnpj_entidade from notas x, status y where x.status = y.codigo and x.status = {}  ORDER BY datahora {}"
QUERY_LISTA_STATUS="select * from status"
QUERY_LISTA_UF="select * from uf"
QUERY_DELETA_NOTAS_PROCESSADAS="DELETE FROM notas WHERE status IN (2, 3)"
QUERY_SAVE="INSERT INTO notas (chave, cnpj, data, uf, numero, codigo, modelo, serie, tipo_emissao, status, message, datahora, origem)  VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"
QUERY_SAVE_CNPJ="INSERT INTO cnpj (cnpj, uf, modelo, serie)  VALUES (?,?,?,?)"
QUERY_INSERT_CNPJ_PADRAO="INSERT INTO cnpj_padrao ('cnpj','descricao','palavras') VALUES ('{}','{}','{}')"
QUERY_UPDATE_CNPJ_PADRAO="UPDATE cnpj_padrao set cnpj='{}', descricao='{}', palavras = '{}'"
QUERY_SELECT_CNPJ_PADRAO="select cnpj, descricao, palavras from cnpj_padrao"
QUERY_SELECT_CONFIG_ARQUIVO="select * from config_arquivo where id_text = '{}'"
QUERY_SELECT_CONFIG_ARQUIVO_PADRAO="select id_text from config_arquivo_padrao"
QUERY_SELECT_SCRIPTS="select * from scripts"
QUERY_SELECT_SCRIPT_PADRAO="select script_id from script_padrao"
QUERY_UPDATE_STATUS_NOTA="UPDATE notas set status = {} where chave = '{}'"
QUERY_UPDATE_STATUS_MESSAGE_NOTA="UPDATE notas set status = {}, message = '{}', datapostagem = '{}', cnpj_entidade = '{}' where chave = '{}'"
DATABASE_FILE="notas.db"

ORIGEM_NOTA_MANUAL=1
ORIGEM_NOTA_DIGITAR=2
ORIGEM_NOTA_IMPORTA=3
ORIGEM_NOTA_XML=4
ORIGEM_NOTA_PORTAL=5
ORIGEM_NOTA_VIDEO=6

VALIDA_CHAVE_PELO_DIGITO=True
SALVA_NOTA_EXPIRADA=False
LIMPA_CAMPO_QUANDO_INVALIDA=True
MESES_EXPIRACAO=1
DIA_EXPIRA=20
DEFAULT_NUMERO_NOTAS=50
MAX_NOTAS=100
MIN_NOTAS=1
SALVA_CNPJ=True
TITULO_DIALOG_ARQUIVO="Selecionar arquivo"



MESES=('Janeiro','Fevereiro','Mar','Abril','Maio','Junho',
           'Julho','Agosto','Setembro','Outubro','Novembro','Dezembro')


STYLES_FILE="styles/main.css"
STYLES_FILE_BUTTONS="styles/button.css"
STYLES_FILE_BUTTONS_ALERT="styles/button_alert.css"

STYLES_FILE_TAB_STOPPED="styles/tab_stopped.css"
STYLES_FILE_TAB_PROGRESS="styles/tab_progress.css"
STYLES_FILE_TAB_ALERT="styles/tab_alert.css"

#FEATURE_FLAGS
VALIDA_CNPJ=True

#dev constants
IMPORTA_PADRAO="TEXT_PADRAO" #id da configuracao do config_arquivo - usado na importacao do arquivo massivo
