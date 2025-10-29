#!/usr/bin/env python3
"""
Generate taxonomy from QFDMO categories JSON file.

This script reads the qfdmo.json file and generates a taxonomy
in the format used by Open Products Facts (similar to categories.txt).
"""

import json
import sys
from collections import defaultdict
from typing import Dict, List, Set


def load_qfdmo_data(filename: str) -> List[Dict]:
    """Load QFDMO data from JSON file."""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)


def extract_categories_and_items(data: List[Dict]) -> tuple:
    """
    Extract categories and items from QFDMO data.
    
    Returns:
        tuple: (category_items, all_categories)
            - category_items: dict mapping category -> list of items
            - all_categories: set of all category codes
    """
    category_items = defaultdict(list)
    all_categories = set()
    
    for entry in data:
        fields = entry.get('fields', {})
        sous_categories = fields.get('sous_categorie', [])
        
        if sous_categories:
            for cat in sous_categories:
                all_categories.add(cat)
                category_items[cat].append({
                    'libelle': fields.get('libelle'),
                    'code': fields.get('code'),
                    'id': fields.get('identifiant_qfdmod')
                })
    
    return category_items, all_categories


def format_category_name(code: str) -> str:
    """
    Convert a category code to a readable name.
    
    Example: 'gros_electromenager_hors_refrigerant' -> 'Gros électroménager hors réfrigérant'
    """
    # Replace underscores with spaces
    name = code.replace('_', ' ')
    
    # Capitalize first letter of each word
    words = name.split()
    formatted_words = []
    
    for word in words:
        # Special handling for common abbreviations
        if word.upper() in ['RFID', 'USB', 'GPS', 'DVD', 'CD', 'IPL', 'WC', 'BA13']:
            formatted_words.append(word.upper())
        elif word in ['et', 'de', 'du', 'pour', 'a', 'en']:  # French articles/prepositions
            formatted_words.append(word)
        else:
            formatted_words.append(word.capitalize())
    
    return ' '.join(formatted_words)


def generate_taxonomy_header() -> str:
    """Generate the taxonomy file header."""
    return """# QFDMO Categories Taxonomy
# Generated from qfdmo.json
# QFDMO: Où et comment donner, réparer et recycler tous vos objets
# https://www.ecosystem.eco/fr/qfdmo
#
# Format:
# - Each category starts with its code
# - fr: French name (libelle from the data)
# - Items under each category are listed with their codes
# - Parent-child relationships use < fr: Parent Category
#

"""


def generate_taxonomy(category_items: Dict, all_categories: Set) -> str:
    """
    Generate the taxonomy content.
    
    Args:
        category_items: dict mapping category -> list of items
        all_categories: set of all category codes
        
    Returns:
        str: Formatted taxonomy content
    """
    output = []
    
    # Sort categories alphabetically
    sorted_categories = sorted(all_categories)
    
    for category_code in sorted_categories:
        # Category header
        output.append(f"#")
        output.append(f"fr: {format_category_name(category_code)}")
        output.append(f"code: {category_code}")
        
        # List items in this category
        items = category_items.get(category_code, [])
        if items:
            output.append(f"# Items in this category: {len(items)}")
            
        output.append("")  # Empty line between categories
    
    return '\n'.join(output)


def generate_items_list(category_items: Dict, all_categories: Set) -> str:
    """
    Generate a detailed list of items per category.
    
    Args:
        category_items: dict mapping category -> list of items
        all_categories: set of all category codes
        
    Returns:
        str: Formatted items list
    """
    output = []
    output.append("\n# DETAILED ITEMS LIST\n#")
    
    sorted_categories = sorted(all_categories)
    
    for category_code in sorted_categories:
        items = category_items.get(category_code, [])
        if not items:
            continue
            
        output.append(f"\n## {format_category_name(category_code)} ({category_code})")
        output.append(f"# {len(items)} items\n")
        
        # Sort items by libelle
        sorted_items = sorted(items, key=lambda x: x.get('libelle', ''))
        
        for item in sorted_items:
            libelle = item.get('libelle', 'Unknown')
            code = item.get('code', 'unknown')
            item_id = item.get('id', 'N/A')
            
            output.append(f"< fr: {format_category_name(category_code)}")
            output.append(f"fr: {libelle}")
            output.append(f"code: {code}")
            if item_id is not None:
                output.append(f"identifiant_qfdmod: {item_id}")
            output.append("")
    
    return '\n'.join(output)


def main():
    """Main function to generate the taxonomy."""
    input_file = 'qfdmo.json'
    output_file = 'qfdmo_taxonomy.txt'
    
    # Allow command-line arguments
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    
    try:
        # Load data
        print(f"Loading data from {input_file}...")
        data = load_qfdmo_data(input_file)
        print(f"Loaded {len(data)} entries")
        
        # Extract categories and items
        print("Extracting categories and items...")
        category_items, all_categories = extract_categories_and_items(data)
        print(f"Found {len(all_categories)} categories")
        
        # Generate taxonomy
        print("Generating taxonomy...")
        header = generate_taxonomy_header()
        taxonomy = generate_taxonomy(category_items, all_categories)
        items_list = generate_items_list(category_items, all_categories)
        
        # Write to file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(header)
            f.write(taxonomy)
            f.write(items_list)
        
        print(f"Taxonomy generated successfully: {output_file}")
        print(f"  - {len(all_categories)} categories")
        print(f"  - {len(data)} total items")
        
        # Print some statistics
        print("\nTop 10 categories by number of items:")
        sorted_by_count = sorted(
            category_items.items(),
            key=lambda x: len(x[1]),
            reverse=True
        )[:10]
        
        for cat, items in sorted_by_count:
            print(f"  {format_category_name(cat)}: {len(items)} items")
        
    except FileNotFoundError:
        print(f"Error: Could not find file '{input_file}'")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in '{input_file}': {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
