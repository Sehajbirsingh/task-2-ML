import requests
from bs4 import BeautifulSoup

def scrape_wikipedia(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the title
    title = soup.find(id="firstHeading").text
    
    # Extract the first paragraph (usually a brief description)
    description = soup.find('p', class_='').text
    
    return title, description

# URL of the Wikipedia page to scrape
url = "https://en.wikipedia.org/wiki/Web_scraping"

# Perform the scraping
title, description = scrape_wikipedia(url)

# Print the results
print(f"Title: {title}")
print(f"Description: {description}")

# Save the results to a text file
with open('scraping_results.txt', 'w', encoding='utf-8') as f:
    f.write(f"Title: {title}\n\n")
    f.write(f"Description: {description}")

print("Results have been saved to 'scraping_results.txt'")