# papers_fetcher/utils.py

import re
from typing import Optional
import csv
from typing import List, Dict

EMAIL_REGEX = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

def extract_email(text: Optional[str]) -> Optional[str]:
    if not text:
        return None
    match = re.search(EMAIL_REGEX, text)
    return match.group(0) if match else None


def export_to_csv(
    papers: List[Dict],
    filename: str
) -> None:
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=[
            "PubmedID",
            "Title",
            "Publication Date",
            "Non-academic Author(s)",
            "Company Affiliation(s)",
            "Corresponding Author Email"
        ])
        writer.writeheader()

        for paper in papers:
            writer.writerow({
                "PubmedID": paper["pubmed_id"],
                "Title": paper["title"],
                "Publication Date": paper["publication_date"],
                "Non-academic Author(s)": ", ".join(paper["non_acad_authors"]),
                "Company Affiliation(s)": ", ".join(paper["companies"]),
                "Corresponding Author Email": paper.get("email") or "N/A"
            })
