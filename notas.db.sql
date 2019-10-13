BEGIN TRANSACTION;
DROP TABLE IF EXISTS "steps";
CREATE TABLE IF NOT EXISTS "steps" (
	"id"	INTEGER,
	"script_id"	INTEGER,
	"step_id"	INTEGER,
	"step_name"	TEXT,
	"step_description"	TEXT,
	"sort_number"	INTEGER DEFAULT 0,
	"skip"	TEXT DEFAULT '0',
	"on_success_goto"	INTEGER DEFAULT 0,
	"on_error_goto"	INTEGER DEFAULT 0,
	"find_method"	TEXT,
	"expression"	TEXT,
	"action"	TEXT,
	"text_to_type"	TEXT,
	"check_session"	TEXT DEFAULT '1',
	"is_check_session_timeout"	TEXT DEFAULT '0',
	"session_timeout__step_id"	INTEGER,
	"on_session_timeout_start_from"	INTEGER,
	"base_element"	TEXT,
	"element_from_step"	INTEGER,
	"error_message_finder"	TEXT,
	"success_message_finder"	TEXT,
	"must_wait_element"	TEXT DEFAULT '1',
	"timeout_to_element"	INTEGER,
	"log_message_before"	TEXT,
	"log_message_after"	TEXT,
	"wait_manual_action"	TEXT DEFAULT '0',
	"steps_to_skip_on_next_run"	TEXT,
	PRIMARY KEY("id"),
	CONSTRAINT "fk_script" FOREIGN KEY("script_id") REFERENCES "scripts"("id") ON DELETE CASCADE
);
DROP TABLE IF EXISTS "scripts";
CREATE TABLE IF NOT EXISTS "scripts" (
	"id"	INTEGER,
	"name"	TEXT,
	"description"	TEXT,
	"version"	TEXT DEFAULT '1',
	"status"	TEXT DEFAULT '0',
	"delete_on_sync"	TEXT DEFAULT '0',
	PRIMARY KEY("id")
);
DROP TABLE IF EXISTS "config_arquivo_padrao";
CREATE TABLE IF NOT EXISTS "config_arquivo_padrao" (
	"id"	INTEGER,
	"id_text"	TEXT,
	PRIMARY KEY("id")
);
DROP TABLE IF EXISTS "config_arquivo";
CREATE TABLE IF NOT EXISTS "config_arquivo" (
	"id"	INTEGER,
	"cnpj"	TEXT,
	"id_text"	TEXT,
	"nome"	TEXT,
	"delimitador"	TEXT,
	"tipo"	TEXT,
	"coluna"	INTEGER,
	"nome_coluna"	TEXT,
	"header"	TEXT,
	"sheet_name"	TEXT,
	PRIMARY KEY("id")
);
DROP TABLE IF EXISTS "cnpj_padrao";
CREATE TABLE IF NOT EXISTS "cnpj_padrao" (
	"id"	INTEGER,
	"cnpj"	TEXT,
	PRIMARY KEY("id")
);
DROP TABLE IF EXISTS "cnpj";
CREATE TABLE IF NOT EXISTS "cnpj" (
	"id"	INTEGER,
	"cnpj"	TEXT,
	"empresa"	TEXT,
	"uf"	TEXT,
	"modelo"	TEXT,
	"serie"	TEXT,
	PRIMARY KEY("id")
);
DROP TABLE IF EXISTS "notas";
CREATE TABLE IF NOT EXISTS "notas" (
	"id"	INTEGER,
	"chave"	TEXT,
	"cnpj"	TEXT,
	"data"	TEXT,
	"uf"	TEXT,
	"numero"	TEXT,
	"modelo"	TEXT,
	"serie"	TEXT,
	"tipo_emissao"	TEXT,
	"codigo"	TEXT,
	"status"	TEXT,
	"valor"	REAL,
	"message"	TEXT,
	PRIMARY KEY("id")
);
INSERT INTO "steps" ("id","script_id","step_id","step_name","step_description","sort_number","skip","on_success_goto","on_error_goto","find_method","expression","action","text_to_type","check_session","is_check_session_timeout","session_timeout__step_id","on_session_timeout_start_from","base_element","element_from_step","error_message_finder","success_message_finder","must_wait_element","timeout_to_element","log_message_before","log_message_after","wait_manual_action","steps_to_skip_on_next_run") VALUES (1,1,1,'click elemento Aviso Inicial','quando encontrar elemento aviso, significa que fez o login',10,'0',0,2,'name','ctl00$ConteudoPagina$btnContinuar','click',NULL,'1','0',NULL,0,NULL,NULL,NULL,NULL,'1',200000000,'procutando botão de aviso inicial','botão de aviso clickado','0',NULL),
 (2,1,2,'click elemento Entidades','busca e clica no menu Entidades',20,'0',0,-1,'xpath','//a[contains(text(), ''Entidades'')]','click',NULL,'1','0',NULL,0,NULL,NULL,NULL,NULL,'1',3,'procurando menu Entidades','menu entidades clickado','0',NULL),
 (3,1,3,'click elemento Cupons sem CPF','clica no segundo nivel do menu - cupons sem cpf',30,'0',0,0,'xpath','//a[@href=''/EntidadesFilantropicas/DoacaoNotasListagem.aspx'']','click',NULL,'1','0',NULL,0,NULL,NULL,NULL,NULL,'1',3,'procurando menu Cadastro Cupom sem CPF','menu Cupom sem cpf clickado','0',NULL),
 (4,1,4,'click elemento botão Nova Doação','clicka no botão Nova Doação',40,'0',0,2,'id','btnNovaDoacao','click',NULL,'1','0',NULL,0,NULL,NULL,NULL,NULL,'1',3,'procurando botão de nova doação','botão nova doação clickado','0','none'),
 (5,1,5,'busca elemento popup','procura por elemento de popup de aviso',50,'0',0,7,'xpath','//div[@aria-labelledby=''ui-dialog-title-divPerguntaMaster'']','find',NULL,'1','0',NULL,0,NULL,NULL,NULL,NULL,'1',3,'procurando popup de mensagem inicial','popup de mensagem inicial encontrado','0',NULL),
 (6,1,6,'busca botão SIM no popup','procura por botão sim no popup e clicka nele',60,'0',0,7,'xpath','.//span[contains(text(), ''Sim'')]','click',NULL,'1','0',NULL,0,'other_step',6,NULL,NULL,'1',2,'procurando botão SIM no ppup','botão SIM encontrado e clickado','0',NULL),
 (7,1,7,'busca formulário de dados','procura pelo formulário de dados',70,'0',0,0,'id','divDados','find',NULL,'1','0',NULL,0,NULL,NULL,NULL,NULL,'0',0,'procurando formulário principal de dados','formulário encontrado','0',NULL),
 (8,1,8,'busca formulário da chave de acesso','procura pelo formulário específico da chave de acesso dentro do formulário principal',80,'0',0,0,'id','divDocComChave','find',NULL,'1','0',NULL,0,'other_step',7,NULL,NULL,'0',0,'procurando formulário específico da chave de acesso','formulário da chave de acesso encontrado','0',NULL),
 (9,1,9,'busca input da chave de acesso','procura input da chave de acesso e digita chave',90,'0',0,0,'xpath','//span[contains(text(), ''Chave-de-acesso'')]/following-sibling::input','type','{chave}','1','0',NULL,0,'other_step',8,NULL,NULL,'0',0,'procurando input da chave de acesso','input da chave de acesso encontrado e chave digitada','0',NULL),
 (10,1,10,'busca input do cnpj','procura input do cnpj da instituição e digita',100,'0',0,0,'name','ctl00$ConteudoPagina$entiFilantropica$txtCNPJEntidade','type','{cnpj}','1','0',NULL,0,NULL,NULL,NULL,NULL,'0',0,'procurando input do cnpj da instituição','input da instituição encontrado e digitado','0',NULL),
 (11,1,11,'busca botão de busca de instituição pelo cnpj','procura botão de busca de instituição por meio do cnpj e clicka nele',110,'0',0,0,'name','ctl00$ConteudoPagina$entiFilantropica$btnBuscar','click',NULL,'1','0',NULL,0,NULL,NULL,NULL,NULL,'0',0,'procurando botão de busca do cnpj','botão de busca por cnj encontrado e clickado','0',NULL),
 (12,1,12,'busca input de seleção da entidade','procura checkbox da entidade encontrada e clicka no primeiro',120,'0',0,0,'name','ctl00$ConteudoPagina$entiFilantropica$gdvConsultaEntidades$ctl02$rdbSelecao','click',NULL,'1','0',NULL,0,NULL,NULL,NULL,NULL,'1',5,'procurando input de seleção da entidade','input da entidade encontrado e selecionado','0',NULL),
 (13,1,13,'busca botão de salvar','procura botão de salvar para confirmar a doação',130,'0',0,0,'name','ctl00$ConteudoPagina$btnSalvarNota','click',NULL,'1','0',NULL,0,NULL,NULL,NULL,NULL,'0',0,'procurando botão de salvar nota','botão de salvar encontrado e clickado','0',NULL),
 (14,1,14,'busca mensagem de erro no resultado','procura mensagem de erro',140,'0',0,17,'xpath','//div[@aria-labelledby=''ui-dialog-title-divErroMaster'']','find',NULL,'1','0',NULL,0,NULL,NULL,NULL,NULL,'1',3,'procurando mensagem de erro','mensagem de erro encontrada','0',NULL),
 (15,1,15,'busca label com mensagem de erro','procura a mensagem de erro dentro do popup e mostra',150,'0',0,17,'id','lblErroMaster','show',NULL,'1','0',NULL,0,'other_step',14,NULL,NULL,'0',0,'procurando mensagem de erro','mensagem de erro encontrada e exibida','0',NULL),
 (16,1,16,'busca botão de ok no erro','procura botão de ok na mensagem de erro e clicka',160,'0',7,17,'xpath','.//span[contains(text(), ''Ok'')]','click',NULL,'1','0',NULL,0,'other_step',14,NULL,NULL,'0',0,'procurando botão de confirmacao do erro','botão de ok do erro encontrado e clickado','0','10|11|12'),
 (17,1,17,'busca mensagem de sucesso no resultado','procura mensagem de sucesso',170,'0',0,2,'xpath','//div[@aria-labelledby=''ui-dialog-title-divPerguntaMaster'']','find',NULL,'1','0',NULL,0,NULL,NULL,NULL,NULL,'1',3,'procurando mensagem de sucesso','mensagem de sucesso encontrada','0','none'),
 (18,1,18,'busca label com mensagem de sucesso','procura a mensagem de sucesso dentro do popup e mostra',180,'0',0,2,'id','lblPerguntaMaster','show',NULL,'1','0',NULL,0,'other_step',17,NULL,NULL,'0',0,'procurando mensagem de sucesso','mensagem de sucesso encontrada e exibida com sucesso','0',NULL),
 (19,1,19,'busca notão de NÃO na mensagem de sucesso','procura e clicka no botão NÃO na mensagem de sucesso',190,'0',7,2,'xpath','.//span[contains(text(), ''Não'')]','click',NULL,'1','0',NULL,0,'other_step',17,NULL,NULL,'0',0,'procurando botão NÃO na mensagem de sucesso','botão de NÃO encontrado e clickado com sucesso','0','10|11|12'),
 (20,1,20,'check de sessao expirada 1','procura por label de mensagem de bem vindo',200,'0',2,0,'id','mensagemBemVindo','find',NULL,'0','1',NULL,0,NULL,NULL,NULL,NULL,'1',5,'verificando se voltou para a tela de abertura','tela de abertura encontrada - reiniciando processo','0','none'),
 (21,1,21,'check de sessao expirada 2','procura por tela de login',210,'0',1,0,'id','divLogin','find',NULL,'0','1',NULL,0,NULL,NULL,NULL,NULL,'1',5,'verificando se foi para a tela de login','tela de login encontrada - ação na tela será necessária para realizar o login novamente','0','none'),
 (22,1,22,'check de conexão','procurar por tela de erro de conexão',220,'0',-1,0,'id','main-frame-error','find',NULL,'0','1',NULL,0,NULL,NULL,NULL,NULL,'1',5,'verificando se conexão com internet falhou','identificado que sua conexão com a internet falhou - será iniciada tentativa de refresh da página','0','none');
INSERT INTO "scripts" ("id","name","description","version","status","delete_on_sync") VALUES (1,'Cupom sem CPF com Chave','Opção no menu de cadastro de cupons sem CPF, informando a chave de acesso','1','1','1'),
 (2,'Cadastramento cupom autorizado entidade','Opção no menu de cadastramento de cupons informando chave de acesso, quando autorizado pela instituição','1','1','1');
COMMIT;
