import csv
import sys
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

csv.field_size_limit(sys.maxsize)

# File paths
file_reviews_emails = 'reviews-with-emails.csv'
file_google_reviews = 'google-reviews-with-locale.csv'
output_file = 'compiled-reviews.csv'

# Column mapping
mapping = [
    ('check_score', 'Rating'),
    ('check_item_id', 'Page ID'),
    ('check_nickname', 'Review Display'),
    ('check_title', 'Review Title'),
    ('check_content', 'Review Text')
]

def normalize(value):
    return value.strip().lower() if isinstance(value, str) else ''

# Read reviews-with-emails.csv into a list of dicts
with open(file_reviews_emails, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    reviews_emails = list(reader)

# Build a lookup dictionary for fast matching
lookup = {}
for row in reviews_emails:    
    key = tuple(normalize(row.get(src, '')) for src, _ in mapping)
    lookup[key] = row.get('email', '')

# Read google-reviews-with-locale.csv and process
with open(file_google_reviews, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    google_reviews = list(reader)
    google_headers = reader.fieldnames

# Add 'email' to headers if not present
if 'email' not in google_headers:
    google_headers.append('email')

# Create a list of keys for fuzzy matching
lookup_keys = list(lookup.keys())
lookup_key_strs = ['|'.join(k) for k in lookup_keys]

# Match and assign email using fuzzy matching
for row in google_reviews:
    key = tuple(normalize(row.get(dst, '')) for _, dst in mapping)
    key_str = '|'.join(key)
    match, score = process.extractOne(key_str, lookup_key_strs, scorer=fuzz.token_sort_ratio)
    if score > 90:  # Adjust threshold as needed
        matched_key = tuple(match.split('|'))
        row['email'] = lookup.get(matched_key, '')
    else:
        row['email'] = ''

# Write the output
with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=google_headers)
    writer.writeheader()
    writer.writerows(google_reviews)

print(f"Done! Output saved to {output_file}")