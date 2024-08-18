from src.services.dados.ioperacoes_dados import IOperacaoDados
from typing import Generator, Iterable, TypeVar, Generic
from abc import abstractmethod
import os

T = TypeVar('T')


class Arquivo(IOperacaoDados, Generic[T]):
    def __init__(self, nome_arquivo: str) -> None:
        self._nome_arquivo = nome_arquivo
        self._caminho_base = os.getcwd()

    @abstractmethod
    def abrir_arquivo(self) -> T:
        """Método para abrir arquivo

        Returns:
            Any: pode retornar um excel, txt
        """
        pass

    @abstractmethod
    def salvar_dados(self):
        """Método para salvar dados
        """
        pass

    @abstractmethod
    def marcar_campo(self):
        """Método para marcar as url baixadas
        """
        pass

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
