from abc import ABC, abstractmethod


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
    def obter_resposta_modelo(self, sentenca: str) -> str:
        """Método para obter a transcrição formatada pela IA

        Args:
            sentenca (str): recebe a sentença

        Returns:
            str: resposta da ia
        """
        pass
