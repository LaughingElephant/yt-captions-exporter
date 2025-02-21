from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import NoTranscriptFound, TranscriptsDisabled
import sys
import os

def fetch_captions(video_ids):
    output_dir = "captions"
    os.makedirs(output_dir, exist_ok=True)

    for video_id in video_ids:
        try:
            print(f"Fetching captions for video ID: {video_id}")

            # Fetch transcript
            try:
                transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
                try:
                    transcript = transcript_list.find_manually_created_transcript(['en']).fetch()
                    print("Manual captions found.")
                except NoTranscriptFound:             
                    print("No manual captions found. Trying auto-generated captions...")
                    transcript = transcript_list.find_generated_transcript(['en']).fetch()
            except NoTranscriptFound:
                print("No captions available (manual or auto-generated).")
                continue            
            # Convert transcript to plain text
            captions = "\n".join([item['text'] for item in transcript])

            # Save captions to a file
            output_file = os.path.join(output_dir, f"{video_id}.txt")
            with open(output_file, "w", encoding="utf-8") as file:
                file.write(captions)
            
            print(f"Captions saved to: {output_file}")
        except NoTranscriptFound:
            print(f"No captions (manual or auto-generated) available for video ID: {video_id}")
        except TranscriptsDisabled:
            print(f"Captions are disabled for video ID: {video_id}")
        except Exception as e:
            print(f"An error occurred for video ID {video_id}: {e}")

if __name__ == "__main__":
    print("Enter YouTube video URLs or IDs (comma-separated):")
    input_data = input().strip()
    
    # Parse video IDs from input (support both URLs and plain IDs)
    video_ids = [
        url.split("v=")[-1].split("&")[0] if "youtube.com" in url else url.strip()
        for url in input_data.split(",")
    ]
    
    fetch_captions(video_ids)
    
    # Helper function to get the correct path for the 'captions' folder
def resource_path(relative_path):
    # Get the absolute path to resources, considering the temporary extraction directory
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# Use the resource_path function for the captions folder
CAPTIONS_DIR = resource_path("captions")
os.makedirs(CAPTIONS_DIR, exist_ok=True)

# Example: Save a file in the captions folder
def save_to_captions(filename, content):
    filepath = os.path.join(CAPTIONS_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"Saved to {filepath}")