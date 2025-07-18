import pandas as pd
from langdetect import detect, LangDetectException

# Load the CSV file
df = pd.read_csv('google-reviews.csv')

def detect_locale(text):
    try:
        if pd.isnull(text) or not isinstance(text, str) or text.strip() == "":
            return "en_US"  # Default to English if empty or not a string
        lang = detect(text)
        if lang == 'fr':
            return "fr_CA"
        else:
            return "en_US"
    except LangDetectException:
        return "en_US"

# Apply the function to the Review Text column
df['Locale'] = df['Review Text'].apply(detect_locale)

# Save the updated CSV
df.to_csv('google-reviews-with-locale.csv', index=False)