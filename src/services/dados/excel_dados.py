from openpyxl import load_workbook
from openpyxl.workbook.workbook import Workbook
from src.services.dados.ioperacoes_dados import IOperacaoDados
import os


class ExcelDados(IOperacaoDados):
    def __init__(self, nome_arquivo: str) -> None:
        self.__caminho_base = os.getcwd()
        self.__caminho_planilha = os.path.join(
            self.__caminho_base, 'docs', f'{nome_arquivo}.xlsx')
        self.__planilha = self.abrir_planilha()

    def abrir_planilha(self) -> Workbook:
        planilha = load_workbook(self.__caminho_planilha)
        return planilha
