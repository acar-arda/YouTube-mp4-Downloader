import yt_dlp

def my_hook(d, window):
    if d['status'] == 'downloading':
        downloaded = d.get('downloaded_bytes') or 0
        total = d.get('total_bytes') or d.get('total_bytes_estimate') or 0
        if total:
            percent = downloaded / total * 100
        else:
            percent = 0
        window.write_event_value('-PROGRESS-', percent)
    elif d['status'] == 'finished':
        window.write_event_value('-PROGRESS-', 100)

def download_video(url, directory, window):
    ydl_opts = {
        'format': 'best',
        'outtmpl': directory + '/%(title)s.%(ext)s',
        'quiet': True,
        'progress_hooks': [lambda d: my_hook(d, window)]
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            window.write_event_value('-RESULT-', "İndirme Başarılı!")
        except Exception as e:
            window.write_event_value('-RESULT-', f"İndirme Başarısız! : {e}")