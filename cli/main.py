# cli/main.py

import typer
from typing import Optional
from papers_fetcher.fetcher import fetch_pubmed_papers
from papers_fetcher.filters import extract_non_academic_authors
from papers_fetcher.utils import export_to_csv



app = typer.Typer(help="Fetch PubMed papers with non-academic authors.")

@app.command()
def get_papers_list(
    query: str = typer.Argument(..., help="PubMed search query"),
    file: Optional[str] = typer.Option(None, "--file", "-f", help="Output CSV filename"),
    debug: bool = typer.Option(False, "--debug", "-d", help="Enable debug output")
):
    """
    Fetches papers matching the query and writes results to CSV (or prints to console).
    """
    if debug:
        typer.echo("[DEBUG] Debug mode is ON")
        typer.echo(f"[DEBUG] Query: {query}")
        typer.echo(f"[DEBUG] Output file: {file if file else 'stdout'}")

    typer.echo(f"Fetching papers for query: '{query}'")
    # We'll add real logic here next
    # typer.echo("🚧 This feature is under construction 🚧")
    papers = fetch_pubmed_papers(query, debug=debug)
    typer.echo(f"Found {len(papers)} papers.")
    # for paper in papers:
    #     # typer.echo(f"- {paper['title']} ({paper['pubmed_id']})")
    #     non_acad_authors, companies = extract_non_academic_authors(paper["authors"])
    #     if non_acad_authors:
    #         typer.echo(f"\n📄 {paper['title']} ({paper['pubmed_id']})")
    #         typer.echo(f"🗓  Published: {paper['publication_date']}")
    #         typer.echo(f"👨‍🔬 Non-Academic Authors: {', '.join(non_acad_authors)}")
    #         typer.echo(f"🏢 Companies: {', '.join(companies)}")
    #         if paper.get("email"):
    #             typer.echo(f"📧 Corresponding Email: {paper['email']}")
    filtered_papers = []

    for paper in papers:
        non_acad_authors, companies = extract_non_academic_authors(paper["authors"])
        if non_acad_authors:
            paper["non_acad_authors"] = non_acad_authors
            paper["companies"] = companies
            filtered_papers.append(paper)

            # Console output
            typer.echo(f"\n📄 {paper['title']} ({paper['pubmed_id']})")
            typer.echo(f"🗓  Published: {paper['publication_date']}")
            typer.echo(f"👨‍🔬 Non-Academic Authors: {', '.join(non_acad_authors)}")
            typer.echo(f"🏢 Companies: {', '.join(companies)}")
            if paper.get("email"):
                typer.echo(f"📧 Corresponding Email: {paper['email']}")

    if file:
        export_to_csv(filtered_papers, file)
        typer.echo(f"\n✅ Saved results to: {file}")






def main():
    app()

if __name__ == "__main__":
    main()
