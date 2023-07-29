tabela_documentario = """
CREATE TABLE documentario(
    idDocumentario int not null AUTO_INCREMENT,
    nome varchar(200) not null,
    duracao int not null,
    ano int not null,
    PRIMARY KEY(idDocumentario)
);
 """