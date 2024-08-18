from src.services.dados.arquivo import Arquivo
from typing import Generator, TextIO, Tuple
import os


class ArquivoTXT(Arquivo[TextIO]):
    def __init__(self, nome_arquivo: str = None, texto: str = None) -> None:
        super().__init__(nome_arquivo, texto)

    def _abrir_arquivo(self) -> TextIO:
        if self.nome_arquivo is not None:
            return open(self.caminho_arquivo, 'w')

    def ler_valores(self) -> Generator[Tuple[str, str], None, None]:
        with open(self.caminho_arquivo, 'r') as arquivo:
            for linha in arquivo:
                yield linha

    def gravar_dados(self, **kwargs):

        with self._abrir_arquivo() as arquivo:
            arquivo.write(self.texto)
            arquivo.close()

    def salvar_dados(self, nome_arquivo: str = None, **kwargs):
        pass
