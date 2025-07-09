# tests/test_filters.py

from papers_fetcher.filters import is_academic_affiliation, extract_non_academic_authors

def test_is_academic_true():
    assert is_academic_affiliation("Harvard University, Boston, MA")

def test_is_academic_false():
    assert not is_academic_affiliation("Pfizer Inc., New York, NY")

def test_extract_non_academic_authors():
    authors = [
        {"name": "Alice A", "affiliation": "Harvard University"},
        {"name": "Bob B", "affiliation": "Moderna Inc."},
        {"name": "Carol C", "affiliation": "Another Biotech LLC"}
    ]
    names, companies = extract_non_academic_authors(authors)
    assert names == ["Bob B", "Carol C"]
    assert companies == ["Moderna Inc.", "Another Biotech LLC"]
