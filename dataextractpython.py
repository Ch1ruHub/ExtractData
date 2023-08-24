import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = 'https://example.com'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the <a> tags (links) on the page
links = soup.find_all('a')

# Print the text and URLs of the links
for link in links:
    link_text = link.get_text()
    link_url = link['href']
    print(f"Link Text: {link_text}\nLink URL: {link_url}\n{'='*30}")

# Save the extracted data to a text file
with open('extracted_links.txt', 'w') as file:
    for link in links:
        link_text = link.get_text()
        link_url = link['href']
        file.write(f"Link Text: {link_text}\nLink URL: {link_url}\n{'='*30}\n")

print("Data extraction and writing complete.")
