# YouTube Captions Downloader

This Python script fetches captions (subtitles) for YouTube videos, including both manually uploaded and auto-generated captions. It supports multiple video URLs or IDs, and saves the captions as `.txt` files for each video.

## Features

- Fetch captions from YouTube videos (manual or auto-generated).
- Accepts a list of video URLs or IDs as input.
- Saves captions to a `captions` directory with each file named after the video ID.
- Handles errors gracefully for videos without captions or disabled captions.

## Prerequisites

Ensure you have Python 3.9 or later installed. You also need to install the following Python libraries:

- [`youtube-transcript-api`](https://pypi.org/project/youtube-transcript-api/)

To install the required library, run:

```bash
pip install youtube-transcript-api
```

## How to Use

1. **Clone or Download the Script**
   Save the script to a file, e.g., `youtube_captions_downloader.py`.

2. **Run the Script**
   Execute the script from the command line:

   ```bash
   python youtube_captions_downloader.py
   ```

3. **Provide Input**
   When prompted, enter a comma-separated list of YouTube video URLs or IDs:

   ```
   Enter YouTube video URLs or IDs (comma-separated):
   https://www.youtube.com/watch?v=abc123, xyz456
   ```
   IMPORTANT - shortened youtube URLs will not work:
   https://youtu.be/abc123

4. **Output**
   The script will:
   - Fetch captions for each video.
   - Save them to the `captions` directory.
   - Notify you of any errors or unavailable captions.

## Example

### Input

```
https://www.youtube.com/watch?v=abc123, xyz456
```

### Output

- `captions/abc123.txt`
- `captions/xyz456.txt`

Each file contains the captions in plain text format.

## Error Handling

The script handles the following scenarios:

- **No Captions Found**: Logs a message if neither manual nor auto-generated captions are available.
- **Captions Disabled**: Notifies you if captions are disabled for a video.
- **Invalid Input**: Ensures input is properly parsed for video IDs.

## Notes

- Auto-generated captions default to English (`en`). You can customize the language preferences by editing the script's `languages` parameter in the `YouTubeTranscriptApi.get_transcript()` method.
- Invalid characters in video titles are replaced with underscores for safe filenames.

## License

This script is provided as-is under the MIT License. Feel free to modify and use it as needed.
