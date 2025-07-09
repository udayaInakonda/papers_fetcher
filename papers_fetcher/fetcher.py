# papers_fetcher/fetcher.py

import requests
from lxml import etree
from typing import List, Dict
from papers_fetcher.utils import extract_email


BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
MAX_RESULTS = 20  # You can increase this later

def fetch_pubmed_papers(query: str, debug: bool = False) -> List[Dict]:
    # Step 1: Use esearch to get paper IDs
    search_url = BASE_URL + "esearch.fcgi"
    search_params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": MAX_RESULTS
    }
    search_response = requests.get(search_url, params=search_params)
    if debug:
        print("[DEBUG] esearch URL:", search_response.url)
    search_data = search_response.json()
    id_list = search_data["esearchresult"]["idlist"]

    if not id_list:
        return []

    # Step 2: Use efetch to get paper details
    fetch_url = BASE_URL + "efetch.fcgi"
    fetch_params = {
        "db": "pubmed",
        "id": ",".join(id_list),
        "retmode": "xml"
    }
    fetch_response = requests.get(fetch_url, params=fetch_params)
    if debug:
        print("[DEBUG] efetch URL:", fetch_response.url)

    root = etree.fromstring(fetch_response.content)
    papers = []

    for article in root.xpath("//PubmedArticle"):
        paper = {
            "pubmed_id": None,
            "title": None,
            "publication_date": None,
            "authors": []
        }

        # PubMed ID
        pmid = article.findtext(".//PMID")
        paper["pubmed_id"] = pmid

        # Title
        title = article.findtext(".//ArticleTitle")
        paper["title"] = title

        # Publication Date
        pubdate_elem = article.find(".//PubDate")
        if pubdate_elem is not None:
            year = pubdate_elem.findtext("Year") or "n.d."
            paper["publication_date"] = year

        # Authors
        # authors = []
        # for author in article.findall(".//Author"):
        #     name_parts = []
        #     lastname = author.findtext("LastName")
        #     initials = author.findtext("Initials")
        #     if lastname:
        #         name_parts.append(lastname)
        #     if initials:
        #         name_parts.append(initials)

        #     full_name = " ".join(name_parts).strip()
        #     affiliation = author.findtext(".//AffiliationInfo/Affiliation")
        #     authors.append({
        #         "name": full_name,
        #         "affiliation": affiliation
        #     })

        # paper["authors"] = authors
        # papers.append(paper)
                # Authors
        authors = []
        corresponding_email = None  # New!

        for author in article.findall(".//Author"):
            name_parts = []
            lastname = author.findtext("LastName")
            initials = author.findtext("Initials")
            if lastname:
                name_parts.append(lastname)
            if initials:
                name_parts.append(initials)

            full_name = " ".join(name_parts).strip()
            affiliation = author.findtext(".//AffiliationInfo/Affiliation")

            # Try to extract email from this affiliation
            if not corresponding_email:
                corresponding_email = extract_email(affiliation)

            authors.append({
                "name": full_name,
                "affiliation": affiliation
            })

        paper["authors"] = authors
        paper["email"] = corresponding_email  # Add this
        papers.append(paper)

    return papers
