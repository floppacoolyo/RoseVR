import yt_dlp
import os

def download_audio(urls):
    # Configurações para baixar apenas o áudio e converter para MP3
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        # Caminho direto para o seu executável do FFmpeg
        'ffmpeg_location': r'C:\ffmpeg\ffmpeg.exe',
        'outtmpl': '%(title)s.%(ext)s',  # Nome do arquivo será o título da música
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Iniciando download...")
            ydl.download(urls)
            print("\nDownload concluído com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    # Lista dos links para download
    musicas = [
        "https://www.youtube.com/watch?v=NT4eF9YsYnM", # Passo Bem Solto
        "https://www.youtube.com/watch?v=orOgilmiL_4"  # No Batidão
    ]
    
    download_audio(musicas)