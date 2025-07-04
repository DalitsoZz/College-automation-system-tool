import re
import os
import zipfile
import fitz  # PyMuPDF
import xml.etree.ElementTree as ET
from urllib.parse import urlparse
from typing import List
import requests
from dotenv import load_dotenv

load_dotenv()

class DocumentExtractor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.extension = os.path.splitext(file_path)[-1].lower()

        if self.extension == '.docx':
            if not os.path.exists(file_path):
                raise FileNotFoundError(f'File not found: {file_path}')
            self._nsmap = {
                'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
            self._doc_zip = self.__unzip(file_path)
            self.filelist = self._doc_zip.namelist()

        elif self.extension == '.pdf':
            if not os.path.exists(file_path):
                raise FileNotFoundError(f'File not found: {file_path}')
        else:
            raise ValueError(f"Unsupported file extension: {self.extension}")

    def __unzip(self, path):
        return zipfile.ZipFile(path)

    def __qn(self, tag: str) -> str:
        prefix, tagroot = tag.split(':')
        uri = self._nsmap[prefix]
        return f'{{{uri}}}{tagroot}'

    def __xml2text(self, xml: str) -> str:
        text = u""
        root = ET.fromstring(xml)
        for child in root.iter():
            if child.tag == self.__qn('w:t'):
                text += child.text if child.text else ''
            elif child.tag == self.__qn('w:tab'):
                text += '\t'
            elif child.tag in (self.__qn('w:br'), self.__qn('w:cr')):
                text += '\n'
            elif child.tag == self.__qn('w:p'):
                text += '\n\n'
        return text

    def extract_text(self) -> str:
        if self.extension == '.pdf':
            return self._extract_pdf_text()
        elif self.extension == '.docx':
            return self._extract_docx_text()

    def _extract_pdf_text(self) -> str:
        print(f"Opening PDF: {self.file_path} - Exists: {os.path.exists(self.file_path)}")
        text = ""
        try:
            with fitz.open(self.file_path) as doc:
                for page in doc:
                    text += page.get_text() + "\n"
        except Exception as e:
            print(f"Error opening PDF: {e}")
            raise
        return text.strip()

    def _extract_docx_text(self) -> str:
        raw_xml = self._doc_zip.read("word/document.xml")
        text = self.__xml2text(raw_xml)
        return re.sub(r"\n{1,}", "\n", text).strip()

    def extract_urls(self) -> List[str]:
        if self.extension == '.docx':
            words = self._doc_zip.read('word/document.xml').decode('utf-8').split()
        elif self.extension == '.pdf':
            words = self._extract_pdf_text().split()
        else:
            return []

        urls = []
        for word in words:
            parsed_url = urlparse(word)
            if parsed_url.scheme and parsed_url.netloc:
                urls.append(word)
        return urls

    def close(self):
        if self.extension == '.docx':
            self._doc_zip.close()

    def detect_ai_content(self, text: str) -> dict:
        """
        Calls the external AI content detector API with the given text.
        Returns the API response as a dictionary.
        """
        url = 'https://ai-content-detector-ai-gpt.p.rapidapi.com/api/detectText/'
        headers = {
            'x-rapidapi-key': os.environ.get('RAPIDAPI_KEY'),
            'x-rapidapi-host': 'ai-content-detector-ai-gpt.p.rapidapi.com',
            'Content-Type': 'application/json',
        }
        try:
            response = requests.post(url, json={'text': text}, headers=headers)
            return response.json()
        except Exception as e:
            return {'error': str(e)}


# Example usage for testing locally
if __name__ == '__main__':
    # Set your local PDF or DOCX file path here
    path = "path/to/your/file.pdf"

    extractor = DocumentExtractor(path)
    text = extractor.extract_text()
    print(text[:1000])
    extractor.close()
