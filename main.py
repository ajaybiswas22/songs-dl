import pandas as pd
import os
from yt_dlp import YoutubeDL

def main():
    input_dir = "input"
    output_dir = "output"

    input_fetched = os.listdir(input_dir)
    input_fetched = [x for x in input_fetched if x.endswith(".csv")]

    for file in input_fetched:
        filename = os.path.splitext(file)[0]
        print(filename)

        songs_df = pd.read_csv(input_dir + "/" + file, header=None)
        URLS = list(songs_df[0])

        ydl_opts = {
        'format': 'mp3/bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
        'outtmpl':output_dir + '/' + filename + '/%(title)s.%(ext)s',
        }

        with YoutubeDL(ydl_opts) as ydl:
            error_code = ydl.download(URLS)

if __name__ == "__main__":
    main()