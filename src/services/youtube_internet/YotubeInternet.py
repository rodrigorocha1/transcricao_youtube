from src.services.youtube_internet.iyoutubeinternet import IYoutubeInternet
from src.pacote_log.config_log import logger
from youtube_transcript_api import (
    YouTubeTranscriptApi,
    TranscriptsDisabled,
    CouldNotRetrieveTranscript,
    NoTranscriptAvailable,
    NoTranscriptFound,

)


class YoutubeInternet(IYoutubeInternet):

    @classmethod
    def recuperar_legenda(self, id_video: str) -> str:
        """Método para recuperar a legenda do vídeo

        Args:
            id_video(str): id do vídeo do youtube

        Returns:
            str: retorna a legenda
        """
        try:
            legendas = YouTubeTranscriptApi.get_transcript(
                id_video,
                languages=['pt']
            )
            legenda = ' '.join(legenda['text'] for legenda in legendas).strip()
            return legenda
        except TranscriptsDisabled as E:
            logger.error(f'legendas desabilitadas {id_video}')
            exit()
        except CouldNotRetrieveTranscript as msg:
            logger.error(
                f'Não recuperou a transcrição para o vídeo {id_video} : {msg}')
            exit()
        except Exception as e:
            logger.critical(f'FALHA TOTAL {e}')
            exit()
