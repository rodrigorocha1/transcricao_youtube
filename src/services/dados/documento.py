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

    def gravar_dados(self, texto: str):
        linhas = texto.split("\n")
        for linha in linhas:
            if linha.startswith("##  "):
                titulo = self.__documento.add_heading(linha[3:], level=1)
                for run in titulo.runs:
                    run.font.color.rgb = self.__cor
                    run.font.name = self.__fonte
            elif linha.startswith("### "):
                subtitulo = self.__documento.add_heading(linha[4:], level=2)
                for run in subtitulo.runs:
                    run.font.color.rgb = RGBColor(0, 0, 0)
                    run.font.name = 'Ubuntu'
            elif linha.startswith("* "):

                paragrafo = self.__documento.add_paragraph(
                    linha[2:], style='List Bullet')
                paragrafo.alignment = self.__alinhamento_justificado
                for run in paragrafo.runs:
                    run.font.name = self.__fonte
            elif linha.strip() != "":
                paragrafo = self.__documento.add_paragraph(linha)
                paragrafo.alignment = self.__alinhamento_justificado
                for run in paragrafo.runs:
                    run.font.name = self.__fonte

    def salvar_dados(self):
        self.__documento.save(self._caminho_arquivo)
