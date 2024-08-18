from src.services.youtube_internet.iyoutubeinternet import IYoutubeInternet
from youtube_transcript_api import YouTubeTranscriptApi


class YoutubeInternet(IYoutubeInternet):

    @classmethod
    def recuperar_legenda(self, id_video: str) -> str:
        """Método para recuperar a legenda do vídeo

        Args:
            id_video(str): id do vídeo do youtube

        Returns:
            str: retorna a legenda
        """
        legendas = YouTubeTranscriptApi.get_transcript(
            id_video,
            languages=['pt']
        )
        legenda = ' '.join(legenda['text'] for legenda in legendas).strip()
        return legenda
