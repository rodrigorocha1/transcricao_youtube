## Transcrição das legendas de um vídeo do  youtube e prepararando o resumo com a API do google gemini

## 1 - Ideia do projeto

A ideia surgiu de um short do canal Asimov Academy (https://www.youtube.com/shorts/V1PNrhV9qjA), com alguns extras adicionados comforme irá ser descrito no tópico 2.

## 2- Fluxo do projeto:

Os links dos vídeos irão ser guardados em um excel  e lidos posteriormente, depois irá ser utilizado a biblioteca do python youtube_transcript_api para baixar as transcrições e as transcrições serão submetida ao modelo com a seguinte sentença “Crie um resumo com base nessa transcrição do vídeo do youtube: '{texto}' e formate para ser salvo em um arquivo docx inclua títulos e subtitulos e formate o texto como 'justificado' quando possível. Faça assim. título nível 1 marque com ## subtibulo, marque com ##, paragrafo marque com *” 
Depois, a resposta do google gemini ira ser formatada para documento word e ser salva.
 
## 3 Diagrama de classe
A figura abaixo, mostra um diagrama de classe para o projeto, a ideia, de maneira geral, é consumir um arquivo (excel), no qual, os id’s dos vídeos do youtube irão ser submetidos a um serviço de transcrição de legendas (youtube_transcript_api), logo em seguida, a transcrição irá ser submetida a um modelo de chat ia (Google Gemini), logo depois, o texto da resposta do modelo de ia irá ser formatado e salvo em um arquivo (docx), a transcrição bruta,  também irá ser salva em um arquivo (txt) e marcando em um arquivo (excel), as url’s que já baixaram a transcrição.

![Exemplo de imagem](https://raw.githubusercontent.com/rodrigorocha1/transcricao_youtube/main/docs/diagrama%20de%20classe.png)

## 4- Vídeo

[Clique aqui para ver a demonstração]([https://youtu.be/tLYOw8iu-SM](https://youtu.be/CPAyC4Litms))
