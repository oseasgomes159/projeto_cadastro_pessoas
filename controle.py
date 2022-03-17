from PyQt5 import uic, QtWidgets
import mysql.connector

#CONECTAR O MEU BANCO DE DADOS AO PROGRAMA CRIADO

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cadastro_pessoas"
)

#MOSTRAR DADOS DIGITADOS NA LINEEDIT

def funcao_principal():
    linha1 = cadastro_pessoas.lineEdit.text()
    linha2 = cadastro_pessoas.lineEdit_2.text()
    linha3 = cadastro_pessoas.lineEdit_3.text()
    linha4 = cadastro_pessoas.lineEdit_4.text()
    linha5 = cadastro_pessoas.lineEdit_5.text()
    linha6 = cadastro_pessoas.lineEdit_6.text()
    linha7 = cadastro_pessoas.lineEdit_7.text()
    linha8 = cadastro_pessoas.lineEdit_8.text()
    linha9 = cadastro_pessoas.lineEdit_9.text()
    linha10 = cadastro_pessoas.lineEdit_10.text()

    print("Telefone:", linha1)
    print("Nome:", linha2)
    print("CEP:", linha3)
    print("Endereço:", linha4)
    print("Numero:", linha5)
    print("Complemento:", linha6)
    print("Bairro:", linha7)
    print("Cidade:", linha8)
    print("Estado:", linha9)
    print("Referencia:", linha10)

#PUXAR TODOS DADOS INSERIDOS NAS COLUNAS PARA O BANCO DE DADOS

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO pessoas (telefone, nome, cep, endereço, numero, complemento, bairro, cidade, estado, referencia) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    dados = (str(linha1),str(linha2),str(linha3),str(linha4),str(linha5),str(linha6),str(linha7),str(linha8),str(linha9),str(linha10))
    cursor.execute(comando_SQL,dados)
    banco.commit()

app = QtWidgets.QApplication([])
cadastro_pessoas = uic.loadUi("cadastro_pessoas.ui")
cadastro_pessoas.pushButton.clicked.connect(funcao_principal)

cadastro_pessoas.show()
app.exec()






"""#CRIAR A TABELA
 create table pessoas (
id INT NOT NULL AUTO_INCREMENT,
telefone VARCHAR(11),
nome CHAR(50),
cep VARCHAR(8),
endereço CHAR(100),
numero VARCHAR(100),
complemento CHAR(100),
bairro CHAR(50),
cidade CHAR(50),
estado CHAR(50),
referencia CHAR(100),
PRIMARY KEY (id)
);
#INSERIR DADOS A TABELA
INSERT INTO pessoas (telefone, nome, cep, endereço, numero, complemento, bairro, cidade, estado, referencia)
VALUES ("21968475724", "Oséias Gomes", "24350200", "Estrada Frei Orlando", "138", "Casa 5", "Piratininga", "Niteroi", "RJ", "Próximo A Escola"); """