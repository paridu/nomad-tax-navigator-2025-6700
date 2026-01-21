import PyPDF2
import re
import json

class TreatyParser:
    """
    Parses unstructured Tax Treaty PDFs into structured JSON components
    specifically looking for 'Tie-breaker' rules and 'Permanent Establishment' definitions.
    """
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.content = ""

    def extract_text(self):
        with open(self.file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            self.content = " ".join([page.extract_text() for page in reader.pages])

    def identify_residency_article(self):
        # DTAs usually have residency rules in Article 4
        pattern = r"(Article 4|Resident).*?(?=Article 5)"
        match = re.search(pattern, self.content, re.IGNORECASE | re.DOTALL)
        return match.group(0) if match else "Article 4 not found"

    def structure_metadata(self):
        return {
            "source": self.file_path,
            "residency_logic_snippet": self.identify_residency_article()[:500],
            "contains_tie_breaker": "tie-breaker" in self.content.lower()
        }

if __name__ == "__main__":
    # Example usage
    parser = TreatyParser("data/raw/thailand_uk_dta.pdf")
    # parser.extract_text()
    # print(json.dumps(parser.structure_metadata(), indent=2))
    print("TreatyParser initialized for DTA ingestion.")