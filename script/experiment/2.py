import re
import nltk
import pandas as pd
import unidecode
import num2words
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Download NLTK Pre-trained models
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")

# path to Parquet file
dataset = pd.read_parquet("../data/imdb/plain_text/test-00000-of-00001.parquet")
# Access text data (assuming column name is 'text')
text_data = dataset["text"]
# Access class label data (assuming column name is 'label')
class_labels = dataset["label"]


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

    # Remove punctuation and non-alphanumeric characters ,HTML tags ,URLs
    patterns = [r"https?://\S+", r"<.*?>"]

    def remove_elements(text, pattern):
        for pattern in patterns:
            text = re.sub(pattern, "", text)
        return text

    text = list(map(lambda x: remove_elements(text, patterns), [text]))[0]

    # Number replacement with words library
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


# Preprocess text data
preprocessed_text = []
for review in text_data:
    preprocessed_text.append(preprocess_review(review))

# Convert preprocessed data to pandas data frame
df = pd.DataFrame(
    {
        "original_text": text_data,
        "preprocessed_text": preprocessed_text,
        "label": class_labels,
    }
)
# Save as CSV
df.to_csv("preprocessed_data-2.csv", index=False)  # Save as CSV
