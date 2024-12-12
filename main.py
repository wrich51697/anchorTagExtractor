# main.py
# Author: William Richmond
# Date: 2024-12-11
# Class: CYBR-260-45
# Assignment: Anchor Tag Extractor - Main Entry Point
# Description: Entry point for the Anchor Tag Extractor application.
# Revised on: 2024-12-11

from tkinter import Tk
from extractor.anchor_extractor import AnchorExtractor
from extractor.database_manager import DatabaseManager
from gui.main_gui import GUI

if __name__ == "__main__":
    # Main execution block.
    # Initializes the extractor and GUI, then starts the Tkinter main loop.
    extractor = AnchorExtractor()
    db_manager = DatabaseManager()
    root = Tk()
    app = GUI(root, extractor, db_manager)
    root.mainloop()
