import bibtexparser
from pylatexenc.latex2text import LatexNodes2Text

def latex_to_unicode(text):
    """Convert LaTeX-formatted text to Unicode."""
    return LatexNodes2Text().latex_to_text(text) if text else ""

def format_authors(authors):
    """Format authors list, making 'Yun-Chih Chen' bold."""
    if not authors:
        return "Unknown Authors"
    formatted_authors = []
    for author in authors.split(' and '):
        author_name = latex_to_unicode(author.strip())
        formatted_authors.append(author_name)
    return ', '.join(formatted_authors)

def bibtex_to_hugo(bibtex_file):
    """Convert BibTeX entries to Hugo shortcode format."""
    with open(bibtex_file, 'r', encoding='utf-8') as bibtex_fp:
        bib_database = bibtexparser.load(bibtex_fp)

    # Sort entries by year (descending)
    sorted_entries = sorted(
        bib_database.entries,
        key=lambda entry: int(entry.get('year', '0')),
        reverse=True
    )

    for entry in sorted_entries:
        authors = format_authors(entry.get('author', 'Unknown Authors'))
        title = latex_to_unicode(entry.get('title', 'No Title'))
        conference = latex_to_unicode(entry.get('booktitle', entry.get('journal', 'No Venue')))
        year = entry.get('year', 'No Year')

        print("- {{< publication")
        print(f'    authors="{authors}"')
        print(f'    title="{title}"')
        print(f'    conference="{conference}"')
        print(f'    year="{year}" >}}}}')

# Example usage
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_bibtex_file>")
    else:
        bibtex_file = sys.argv[1]
        bibtex_to_hugo(bibtex_file)