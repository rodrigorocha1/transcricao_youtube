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
        """Método que irá fazer a busca da setença

        Args:
            sentenca (str): sentença

        Returns:
            str: texto com a resposta da sentença
        """
        pass
