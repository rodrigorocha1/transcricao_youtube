from src.services.dados.ioperacoes_dados import IOperacaoDados
from typing import Generator, Iterable, TypeVar, Generic
from abc import abstractmethod
import os

T = TypeVar('T')


class Arquivo(IOperacaoDados, Generic[T]):
    def __init__(self, nome_arquivo: str = None) -> None:
        """_summary_

        Args:
            nome_arquivo (str): nome do arquivo a ser aberto sem extensao 
        """
        self._nome_arquivo = nome_arquivo
        self._caminho_base = os.getcwd()
        if self._nome_arquivo is not None:
            self._caminho_arquivo = os.path.join(
                self._caminho_base, 'docs', f'{self._nome_arquivo}')

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

    @abstractmethod
    def _abrir_arquivo(self) -> T:
        """_summary_

        Returns:
            T: Retorna o arquivo aberto
        """
        pass

    @abstractmethod
    def salvar_dados(self, nome_arquivo: str = None):
        """Método para salvar arquivo

        Args:
            nome_arquivo (str, optional): nome do arquivo . Defaults to None.
        """
        pass
