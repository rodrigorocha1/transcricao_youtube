from src.services.dados.ioperacoes_dados import IOperacaoDados
from src.services.dados.excel_dados import ExcelDados
from src.services.youtube_internet.iyoutubeinternet import IYoutubeInternet
from src.services.youtube_internet.YotubeInternet import YoutubeInternet
from src.services.iachat.ichat import IChat
from src.services.iachat.chat_google_gemini import ChatGoogleGemini
from src.services.dados.documento import Documento
from src.services.dados.arquivo import Arquivo
from src.services.dados.arquivo_txt import ArquivoTXT
from src.pacote_log.config_log import logger
from typing import Union, Tuple


class TranscricaoVideoPipeline:
    def __init__(
            self, arquivo:
            Union[IOperacaoDados, Arquivo],
            servico_youtube: IYoutubeInternet,
            servico_chat: IChat,
            documento: Documento,
            arquivo_bruto: Arquivo) -> None:
        self.__arquivo = arquivo
        self.__servico_youtube = servico_youtube
        self.__servico_chat = servico_chat
        self.__documento = documento
        self.__arquivo_bruto = arquivo_bruto

    def __realizar_operacoes_documento_texto_tratado(self, valor: Tuple[str, str], texto_tratado: str):
        with self.__documento as documento_tratado:
            documento_tratado = self.__documento
            documento_tratado.opcao_tratamento = 1
            documento_tratado.texto = texto_tratado
            documento_tratado.gravar_dados()
            documento_tratado.salvar_dados(
                nome_arquivo=f'resumo_do_video_{str(valor[1])}.docx')

    def __realizar_operacoes_texto_bruto(self, valor: Tuple[str, str], texto_bruto: str):
        arquivo_bruto = self.__arquivo_bruto
        arquivo_bruto.texto = texto_bruto
        arquivo_bruto.nome_arquivo = f'transcricao_bruta_{valor[1]}.txt'
        arquivo_bruto.gravar_dados()
        arquivo_bruto.salvar_dados()
        del arquivo_bruto

    def rodar_pipeline(self):
        logger.info('Iniciando Transcrição')
        for chave, valor in enumerate(self.__arquivo.ler_valores()):

            chave += 1
            texto_legenda = self.__servico_youtube.recuperar_legenda(valor[0])
            sentenca = self.__servico_chat.criar_sentenca(texto=texto_legenda)
            texto_tratado = self.__servico_chat.obter_resposta_modelo(
                sentenca=sentenca)
            self.__realizar_operacoes_documento_texto_tratado(
                valor=valor,  texto_tratado=texto_tratado)
            self.__realizar_operacoes_texto_bruto(
                valor=valor, texto_bruto=texto_legenda)
        self.__arquivo.salvar_dados(linha=chave)


if __name__ == '__main__':
    tvp = TranscricaoVideoPipeline(
        arquivo=ExcelDados(
            nome_arquivo='videos_transcrever.xlsx'
        ),
        servico_youtube=YoutubeInternet(),
        servico_chat=ChatGoogleGemini(),
        documento=Documento(),
        arquivo_bruto=ArquivoTXT())
    tvp.rodar_pipeline()
