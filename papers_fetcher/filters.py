# papers_fetcher/filters.py

from typing import List, Tuple, Optional

ACADEMIC_KEYWORDS = [
    "university", "college", "institute", "hospital", "school",
    "center", "centre", "faculty", "dept", "department", "universität"
]

def is_academic_affiliation(affiliation: Optional[str]) -> bool:
    if affiliation is None:
        return True
    affil_lower = affiliation.lower()
    return any(keyword in affil_lower for keyword in ACADEMIC_KEYWORDS)

def extract_non_academic_authors(authors: List[dict]) -> Tuple[List[str], List[str]]:
    non_academic_names = []
    company_names = []

    for author in authors:
        name = author.get("name")
        affiliation = author.get("affiliation")

        if affiliation and not is_academic_affiliation(affiliation):
            non_academic_names.append(name)
            company_names.append(affiliation)

    return non_academic_names, company_names
