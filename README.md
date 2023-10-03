# Bwaku - JSONL Data Processor

## Introduction

Bwaku is a Python program designed for processing and manipulating data stored in JSONL files. It provides a set of functionalities to work with multilingual datasets, extract and transform data, and generate structured output in various formats.

This program was created to address specific data processing tasks, including:

- **Generating Excel Files**: Bwaku can take JSONL files containing multilingual data and produce separate Excel files for each language, simplifying data analysis and presentation.

- **Creating Separate JSONL Files**: Bwaku can filter and split JSONL data based on specified categories (e.g., test, train, dev) and generate separate JSONL files for each category and language.

- **Generating Translation Data**: Bwaku can merge data from different languages, extract translations from English (en) to other languages (xx), and create a structured JSONL file for easy access and analysis.

## Project Tasks
## Question 1: python3 environment setup 
In this section, you will set up the python 3 environment and work with the MASSIVE dataset

Task 1 : Build a python3 project with the structure of projects installing the necessary dependencies in preffered IDE (pycharm, visual studio) then import the MASSIVE dataset https://github.com/alexa/massive

Task 2 : generate "en-xx.xlxs" files for all languages, using id, utt and annot_utt. Recursion is not used due to its heavy time complexity.

Task 3 : have the flags running the solution in the run_script.sh

## Question 2: Working with files 
In this question, you will be manipulating JSON files to produce required outputs:

Task 1: generate seperate JSONL files for English (en), Swahili (sw) and German (de) with test, train and dev.

Task 2: generate a single JSON file showing all the translations from en to xx with id and utt for all the train sets(pretty print your json file structure)

# Prerequisites
- >python >= 3.11
- >pandas
- >absl-py


# Installation Process

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
