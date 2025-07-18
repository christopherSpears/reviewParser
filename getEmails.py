import pandas as pd

# Load both files
google_reviews = pd.read_csv('google-reviews.csv', dtype=str)
review_export = pd.read_csv('review-export.csv', dtype=str)

# Fill NaN with empty string for matching
google_reviews = google_reviews.fillna('')
review_export = review_export.fillna('')

# Build lookup dictionary from review-export
lookup = {}
for _, row in review_export.iterrows():
    key = (
        row['Page ID'].strip(),
        row['Review Display'].strip(),
        row['Review Title'].strip(),
        row['Review Text'].strip()
    )
    lookup[key] = row['Reviewer Email']  # or whatever the email column is called

# Update google-reviews with emails
def get_email(row):
    key = (
        row['Page ID'].strip(),
        row['Review Display'].strip(),
        row['Review Title'].strip(),
        row['Review Text'].strip()
    )
    return lookup.get(key, row['User Email'])  # keep existing if not found

google_reviews['User Email'] = google_reviews.apply(get_email, axis=1)

# Save the updated file
google_reviews.to_csv('google-reviews-with-emails.csv', index=False)