from typing import Generator, Iterable
from openpyxl import load_workbook
from openpyxl.workbook.workbook import Workbook
from openpyxl.worksheet.worksheet import Worksheet
from src.services.dados.ioperacoes_dados import IOperacaoDados
import os


class ExcelDados(IOperacaoDados):
    def __init__(self, nome_arquivo: str) -> None:
        self.__caminho_base = os.getcwd()
        self.__caminho_planilha = os.path.join(
            self.__caminho_base, 'docs', f'{nome_arquivo}.xlsx')
        self.__planilha = self.__abrir_arquivo()
        self.__aba = self.__planilha.active
        self.__ultima_linha = self.__aba.max_row

    def __abrir_arquivo(self) -> Workbook:
        """Método para abrir planilha
        """
        planilha = load_workbook(self.__caminho_planilha)
        return planilha

    def ler_valores(self) -> Generator[Iterable[str], None, None]:
        """Método para ler os valores da planilha

        Args:
            aba (Worksheet): a aba da planilha que está ativa
            ultima_linha (int): última linha do xlsx

        Yields:
            Generator[Iterable[str], None, None]: gerador com o valores da celula
        """
        for linha in self.__aba.iter_rows(
                min_row=2,
                max_row=self.__ultima_linha,
                min_col=1,
                max_col=2
        ):
            yield (celula.value for celula in linha)
