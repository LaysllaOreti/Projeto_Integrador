import sys
import csv
from PyQt5 import QtWidgets, uic

class MinhaJanela(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("qtDesigner.ui", self)
        self.carregar_tabela_csv("estoque.csv")

    def carregar_tabela_csv(self, nome_arquivo):
        try:
            with open(nome_arquivo, newline='', encoding='utf-8') as csvfile:
                leitor = csv.reader(csvfile, delimiter=',')

                # Lê os dados do CSV
                dados = list(leitor)
                if not dados:
                    return

                # Define cabeçalhos
                cabecalhos = dados[0]
                linhas = dados[1:]

                tabela = self.findChild(QtWidgets.QTableWidget, "tabelaDados")
                tabela.setColumnCount(len(cabecalhos))
                tabela.setHorizontalHeaderLabels(cabecalhos)
                tabela.setRowCount(len(linhas))

                for i, linha in enumerate(linhas):
                    for j, valor in enumerate(linha):
                        tabela.setItem(i, j, QtWidgets.QTableWidgetItem(valor))

        except FileNotFoundError:
            print(f"Arquivo '{nome_arquivo}' não encontrado.")
        except Exception as e:
            print(f"Erro ao carregar CSV: {e}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    janela = MinhaJanela()
    janela.show()
    sys.exit(app.exec_())
