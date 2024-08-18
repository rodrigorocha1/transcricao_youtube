from typing import Generator, Iterable
from openpyxl import load_workbook
from openpyxl.workbook.workbook import Workbook
from openpyxl.worksheet.worksheet import Worksheet
from src.services.dados.arquivo import Arquivo
import os


class ExcelDados(Arquivo[Workbook]):

    def __init__(self) -> None:
        super().__init__()
        self.__caminho_planilha = os.path.join(
            self._caminho_base, 'docs', f'{self._nome_arquivo}.xlsx')
        self.__planilha = self.abrir_arquivo()
        self.__aba = self.__planilha[self.__nome_aba]
        self.__nome_aba = self.__planilha.active.title
        self.__ultima_linha = self.__aba.max_row
        self.__ultima_coluna = self.__aba.max_column

    def abrir_arquivo(self) -> Workbook:
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
                celula.alignment = alinhamento_centralizado

    def salvar_planilha(self):
        """Método para salvar dados 
        """
        self.__planilha.save(self.__caminho_planilha)
        self.__planilha.close()
