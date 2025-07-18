import pandas as pd

df = pd.read_csv('INSERT CSV HERE.csv')

french_review_ids = ['ARRAY, OF, REVIEW, IDS']

df['Locale'] = df['Review ID'].apply(lambda x: 'fr_CA' if str(x) in french_review_ids else 'en_US')

df.to_csv('NEW FILE NAME HERE.csv', index=False)
