import requests
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz
import re

class DocumentIndexer:
    def __init__(self):
        self.index = {}
        self.urls = {
            "Segment": "https://segment.com/docs/connections/sources/#adding-a-source",
            "mParticle": "https://docs.mparticle.com/guides/getting-started/",
            "Lytics": "https://docs.lytics.com/",
            "Zeotap": "https://docs.zeotap.com/introduction/#getting-started"
        }

    def fetch_page(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

    def parse_content(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        content = soup.get_text(separator=' ')
        content = re.sub(r'\s+', ' ', content).strip()
        return content.split('. ')

    def build_index(self):
        for platform, url in self.urls.items():
            html = self.fetch_page(url)
            if html:
                sentences = self.parse_content(html)
                self.index[platform] = sentences
            else:
                self.index[platform] = []

    def search(self, query):
        results = {}
        for platform, sentences in self.index.items():
            best_match = None
            highest_score = 0
            for sentence in sentences:
                score = fuzz.partial_ratio(query.lower(), sentence.lower())
                if score > highest_score and score > 60:  # Lowered threshold
                    highest_score = score
                    best_match = sentence
            if best_match:
                results[platform] = best_match
        return results if results else "I couldn’t find a clear answer. Try rephrasing your question."