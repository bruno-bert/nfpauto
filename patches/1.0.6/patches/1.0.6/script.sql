CREATE TABLE messages_retry (id INTEGER PRIMARY KEY, codigo INTEGER, message TEXT DEFAULT '');
insert into messages_retry values (1, 1, 'Tipo De documento fiscal não suportado.');
insert into messages_retry values (2, 2, 'COO/Número documento fiscal é obrigatório.');
insert into messages_retry values (3, 3, 'É obrigatório o preenchimento do Código de barras.');
insert into messages_retry values (4, 4, 'O Código de barras informado contém erros, favor corrigir antes de continuar.');
insert into messages_retry values (5, 5, 'Ocorreu um erro inesperado, tente novamente mais tarde.');