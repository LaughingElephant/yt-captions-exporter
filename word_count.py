import os
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def scrub_captions_folder(folder_path):
    word_counter = Counter()

    # Ensure the folder exists
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' does not exist.")
        return

    # Iterate over all .txt files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    text = file.read().lower()
                    words = [word for word in text.split() if not word.isdigit()]
                    word_counter.update(words)
            except Exception as e:
                print(f"Error reading file {filename}: {e}")

    # Save the word count results to a file
    output_file = os.path.join(folder_path, "word_count_results.txt")
    try:
        with open(output_file, "w", encoding="utf-8") as file:
            file.write("Word Count Across All Files:\n")
            for word, count in word_counter.most_common():
                file.write(f"{word}: {count}\n")
        print(f"Word count results saved to {output_file}")
    except Exception as e:
        print(f"Error saving results to file: {e}")

    return word_counter

if __name__ == "__main__":
    captions_folder = "captions"
    word_counts = scrub_captions_folder(captions_folder)

def visualize_word_cloud(word_counts):
    # Generate a word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_counts)

    # Display the word cloud
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Word Cloud of Most Common Words")
    plt.show()

if __name__ == "__main__":
    captions_folder = "captions"
    word_counts = scrub_captions_folder(captions_folder)

    if word_counts:
        visualize_word_cloud(word_counts)
        
wordcloud = WordCloud(
    width=800, height=400,
    background_color='white',
    colormap='magma'
).generate_from_frequencies(word_counts)