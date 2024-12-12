# User Guide

## Overview:

The Anchor Tag Extractor is designed for users who need to analyze web documents by extracting and storing anchor tags.
 The application is intuitive and does not require prior programming experience.

## Steps to Use:



1. Input URL:

   - Enter the full URL of the web page to analyze in the text field.

   - Example: https://example.com

2. Process URL:

   - Click the `Process URL` button.

   - The program will fetch the web page, identify lines containing anchor tags, and display them in the output window.

3. Review Results:

   - The output window will show all extracted anchor tags.

4. Save to Database:

   - All displayed anchor tags are automatically saved to the SQLite database (`hyperlinks_storage.db`).

5. Exit Program:

   - Click the `Exit` button to close the application.
___

## Troubleshooting:

1. Error Fetching URL:

   - Ensure the URL is valid and accessible.

   - Check your internet connection.

2. No Anchor Tags Found:

   - Verify that the web page contains `<a>` tags.

3. Database Issues:

   - Ensure the application has write permissions in the project directory.

___

## Notes:

- All timestamps are recorded in ISO format.

- The database stores each extracted line as a separate record for easy querying and analysis.