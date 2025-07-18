import xml.etree.ElementTree as ET
import csv
import os

tree = ET.parse('c:/Users/cspears/OneDrive - genesco.com/Documents - JYS_Ecommerce/VS Code/RevereParser/google-reviews.xml')
root = tree.getroot()

with open ('google-reviews.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(["Review ID", "Page ID", "Review Display", "Review Title", "Review Date", "Review Location", "Review Text", "Rating", "Verified Buyer", "User Email", "Images"])
    
    # Iterate through each review
    for review in root.findall('.//review'):
        review_id = review.findtext('review_id')
        page_id = review.find('products/product/product_ids/mpns/mpn').text if review.find('products/product/product_ids/mpns/mpn') is not None else ''
        review_display = review.find('reviewer/name').text if review.find('reviewer/name') is not None else ''
        review_title = review.findtext('title')
        review_date = review.findtext('review_timestamp')
        review_location = 'Undisclosed'
        review_text = review.findtext('content')
        rating = review.find('ratings/overall').text if review.find('ratings/overall') is not None else ''
        verified_buyer = 'No'
        user_email = ''
        urls = [url.text.replace('"', '').replace("'", '') for url in review.findall('.//reviewer_images/reviewer_image/url') if url.text]
        images = '|'.join(urls)

        
        # Write the row
        writer.writerow([
            review_id, page_id, review_display, review_title, review_date, review_location,
            review_text, rating, verified_buyer, user_email, images
        ])