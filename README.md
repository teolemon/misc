# Product Attributes Documentation

This repository contains a comprehensive list of product attributes that can be used to describe products across various categories.

## Overview

The attributes have been carefully selected and ranked by their likelihood of being shared across multiple product categories. This makes them universally applicable for product classification, comparison, and data management.

## Files Structure

### attributes.txt
A complete list of all 395 product attributes, ordered by their applicability across categories:
- Most universal attributes (like `brand`, `weight`, `color`) are listed first
- More specialized attributes (like optical or electronic specifications) appear later

### Individual Attribute Documentation Files
Each attribute has its own `.txt` file (e.g., `brand.txt`, `weight.txt`) containing:

1. **Example of usages**: Real-world examples showing how the attribute is used
2. **Possible values**: Description of valid values for this attribute
3. **Source**: Where the attribute information typically comes from
4. **Language fields**: Space for translations (currently English with placeholders for other languages)
5. **Description**: Clear explanation of what the attribute represents
6. **Datatype**: The type of data (text, numeric, boolean, etc.)
7. **Examples**: Three specific examples of the attribute in use
8. **Topic**: Classification category (all set to "generic" for cross-category applicability)
9. **Motivation**: Explanation of why this attribute is important

## Attribute Categories

The attributes cover various aspects of products:

### Physical Dimensions
- width, height, depth, length, diameter, thickness
- weight, size, volume, capacity

### Identification & Branding
- brand, manufacturer, product-name, model-number
- ean, upc, gtin (barcode standards)

### Materials & Composition
- material, ingredients, chemical-composition
- fabric-weight, thread-count, weave-type

### Performance & Specifications
- power-consumption, voltage, frequency
- battery-life, charging-time, battery-type
- screen-size, resolution, refresh-rate
- processor, ram, storage-capacity

### Safety & Compliance
- certifications, safety-warnings, warranty-period
- fire-rating, toxicity-rating, allergens
- age-range, skill-level

### Environmental & Ethical
- eco-certification, recyclable, biodegradable
- organic, vegan, cruelty-free, fair-trade
- sustainable, renewable, energy-rating

### Usage & Care
- washable, dishwasher-safe, microwave-safe
- storage-instructions, care-instructions
- assembly-required, recommended-use

### Features & Capabilities
- adjustable, foldable, stackable, reversible
- wireless, smart-enabled, voice-control
- water-resistance, weatherproof, uv-protection

### Quality & Durability
- durability-rating, lifespan, shelf-life
- stain-resistant, scratch-resistant, fade-resistant
- tensile-strength, compression-strength

### Sensory Attributes
- color, scent, flavor, texture, pattern, finish

### Electronics & Connectivity
- bluetooth-version, wifi-capability, operating-system
- connectivity, ports, compatibility

### Food & Nutrition
- nutritional-values, calorie-content, serving-size
- gluten-free, dairy-free, nut-free, sugar-free
- expiration-date, production-date

### Textile & Fabric
- thread-count, gsm, denier
- breathability, water-absorption, stretch-percentage
- colorfastness, pilling-resistance

### Optical & Display
- resolution, brightness, contrast-ratio
- magnification, focal-length, aperture
- color-temperature, luminous-flux

## Usage

These attributes can be used for:

1. **Product Data Management**: Standardize product information across databases
2. **E-commerce**: Provide consistent product specifications for online stores
3. **Product Comparison**: Enable meaningful comparison between similar products
4. **Search & Filtering**: Allow customers to find products based on specific criteria
5. **Data Integration**: Facilitate data exchange between different systems
6. **Quality Control**: Ensure complete product documentation

## Contributing

When adding or modifying attributes:
1. Ensure the attribute is applicable across multiple product categories
2. Provide clear, specific examples
3. Define the datatype accurately
4. Include typical sources where this information can be found
5. Write clear descriptions that anyone can understand

## Categories Reference

The attributes are designed to work with the product categories defined in `categories.txt`, which includes:
- Animals & Pet Supplies
- Apparel & Accessories
- Hardware & Tools
- Electronics
- Sports & Outdoors
- Home & Garden
- Health & Personal Care
- And many more...

## Format Specification

Each attribute documentation file follows this format:

```
== Documentation == 
* Example of usages: [examples]
* Possible values: [value descriptions]
* Source: [where this data comes from]
* en = [attribute name in English]
* xx = <!-- property names in some other languages -->
* description = 
* description_en = [English description]
* description_xx = <!-- descriptions in other languages -->
* status = <!-- leave this empty -->
* datatype = [data type]
* example 1 = [example]
* example 2 = [example]
* example 3 = [example]
* topic = generic

===  Motivation ===

[Why this attribute is important]
```

## License

This documentation is created for the Open Products Facts project to help standardize product information across various categories and improve product data quality.
