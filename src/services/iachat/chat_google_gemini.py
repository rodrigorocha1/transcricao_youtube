import google.generativeai as genai
from src.services.iachat.ichat import IChat
from dotenv import load_dotenv
import os
load_dotenv


class ChatGoogleGemini(IChat):

    def __init__(self, texto: str) -> None:
        self.__texto = texto
        self.__api_key = os.environ['chave_chat_gpt']

    def criar_sentenca(self) -> str:
        """Cria a sentença da pesquisa

        Returns:
            str: a sentença de busca
        """
        sentenca = f"""
            Crie um resumo com base nessa transcrição do vídeo do youtube: '{self.__texto}' e formate para ser salvo em um arquivo docx inclua títulos e subtitulos e formate o texto como 'justificado' quando possível
        """.strip()
        return sentenca

    def obter_resposta_modelo(self, sentenca: str) -> str:
        """Método que irá fazer a busca da setença

        Args:
            sentenca (str): sentença

        Returns:
            str: texto com a resposta da sentença
        """
        genai.configure(api_key=self.__api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(sentenca)
        texto = response.text
        return texto
