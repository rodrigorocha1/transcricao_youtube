from docx.document import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import RGBColor
from src.services.dados.arquivo import Arquivo


class Documento(Arquivo[Document]):

    def __init__(self, nome_arquivo: str) -> None:
        super().__init__(nome_arquivo)
        self.__fonte = 'Ubuntu'
        self.__cor = RGBColor(0, 0, 0)
        self.__alinhamento_justificado = WD_ALIGN_PARAGRAPH.JUSTIFY
        self.__documento = self._abrir_arquivo()

    def _abrir_arquivo(self) -> Document:
        """Método para abrir_arquivo

        Returns:
            Document: _description_
        """
        documento = Document()
        return documento
