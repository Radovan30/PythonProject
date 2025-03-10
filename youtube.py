import yt_dlp

video_url = "https://www.youtube.com/watch?v=xuf1czJv-XI"
output_filename = "video4.mp4"

ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
    'outtmpl': output_filename,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

print("Video downloaded as:", output_filename)
