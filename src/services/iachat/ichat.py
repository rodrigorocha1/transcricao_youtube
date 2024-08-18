from abc import ABC, abstractmethod


class IChat(ABC):

    @abstractmethod
    def criar_sentenca(self) -> str:
        """Método que vai criar a sentença para o chat

        Returns:
            str: retorna a consulta
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
