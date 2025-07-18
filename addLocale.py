import pandas as pd

df = pd.read_csv('google-reviews-with-emails.csv')

french_review_ids = ['522906cf-a0b6-4d7d-ad93-beb53505b8b1', '0c772dc4-a550-48d3-a98e-75d7d970e140', '8bda66cb-2fa1-4eaa-a132-3fa1ceac644f', '97871901-08dd-4815-940f-fc8fa672efb2', 'd07a678d-de86-471c-827e-f82dd2add915', '1ee5777a-3bd2-482a-9c7b-b6fbfbef4ba3', 'f3c31257-7d4e-4f96-b81b-b5fc237a8756', '0449a7e3-b768-4250-9840-cbe3ee42a2a9', '0af5b758-4576-479b-bd09-07aa8dd8981c', '88052e7e-f6f3-4ac8-869c-c5e60326d3f7', '60e23b78-b4f2-45f4-be56-1c58bbd491fc', '291a61ae-2243-4e4f-b317-5976244fe854', 'a2b0314d-bc08-4c89-b25e-4afa34324327']

df['Locale'] = df['Review ID'].apply(lambda x: 'fr_CA' if str(x) in french_review_ids else 'en_US')

df.to_csv('google-reviews-with-locale.csv', index=False)
