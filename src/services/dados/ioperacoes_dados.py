from abc import ABC, abstractmethod
from openpyxl.worksheet.worksheet import Worksheet
from openpyxl.workbook.workbook import Workbook
from typing import Generator, Iterable


class IOperacaoDados(ABC):

    @abstractmethod
    def abrir_planilha(self) -> Workbook:
        """Método para abrir planilha
        """
        pass

    @abstractmethod
    def ler_valores(self, aba: Worksheet, ultima_linha: int) -> Generator[Iterable[str], None, None]:
        """Método para ler os valores da planilha

        Args:
            aba (Worksheet): a aba da planilha que está ativa
            ultima_linha (int): última linha do xlsx

        Yields:
            Generator[Iterable[str], None, None]: gerador com o valores da celula
        """

        pass
