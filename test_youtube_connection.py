import yt_dlp

url = "https://www.youtube.com/watch?v=wKm8rVaZfqg"

ydl_opts = {
    'quiet': False,  # Set this to False to see more detailed logs
    'format': 'best',  # Choose the best available format
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
