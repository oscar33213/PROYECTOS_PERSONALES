import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime

class WebCrawler:
    def __init__(self, url, output_dir="resultados"):
        self.url = url
        self.output_dir = output_dir
        self.html_content = ""
        self.soup = None
        self.spans = []
        self.css_blocks = []

    def fetch_html(self):
        response = requests.get(self.url)
        response.raise_for_status()
        self.html_content = response.text
        self.soup = BeautifulSoup(self.html_content, "html.parser")

    def extract_spans(self):
        self.spans = [
            {"texto": span.get_text(strip=True), "html": str(span)}
            for span in self.soup.find_all("span")
        ]

    def extract_css(self):
        self.css_blocks = []
        for link in self.soup.find_all("link", rel="stylesheet"):
            css_url = link.get("href")
            if css_url and not css_url.startswith("http"):
                css_url = requests.compat.urljoin(self.url, css_url)
            try:
                css_resp = requests.get(css_url)
                self.css_blocks.append(css_resp.text)
            except Exception as e:
                self.css_blocks.append(f"Error al obtener CSS: {e}")

        for style in self.soup.find_all("style"):
            self.css_blocks.append(style.get_text())

    def save_to_file(self):
        os.makedirs(self.output_dir, exist_ok=True)
        filename = f"extract_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        filepath = os.path.join(self.output_dir, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write("=== SPANS EXTRAÍDOS ===\n")
            for span in self.spans:
                f.write(f"Texto: {span['texto']}\n")
                f.write(f"HTML: {span['html']}\n\n")

            f.write("\n=== CSS BLOQUES ===\n")
            for css in self.css_blocks:
                f.write(css + "\n")

        print(f"Archivo creado: {filepath}")

    def run(self):
        self.fetch_html()
        self.extract_spans()
        self.extract_css()
        self.save_to_file()


if __name__ == "__main__":
    url = input("Introduce la URL: ")
    crawler = WebCrawler(url)
    crawler.run()
