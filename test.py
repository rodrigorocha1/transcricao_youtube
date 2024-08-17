from google.oauth2 import service_account
from googleapiclient.discovery import build
import google.auth
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
import os.path
import pickle

# Substitua pelo caminho do arquivo JSON com suas credenciais OAuth
CLIENT_SECRETS_FILE = '../client_secret.json'
SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']


def get_authenticated_service():
    credentials = None
    # O arquivo token.pickle armazena o token de acesso do usuário
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            credentials = pickle.load(token)

    # Se não houver credenciais válidas, permita ao usuário fazer login.
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRETS_FILE, SCOPES)
            credentials = flow.run_local_server(port=0)
        # Salve as credenciais para a próxima execução
        with open('token.pickle', 'wb') as token:
            pickle.dump(credentials, token)

    return build('youtube', 'v3', credentials=credentials)


def get_video_captions(video_id):
    youtube = get_authenticated_service()
    captions = youtube.captions().list(part='snippet', videoId=video_id).execute()

    for item in captions['items']:
        caption_id = item['id']
        caption = youtube.captions().download(id=caption_id, tfmt='srt').execute()

        # A transcrição estará no formato SRT (SubRip Subtitle)
        return caption.decode('utf-8')


video_id = 'id_video'  # Substitua pelo ID do vídeo do YouTube
transcription = get_video_captions(video_id)
print(transcription)
