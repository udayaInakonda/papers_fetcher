# tests/test_utils.py

from papers_fetcher.utils import extract_email

def test_extract_email_found():
    text = "Biotech Inc., Palo Alto, CA. Contact: jane.doe@biotech.com"
    assert extract_email(text) == "jane.doe@biotech.com"

def test_extract_email_missing():
    text = "Biotech Inc., no contact info here"
    assert extract_email(text) is None

def test_extract_email_empty():
    assert extract_email("") is None
