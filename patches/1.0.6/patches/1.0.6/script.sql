CREATE TABLE messages_retry (id INTEGER PRIMARY KEY, codigo INTEGER, message TEXT DEFAULT '');
insert into messages_retry values (1, 1, 'Tipo De documento fiscal n�o suportado.');
insert into messages_retry values (2, 2, 'COO/N�mero documento fiscal � obrigat�rio.');
insert into messages_retry values (3, 3, '� obrigat�rio o preenchimento do C�digo de barras.');
insert into messages_retry values (4, 4, 'O C�digo de barras informado cont�m erros, favor corrigir antes de continuar.');
insert into messages_retry values (5, 5, 'Ocorreu um erro inesperado, tente novamente mais tarde.');