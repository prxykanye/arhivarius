from yt_dlp import YoutubeDL


def get_channel_info(url: str) -> dict:
    ydl_opts = {
        "extract_flat": True,
        "quiet": True,
        "skip_download": True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    return {
        "url": info.get("uploader_url"),
        "channel_id": info.get("id"),
        "title": info.get("title"),
        "status": "active",
    }
