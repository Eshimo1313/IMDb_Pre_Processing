import re
import unidecode
import num2words
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


def preprocess_review(text):
    """
    preprocess the IMdb dataset

    Args:
        text (str): The text of the movie review.

    Returns:
        str: The processed text file
    """
    # Convert to Unicode and remove Accents and Lowercase conversion
    text = unidecode.unidecode(text).lower()

    # Remove punctuation , non-alphanumeric characters , URLs , HTML tags
    # text = text.replace("\n", "")
    pattern = r"\n|([^\w\s\-])|( +)|(https?://\S+)|<.*?>"
    text = re.sub(pattern, " ", text)

    # Number replacement
    text = re.sub(r"\d+", lambda m: num2words.num2words(int(m.group(0))), text)

    # Tokenize
    tokens = word_tokenize(text)

    # Remove stop words
    stop_words = set(stopwords.words("english"))
    tokens = [token for token in tokens if token not in stop_words]

    # lemmatization
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word, pos="v") for word in tokens]

    # Join tokens back into text
    processed_text = " ".join(tokens)

    return processed_text


def count_word(processed_str, word):
    """
    count word occurrence inside given string

    Args:
        processed_str (str): input string
        word (str): string lookup

    Returns:
        init: word occurrence count
    """
    return processed_str.count(word)
