import streamlit as st
import yt_dlp
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

def descargar_video(url):
    options = {
        'outtmpl': './%(title)s.%(ext)s',
        'format': 'bestvideo[ext=mp4][vcodec^=avc1][height<=1080]+bestaudio[ext=m4a]/best[ext=mp4][height<=1080]',
        'merge_output_format': 'mp4'
    }
    
    with yt_dlp.YoutubeDL(options) as ydl:
        info = ydl.extract_info(url, download=True)
        video_title = info['title']
        # Get the filename of downloaded video
        filename = f"{video_title}.mp4"
        return filename

st.title("Descargar videos de YouTube")
url = st.text_input("Introduce la URL del video de YouTube")

# drop all old mp4 files
for file in os.listdir(dir_path):
    if file.endswith(".mp4"):
        os.remove(os.path.join(dir_path, file))



if st.button("Descargar"):
    try:
        
    
        filename = descargar_video(url)
        
        path_file = os.path.join(dir_path, filename)
        # Read file as bytes
        with open(path_file, 'rb') as f:
            video_bytes = f.read()
        # Show download button
        st.download_button(
            label="Obtener en descargas",
            data=video_bytes,
            file_name=filename,
            mime="video/mp4"
        )

    except Exception as e:
        st.error(f"Error al descargar el video: {str(e)}")