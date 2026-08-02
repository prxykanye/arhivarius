import yt_dlp


def get_video_list(channel_url: str):

    ydl_opts = {
        "extract_flat": True,
        "quiet": True,
        "skip_download": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(channel_url, download=False)
        pass


def download_video(url, output_path="downloads"):
    ydl_opts: dict | None = {
        # "format": "bestvideo+bestaudio/best",
        "outtmpl": f"{output_path}/%(channel)s/%(title)s [%(id)s].%(ext)s",
        "skip": True,
        "skip_download": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        pass
        ydl.download([url])


if __name__ == "__main__":
    # download_video("https://www.youtube.com/@proxykanye")
    get_video_list("https://www.youtube.com/@sumochkinproduction2399")
