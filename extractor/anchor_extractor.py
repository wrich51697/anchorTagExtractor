# anchor_extractor.py
# Author: William Richmond
# Date: 2024-12-11
# Class: CYBR-260-45
# Assignment: Anchor Tag Extractor - Anchor Extractor Module
# Description: Handles extraction of anchor tags from web documents.
# Revised on: 2024-12-11

import requests
from tkinter import messagebox

# Class: AnchorExtractor
# Purpose: Handles fetching documents and extracting anchor tags.
class AnchorExtractor:

    # Function: fetch_root_document
    # Purpose: Fetches the root document from the specified URL.
    # Inputs: url (str) - The URL to fetch.
    # Returns: list[str] - List of lines from the document.
    @staticmethod
    def fetch_root_document(url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text.splitlines()
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching the document: {e}")
            return []

    # Function: extract_anchor_lines
    # Purpose: Extracts lines containing anchor tags.
    # Inputs: lines (list[str]) - Lines from the document.
    # Returns: list[str] - List of lines with anchor tags.
    @staticmethod
    def extract_anchor_lines(lines):
        return [line for line in lines if '<a ' in line]
