import google.generativeai as genai
from src.services.iachat.ichat import IChat
from dotenv import load_dotenv
from typing import Tuple
import os
load_dotenv


class ChatGoogleGemini(IChat):

    def __init__(self) -> None:

        self.__api_key = os.environ['chave_chat_gpt']

    def criar_sentenca(self, texto) -> str:
        """_summary_

        Args:
            texto (_type_): recebe um texto 

        Returns:
            str: A sentença que irá ser lida
        """

        sentenca = f"""
            Crie um resumo com base nessa transcrição do vídeo do youtube: '{texto}' 
            e formate para ser salvo em um arquivo docx inclua títulos e subtitulos e formate o texto como 'justificado' quando possível.
            Faça assim.título nível 1 marque com ## subtibulo, marque com ##, paragrafo marque com *
        """.strip()
        return sentenca

    def obter_resposta_modelo(self, sentenca: str) -> str:
        """Método para obter a transcrição formatada pela IA

        Args:
            sentenca (str): recebe a sentença

        Returns:
            str: resposta da ia
        """

        genai.configure(api_key=self.__api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(sentenca)
        texto = response.text

        return texto
