import subprocess
from tkinter import *
from tkinter import scrolledtext
from collections import Counter
import re
import unicodedata

# Define a list of Mongolian stopwords
mongolian_stopwords = ["юм", "байна", "болон", "тэгээд", "гэсэн", "гэх", "нь", "дээр", "байх", "байдаг", "гэж"]

# Helper function: Use Hunspell to analyze spelling and stemming
def check_spelling_and_stem(words):
    # This function interacts with Hunspell to spell-check and provide stems for words.
    misspelled_words = {}
    stemmed_words = []

    for word in words:
        try:
            normalized_word = unicodedata.normalize('NFC', word)
            result = subprocess.run(
                ["hunspell", "-d", "mn_MN"],
                input=normalized_word,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                encoding="utf-8",
            )
            output = result.stdout.strip()

            # Check if the word is misspelled
            if output.startswith("&") or output.startswith("#"):
                suggestions = re.findall(r"(?<=: ).*", output)
                misspelled_words[word] = suggestions
            else:  # Correctly spelled; get the stem
                stem = re.search(r"(?<=: ).*", output)
                stemmed_words.append(stem.group(0) if stem else word)
        except Exception as e:
            print(f"Error processing word '{word}': {e}")
            misspelled_words[word] = []
    
    return stemmed_words, misspelled_words

# Helper function: Determine text classification based on keywords
def classify_text(text):
    categories = [
        ("эдийн засгийн", "economic"),
        ("спортын", "sports"),
        ("шинжлэх ухаан", "science"),
        ("урлаг", "art"),
        ("технологи", "technology"),
    ]

    for keyword, category in categories:
        if keyword in text:
            return category
    return "unknown"

# Helper function: Analyze frequency of words
def most_common_words(words, top_n=10):
    filtered_words = [word for word in words if word not in mongolian_stopwords]
    word_counts = Counter(filtered_words)
    return word_counts.most_common(top_n)

# Core Functionality
def process_text():
    input_text = text_area.get("1.0", END).strip()  # Get input from the user
    words = re.findall(r"\b\w+\b", input_text, re.UNICODE)

    # Process the text
    stemmed_words, misspelled_words = check_spelling_and_stem(words)
    category = classify_text(input_text)
    common_words = most_common_words(stemmed_words)

    # Display Results
    output_text.delete("1.0", END)
    output_text.insert(END, "=== Analysis Results ===\n")
    output_text.insert(END, f"Category: {category.title()}\n\n")

    output_text.insert(END, "Most Common Words:\n")
    for word, count in common_words:
        output_text.insert(END, f"{word}: {count}\n")

    output_text.insert(END, "\nMisspelled Words:\n")
    for word, suggestions in misspelled_words.items():
        suggestions_text = ", ".join(suggestions) if suggestions else "No suggestions"
        output_text.insert(END, f"{word}: {suggestions_text}\n")

# Tkinter User Interface
root = Tk()
root.title("Mongolian Text Processing Tool")
root.geometry("800x600")

# Input Section
Label(root, text="Enter Mongolian Text:", font=("Arial", 14)).pack(pady=5)
text_area = scrolledtext.ScrolledText(root, wrap=WORD, width=80, height=10, font=("Arial", 12))
text_area.pack(pady=10)

# Process Button
process_button = Button(root, text="Process Text", command=process_text, font=("Arial", 14), bg="green", fg="white")
process_button.pack(pady=10)

# Output Section
Label(root, text="Results:", font=("Arial", 14)).pack(pady=5)
output_text = scrolledtext.ScrolledText(root, wrap=WORD, width=80, height=15, font=("Arial", 12))
output_text.pack(pady=10)

# Run the Tkinter loop
root.mainloop()
