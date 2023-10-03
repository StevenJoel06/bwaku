# Bwaku

## Introduction

Bwaku is a Python program designed for processing and manipulating data stored in JSONL files. It provides a set of functionalities to work with multilingual datasets, extract and transform data, and generate structured output in various formats.
The project aims to practice speaking with multiple file formats with Python libraries such as Pandas. A translation from English to other languages e.g. Swahili is captured. The JSON files are pretty-printed for easy readability
This program was created to address specific data processing tasks, including:

**Generating Excel Files**: Bwaku can take JSONL files containing multilingual data and produce separate Excel files for each language, simplifying data analysis and presentation.

**Creating Separate JSONL Files**: Bwaku can filter and split JSONL data based on specified categories (e.g., test, train, dev) and generate separate JSONL files for each category and language.

**Generating Translation Data**: Bwaku can merge data from different languages, extract translations from English (en) to other languages (xx), and create a structured JSONL file for easy access and analysis.

# Prerequisites
- >python >= 3.11
- >pandas
- >absl-py


# Installation

1. Clone the repo
```
git clone https://github.com/StevenJoel06/bwaku.git
```

2. Ensure you have Python installed on your machine as well as a pip. Confirm with 
```
python -V
pip -v
```
Ensure that the version is 3.10 and above And 22 for pip

3. Install Pandas
```
pip install pandas
```

4. Install absl flags
```
pip install absl-py
```

5. To generate the output files run the generator.sh file
```
./generator.sh
```
6. Generation
The files will automatically be stored in a newly created folder for outout in .xlsx format.
