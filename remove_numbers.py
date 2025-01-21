import os
import re

def scrub_numbers_from_files(folder_path):
    # Ensure the folder exists
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' does not exist.")
        return

    # Process each .txt file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()

                # Remove all numbers using a regular expression
                scrubbed_content = re.sub(r'\d+', '', content)

                # Write the updated content back to the file
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(scrubbed_content)

                print(f"Processed file: {filename}")
            except Exception as e:
                print(f"Error processing file {filename}: {e}")

if __name__ == "__main__":
    folder_to_scrub = "captions"  # Change this to the target folder
    scrub_numbers_from_files(folder_to_scrub)
    