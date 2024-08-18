from abc import ABC, abstractmethod
from typing import Tuple


class IChat(ABC):

    @abstractmethod
    def criar_sentenca(self, texto) -> str:
        """Método que cria a setença

        Args:
            texto (_type_): recebe o texto

        Returns:
            str: sentença que ira ser lida
        """
        pass

    @abstractmethod
    def obter_resposta_modelo(self, sentenca: str) -> Tuple[str, str]:
        """Método para recuperar a transcrição gravada e a transcrição bruta

        Args:
            sentenca (str): recebe a sentença

        Returns:
            Tuple[str, str]: resposta_tratada e resposta bruta
        """
        pass
