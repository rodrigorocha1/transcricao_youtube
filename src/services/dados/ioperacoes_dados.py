from abc import ABC, abstractmethod
from typing import Generator, Iterable


class IOperacaoDados(ABC):

    @abstractmethod
    def ler_valores(self) -> Generator[Iterable[str], None, None]:
        """Método para ler os valores da planilha

        Args:
            aba (Worksheet): a aba da planilha que está ativa
            ultima_linha (int): última linha do xlsx

        Yields:
            Generator[Iterable[str], None, None]: gerador com o valores da celula
        """

        pass
