from src.services.dados.ioperacoes_dados import IOperacaoDados
from src.services.dados.excel_dados import ExcelDados
from src.services.youtube_internet.iyoutubeinternet import IYoutubeInternet
from src.services.youtube_internet.YotubeInternet import YoutubeInternet
from src.services.iachat.ichat import IChat
from src.services.iachat.chat_google_gemini import ChatGoogleGemini
from src.services.dados.documento import Documento


class TranscricaoVideoPipeline:
    def __init__(
            self, arquivo:
            IOperacaoDados,
            servico_youtube: IYoutubeInternet,
            servico_chat: IChat,
            documento: Documento) -> None:
        self.__arquivo = arquivo
        self.__servico_youtube = servico_youtube
        self.__servico_chat = servico_chat
        self.__documento = documento

    def rodar_pipeline(self):
        for chave, valor in enumerate(self.__arquivo.ler_valores()):
            texto_legenda = self.__servico_youtube.recuperar_legenda(valor)
            sentenca = self.__servico_chat.criar_sentenca(texto=texto_legenda)
            texto_gerado = self.__servico_chat.obter_resposta_modelo(
                sentenca=sentenca)
            self.__documento.gravar_dados(texto=texto_gerado)
            self.__documento.salvar_dados(f'{str(chave)}.docx')


tvp = TranscricaoVideoPipeline(
    arquivo=ExcelDados(
        nome_arquivo='videos_transcrever.xlsx'
    ),
    servico_youtube=YoutubeInternet(),
    servico_chat=ChatGoogleGemini(),
    documento=Documento()
)
tvp.rodar_pipeline()
