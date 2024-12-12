# Anchor Tag Extractor Project Documentation

## README.md

### Project Title: Anchor Tag Extractor

### Author: William Richmond

### Date: 2024-12-11Class: CYBR-260-45

### Assignment: Extract and Store Hyperlink Lines

## Description:

The Anchor Tag Extractor is a Python-based tool that retrieves web documents, identifies anchor tags (`<a>`), and stores 
the extracted lines in an SQLite database. The program features a user-friendly graphical user interface (GUI) to 
facilitate easy input and visualization of results.

## Features:

1. Fetches HTML documents from user-specified URLs.

2. Extracts lines containing anchor tags.

3. Displays extracted lines in a scrollable GUI window.

4. Stores extracted lines with timestamps in an SQLite database.
___

## Prerequisites:

1. Python 3.8 or higher.

2. Required Python libraries:

    - `requests`

    - `tkinter`

    - `sqlite3`

To install the required libraries, run:

```bash
   pip install requests
```
___

## Directory Structure:
```text
anchorTagExtractor/
├── extractor/
│   ├── __init__.py
│   ├── anchor_extractor.py  # Handles extraction logic.
│   ├── database_manager.py  # Manages SQLite database operations.
├── gui/
│   ├── __init__.py
│   ├── main_gui.py          # Provides the graphical user interface.
├── main.py                  # Entry point of the program.
└── README.md                # Project documentation.
```
___

## How to Run:

1. Clone or download the project to your local machine.

2. Navigate to the project directory in your terminal.

3. Run the following command:

```bash
python main.py
```

4. Enter the URL in the provided field and click Process URL.

5. View extracted anchor tags in the output window.

6. Stored data can be found in the SQLite database file hyperlinks_storage.db.
___

## Future Enhancements:

- Add support for advanced filtering of anchor tags.

- Enhance database querying capabilities.

- Include export options for extracted data (e.g., CSV, JSON).

