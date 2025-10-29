# QFDMO Taxonomy Generator

This directory contains a Python script to generate a taxonomy from QFDMO (Que Faire De Mes Objets) categories.

## About QFDMO

QFDMO (Que Faire De Mes Objets / What to Do with My Objects) is a French initiative by Ecosystem to help people find where to donate, repair, and recycle their objects.

Website: https://www.ecosystem.eco/fr/qfdmo

## Files

- `qfdmo.json` - Source data in Django fixture format containing 866 objects categorized into 51 categories
- `generate_qfdmo_taxonomy.py` - Python script to generate taxonomy from the JSON data
- `qfdmo_taxonomy.txt` - Generated taxonomy file (output)

## Usage

### Basic Usage

```bash
python3 generate_qfdmo_taxonomy.py
```

This will:
1. Read `qfdmo.json` 
2. Extract categories and items
3. Generate `qfdmo_taxonomy.txt`

### Custom Files

```bash
python3 generate_qfdmo_taxonomy.py input.json output.txt
```

## Generated Taxonomy Format

The generated taxonomy file follows a hierarchical format:

```
# Header with metadata

# Category sections
#
fr: Category Name
qfdmo_name_fr: category_code
# Items in this category: N

# Detailed items list
## Category Name (category_code)
# N items

< fr: Parent Category
fr: Item Name
qfdmo_name_fr: item_code
identifiant_qfdmo: ID
```

## Data Structure

### Input (qfdmo.json)

```json
{
  "model": "qfdmo.objet",
  "fields": {
    "libelle": "Item Label",
    "code": "item_code",
    "sous_categorie": ["category_code"],
    "identifiant_qfdmod": 123
  }
}
```

### Output Fields

- `fr:` - French label/name
- `qfdmo_name_fr:` - QFDMO code identifier
- `identifiant_qfdmo:` - QFDMO numeric identifier (optional)
- `< fr:` - Parent category reference

## Statistics

The current QFDMO dataset contains:

- **51 categories**
- **866 items**

Top categories by item count:
1. Matériel de sport hors vélo: 211 items
2. Meuble: 172 items
3. Petit électroménager: 64 items
4. Décoration: 62 items
5. Jouet: 51 items

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## License

This taxonomy is derived from QFDMO data by Ecosystem.
