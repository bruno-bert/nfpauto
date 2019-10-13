BEGIN TRANSACTION;
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
INSERT INTO "scripts" ("id","name","description","version","status","delete_on_sync") VALUES (1,'Cupom sem CPF com Chave','Opção no menu de cadastro de cupons sem CPF, informando a chave de acesso','1','1','1'),
 (2,'Cadastramento cupom autorizado entidade','Opção no menu de cadastramento de cupons informando chave de acesso, quando autorizado pela instituição','1','1','1');
COMMIT;
