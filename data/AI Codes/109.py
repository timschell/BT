import requests
from bs4 import BeautifulSoup

def get_page_title(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.title.string

def main():
    print("Web Page Title Scraper")
    url = input("Enter URL: ")
    title = get_page_title(url)
    print(f"Page Title: {title}")

if __name__ == "__main__":
    main()
