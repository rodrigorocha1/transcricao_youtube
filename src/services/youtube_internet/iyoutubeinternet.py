from abc import ABC, abstractmethod


class IYoutubeInternet(ABC):
    @abstractmethod
    def recuperar_legenda(self, id_video: str) -> str:
        """Método para recuperar a legenda do vídeo

        Args:
            id_video (str): id do vídeo do youtube

        Returns:
            str: retorna a legenda
        """
        pass
