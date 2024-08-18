from src.services.dados.arquivo import Arquivo
from src.pacote_log.config_log import logger
from typing import Generator, TextIO, Tuple
import os


class ArquivoTXT(Arquivo[TextIO]):
    def __init__(self, nome_arquivo: str = None, texto: str = None) -> None:
        super().__init__(nome_arquivo, texto)

    def _abrir_arquivo(self) -> TextIO:
        try:
            if self.nome_arquivo is not None:
                return open(os.path.join(self._caminho_arquivo, self._nome_arquivo), 'w')
        except FileNotFoundError as m:
            logger.error(f'Não encontrou o arquivo: {m}')
            exit()

    def ler_valores(self) -> Generator[Tuple[str, str], None, None]:
        with open(self._caminho_arquivo, 'r') as arquivo:
            for linha in arquivo:
                yield linha

    def gravar_dados(self):

        with self._abrir_arquivo() as arquivo:
            arquivo.write(self.texto)
            arquivo.close()

    def salvar_dados(self, nome_arquivo: str = None, **kwargs):
        pass
