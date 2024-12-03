import re
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import time

def extract_arxiv_ids(readme_content):
    """Extract arXiv IDs from various URL formats in the README."""
    # Pattern matches both PDF and abstract URLs
    patterns = [
        r'arxiv\.org/(?:pdf|abs)/(\d{4}\.\d{4,5})',
        r'arxiv\.org/(?:pdf|abs)/[a-z-]+/(\d{7})',  # For old arXiv IDs
        r'(\d{4}\.\d{4,5})'  # Bare arXiv IDs
    ]
    
    ids = set()
    for pattern in patterns:
        matches = re.finditer(pattern, readme_content, re.IGNORECASE)
        ids.update(match.group(1) for match in matches)
    
    return sorted(list(ids))

def fetch_arxiv_metadata(arxiv_id):
    """Fetch metadata for a single arXiv ID using the arXiv API."""
    base_url = 'http://export.arxiv.org/api/query?'
    query = f'id_list={arxiv_id}'
    url = base_url + query
    
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read().decode('utf-8')
        return data
    except Exception as e:
        print(f"Error fetching metadata for {arxiv_id}: {e}")
        return None

def parse_xml_to_bibtex(xml_data, arxiv_id):
    """Parse arXiv API XML response into BibTeX format."""
    try:
        root = ET.fromstring(xml_data)
        # Define XML namespaces
        ns = {
            'atom': 'http://www.w3.org/2005/Atom',
            'arxiv': 'http://arxiv.org/schemas/atom'
        }
        
        # Extract entry data
        entry = root.find('atom:entry', ns)
        if entry is None:
            return None
        
        title = entry.find('atom:title', ns).text.strip().replace('\n', ' ')
        authors = [author.find('atom:name', ns).text for author in entry.findall('atom:author', ns)]
        published = entry.find('atom:published', ns).text[:4]  # Get year
        categories = entry.findall('atom:category', ns)
        primary_category = entry.find('arxiv:primary_category', ns).get('term')
        
        # Create author string and key
        author_string = ' and '.join(authors)
        first_author_last_name = authors[0].split()[-1].lower()
        bibtex_key = f"{first_author_last_name}{published}{arxiv_id.replace('.', '')}"
        
        # Format BibTeX entry
        bibtex = f"""@misc{{{bibtex_key},
    title = {{{title}}},
    author = {{{author_string}}},
    year = {{{published}}},
    eprint = {{{arxiv_id}}},
    archivePrefix = {{arXiv}},
    primaryClass = {{{primary_category}}}
}}"""
        return bibtex
    except Exception as e:
        print(f"Error parsing XML for {arxiv_id}: {e}")
        return None

def main(readme_path):
    """Main function to process README and generate BibTeX entries."""
    # Read README file
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract arXiv IDs
    arxiv_ids = extract_arxiv_ids(content)
    print(f"Found {len(arxiv_ids)} arXiv IDs")
    
    # Fetch and process each ID
    bibtex_entries = []
    for arxiv_id in arxiv_ids:
        print(f"Processing {arxiv_id}...")
        xml_data = fetch_arxiv_metadata(arxiv_id)
        if xml_data:
            bibtex = parse_xml_to_bibtex(xml_data, arxiv_id)
            if bibtex:
                bibtex_entries.append(bibtex)
            # Be nice to the arXiv API
            time.sleep(3)
    
    # Write results to file
    with open('arxiv_bibtex.bib', 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(bibtex_entries))
    
    print(f"\nProcessed {len(bibtex_entries)} entries successfully")
    print("Results written to arxiv_bibtex.bib")

if __name__ == "__main__":
    readme_path = "../README.md"  # Update this path as needed
    main(readme_path)
