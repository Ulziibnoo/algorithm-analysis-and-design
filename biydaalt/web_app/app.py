from flask import Flask, request, jsonify, render_template
import re
from collections import Counter
from difflib import get_close_matches
import unicodedata
import logging

app = Flask(__name__)

# Setup logging for missing words
logging.basicConfig(filename='error.log', level=logging.ERROR)

# Load dictionary and affix file
def load_dictionary_and_affix():
    words = set()
    try:
        # Load dictionary file
        with open('mn_MN.dic', 'r', encoding='utf-8') as dic_file:
            next(dic_file)  # Skip metadata count
            for line in dic_file:
                word = line.strip().split('/')[0]
                normalized_word = normalize_text(word)
                if normalized_word and len(normalized_word) > 1:  # Skip invalid entries
                    words.add(normalized_word)
    except Exception as e:
        print(f"Error loading dictionary: {e}")
    return words

# Normalize text for consistent comparison
def normalize_text(text):
    return unicodedata.normalize("NFC", text).lower()

# Enhanced word suggestion algorithm considering suffixes
def suggest_words(word):
    """Enhanced word suggestion algorithm"""
    word = normalize_text(word)
    base_word = get_base_word(word)  # Get base word if it's a suffixed word
    if base_word in MONGOLIAN_WORDS:
        return [base_word]
    suggestions = get_close_matches(base_word, MONGOLIAN_WORDS, n=5, cutoff=0.7)
    return suggestions

# Get base word if the word ends with suffixes
def get_base_word(word):
    for suffix in TIIN_YALGAL_SUFFIXES:
        if word.endswith(suffix):
            base_word = word[:-len(suffix)]
            if base_word in MONGOLIAN_WORDS:
                return base_word
    return word

# Check if word or its base form with suffix is valid
def is_valid_with_case_suffix(word):
    """
    Checks if the word or its base form with suffixes is valid.
    """
    base_word = get_base_word(word)
    if base_word in MONGOLIAN_WORDS:
        return True
    return False

# Initialize global variables
MONGOLIAN_WORDS = load_dictionary_and_affix()

# Common Mongolian stop words
STOP_WORDS = set(['юм', 'бөгөөд', 'ба', 'гэх', 'мөн', 'нь', 'энэ', 'тэр', 'байна', 'болон'])

# Define text categories with related keywords
CATEGORIES = {
    'эдийн засаг': ['мөнгө', 'банк', 'зах зээл', 'эдийн засаг', 'бизнес', 'төгрөг', 'валют', 'хөрөнгө'],
    'спорт': ['хөл бөмбөг', 'тэмцээн', 'медаль', 'тамирчин', 'спорт', 'бөмбөг', 'наадам', 'барилдаан'],
    'улс төр': ['засгийн газар', 'парламент', 'сонгууль', 'улс төр', 'гишүүн', 'хурал', 'төрийн'],
    'боловсрол': ['сургууль', 'оюутан', 'багш', 'боловсрол', 'сурагч', 'хичээл'],
}

# Тийн ялгалын дагаврууд
TIIN_YALGAL_SUFFIXES = [
    "ын", "ийн", "ны", "ний",  # Өмчлөх (Genitive)
    "д", "т",                  # Өгөх орших (Dative)
    "ыг", "ийг",               # Үйлдүүлэх (Accusative)
    "аар", "ээр", "оор", "өөр",  # Хэрэглэх (Instrumental)
    "аас", "ээс", "оос", "өөс",  # Гарах (Ablative)
    "тай", "тэй", "той",       # Хамтрах (Comitative)
    "дээр", "доор", "урд", "хойд", "дотор", "гадна"  # Орон зайн илэрхийлэл
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_text():
    data = request.get_json()
    text = data.get('text', '')

    if not text.strip():
        return jsonify({
            'misspelled': [],
            'unique_words': 0,
            'top_words': [],
            'category': 'бусад'
        })

    misspelled = []
    words = re.finditer(r'[а-яөүёА-ЯӨҮЁ]+(?:-[а-яөүёА-ЯӨҮЁ]+)?', text)

    for match in words:
        word = normalize_text(match.group())
        start, end = match.start(), match.end()

        if len(word) > 1 and not is_valid_with_case_suffix(word):
            suggestions = suggest_words(word)
            misspelled.append({
                'word': word,
                'start': start,
                'end': end,
                'suggestions': suggestions
            })

    raw_words = re.findall(r'[а-яөүёА-ЯӨҮЁ]+(?:-[а-яөүёА-ЯӨҮЁ]+)?', text)
    normalized_words = [normalize_text(word) for word in raw_words]
    meaningful_words = [word for word in normalized_words if word not in STOP_WORDS and len(word) > 1]

    unique_words = len(set(meaningful_words))
    word_freq = Counter(meaningful_words)
    top_words = word_freq.most_common(10)

    category = classify_text(text)

    return jsonify({
        'misspelled': misspelled,
        'unique_words': unique_words,
        'top_words': top_words,
        'category': category
    })

def classify_text(text):
    text_lower = normalize_text(text)
    max_score = 0
    text_category = 'бусад'

    for category, keywords in CATEGORIES.items():
        score = sum(1 for keyword in keywords if keyword in text_lower)
        if score > max_score:
            max_score = score
            text_category = category

    return text_category

if __name__ == '__main__':
    app.run(debug=True)
