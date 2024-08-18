from typing import Generator, Iterable
from openpyxl import load_workbook
from openpyxl.workbook.workbook import Workbook
from openpyxl.styles import Alignment
from src.services.dados.arquivo import Arquivo
import os


class ExcelDados(Arquivo[Workbook]):

    def __init__(self, nome_arquivo: str) -> None:
        super().__init__(nome_arquivo)

        self.__planilha = self._abrir_arquivo()

        self.__nome_aba = self.__planilha.active.title
        self.__aba = self.__planilha[self.__nome_aba]
        self.__ultima_linha = self.__aba.max_row
        self.__ultima_coluna = self.__aba.max_column
        self.__alinhamento_centralizado = Alignment(
            horizontal='center', vertical='center')

    def _abrir_arquivo(self) -> Workbook:
        """Método para abrir a planilha

        Returns:
            Workbook: uma planilha
        """
        planilha = load_workbook(self._caminho_arquivo)
        return planilha

    def ler_valores(self) -> Generator[Iterable[str], None, None]:
        """Método para ler os valores da planilha

        Args:
            aba (Worksheet): a aba da planilha que está ativa
            ultima_linha (int): última linha do xlsx

        Yields:
            Generator[Iterable[str], None, None]: gerador com o valores da celula
        """

        for linha in self.__aba.iter_rows(min_row=2, max_col=1):
            celula = linha[0]
            yield celula.value.split('=')[-1]

    def marcar_campo(self):
        for linha in self.__aba.iter_rows(
                min_row=1,
                max_row=self.__ultima_linha,
                min_col=self.__ultima_coluna, max_col=self.__ultima_coluna):
            celula = linha[0]
            print(linha[0])
            print(celula.style_id)
            if celula.value is None:
                celula.value = 'X'
                celula.alignment = self.__alinhamento_centralizado

    def salvar_dados(self):
        """Método para salvar dados
        """
        self.__planilha.save(self._caminho_arquivo)

    def __del__(self):
        self.__planilha.close()
