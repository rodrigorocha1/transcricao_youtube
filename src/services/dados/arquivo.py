from src.services.dados.ioperacoes_dados import IOperacaoDados
from typing import Generator, Iterable, TypeVar, Generic
from abc import abstractmethod
import os

T = TypeVar('T')


class Arquivo(IOperacaoDados, Generic[T]):
    def __init__(self, nome_arquivo: str) -> None:
        """_summary_

        Args:
            nome_arquivo (str): nome do arquivo a ser aberto sem extensao 
        """
        self._nome_arquivo = nome_arquivo
        self._caminho_base = os.getcwd()
        self._caminho_arquivo = os.path.join(
            self._caminho_base, 'docs', f'{self._nome_arquivo}')

    @abstractmethod
    def _abrir_arquivo(self) -> T:
        """_summary_

        Returns:
            T: Retorna o arquivo aberto
        """
        pass

    @abstractmethod
    def salvar_dados(self):
        """Método para salvar dados
        """
        pass
