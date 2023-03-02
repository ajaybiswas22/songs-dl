# songs-dl

## Download songs from YouTube for free.

Uses yt-dlp library to download files from YouTube. 

### Usage

1. Create *input* folder.
2. Place csv file(s) containing url(s).
```
# input/file1.csv
link1
link2
link3
```
```
# input/file2.csv
link1
link2
link3
```
3. Install dependencies
```
pip install -r requirements.txt
```
4. Run main.py
5. The *output* folder will contain the extracted files.
```
output/file1/song1.mp3...
output/file2/song1.mp3...
```

### Issues

If main.py fails to execute because of missing FFmpeg encoder. Install FFmpeg dependencies using the following command.

#### Mac
```
brew install ffmpeg
```

#### Windows & Linux [Link](https://ffmpeg.org/download.html)





