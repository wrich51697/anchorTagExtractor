# database_manager.py
# Author: William Richmond
# Date: 2024-12-11
# Class: CYBR-260-45
# Assignment: Anchor Tag Extractor - Database Manager Module
# Description: Manages SQLite database operations.
# Revised on: 2024-12-11

import os
import sqlite3
import datetime

# Class: DatabaseManager
# Purpose: Handles SQLite database operations for storing anchor tags.
class DatabaseManager:

    # Function: __init__
    # Purpose: Initializes the database manager with the database file name.
    # Inputs: db_name (str) - Name of the SQLite database file (default: "hyperlinks_storage.db").
    # Returns: None
    def __init__(self, db_name="hyperlinks_storage.db"):
        self.db_name = db_name
        self.conn = None

    # Function: initialize_database
    # Purpose: Initializes the database and creates the table if it doesn't exist.
    # Inputs: None
    # Returns: None
    def initialize_database(self):
        db_exists = os.path.exists(self.db_name)
        self.conn = sqlite3.connect(self.db_name)
        cursor = self.conn.cursor()

        if not db_exists:
            create_table_query = """
            CREATE TABLE storage (
                curtime TEXT,
                line TEXT
            )
            """
            cursor.execute(create_table_query)
            self.conn.commit()

    # Function: insert_into_database
    # Purpose: Inserts a line with a timestamp into the database.
    # Inputs: line (str) - The line to insert.
    # Returns: None
    def insert_into_database(self, line):
        current_time = datetime.datetime.now().isoformat()
        insert_query = "INSERT INTO storage (curtime, line) VALUES (?, ?)"
        cursor = self.conn.cursor()
        cursor.execute(insert_query, (current_time, line))
        self.conn.commit()