import pandas as pd

# Load the CSV file
df = pd.read_csv('compiled-reviews-w-formulas.csv')

# Copy values from 'email' to 'User Email'
df['User Email'] = df['email']

# Drop the 'email' and 'helper' columns
df = df.drop(['email', 'helper'], axis=1)

# Save the modified DataFrame back to CSV
df.to_csv('revere-reviews.csv', index=False)