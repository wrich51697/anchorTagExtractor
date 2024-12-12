# main_gui.py
# Author: William Richmond
# Date: 2024-12-11
# Class: CYBR-260-45
# Assignment: Anchor Tag Extractor - GUI Module
# Description: Provides a graphical user interface for interacting with the application.
# Revised on: 2024-12-12

import tkinter as tk
from tkinter import messagebox, scrolledtext, Menu
from tkinterweb import HtmlFrame
from markdown import markdown
import os


# Class: GUI
# Purpose: Provides a GUI for the Anchor Tag Extractor application.
class GUI:

    # Function: __init__
    # Purpose: Initializes the GUI components.
    # Inputs: root (Tk) - The Tkinter root window.
    #         extractor (AnchorExtractor) - The backend extractor object.
    #         db_manager (DatabaseManager) - The database manager object.
    # Returns: None
    def __init__(self, root, extractor, db_manager):
        self.output_text = None
        self.url_entry = None
        self.status_label = None
        self.root = root
        self.extractor = extractor
        self.db_manager = db_manager
        self.root.title("Anchor Tag Extractor")
        self.create_widgets()

    # Function: create_widgets
    # Purpose: Creates the GUI widgets.
    # Inputs: None
    # Returns: None
    def create_widgets(self):
        # Create menu bar
        menu_bar = Menu(self.root)
        self.root.config(menu=menu_bar)

        # Help menu
        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        help_menu.add_command(label="User Guide", command=self.show_user_guide)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        # Configure row and column resizing
        self.root.rowconfigure(2, weight=1)  # Output text area (row 2)
        self.root.columnconfigure(1, weight=1)  # Expandable column (column 1)

        # Demo note
        tk.Label(
            self.root,
            text="Example URL provided below. Click 'Process URL' for a demonstration:",
            fg="blue",
            font=("Arial", 10, "italic"),
        ).grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky="w")

        # Input area
        tk.Label(self.root, text="Enter URL:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.url_entry = tk.Entry(self.root, width=50)
        self.url_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")  # Expandable

        # Add actual example URL
        example_url = "https://catalog.champlain.edu"
        self.url_entry.insert(0, example_url)

        # Output area
        self.output_text = scrolledtext.ScrolledText(
            self.root, wrap=tk.WORD, font=("Courier", 10)
        )  # Improved font for readability
        self.output_text.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")  # Expandable

        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.grid(row=3, column=0, columnspan=2, pady=5)

        tk.Button(button_frame, text="Process URL", command=self.process_url).pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame, text="Clear Output", command=self.clear_output).pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame, text="Exit", command=self.root.quit).pack(side=tk.LEFT, padx=10)

        # Status bar
        self.status_label = tk.Label(self.root, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_label.grid(row=4, column=0, columnspan=2, sticky="ew")  # Expandable

    # Function: process_url
    # Purpose: Processes the user-provided URL and stores extracted lines in the database.
    # Inputs: None
    # Returns: None
    def process_url(self):
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showwarning("Input Error", "Please enter a URL.")
            return

        self.status_label.config(text="Fetching document...")
        lines = self.extractor.fetch_root_document(url)
        if not lines:
            self.status_label.config(text="Failed to fetch document.")
            return

        self.status_label.config(text="Extracting anchor tags...")
        anchor_lines = self.extractor.extract_anchor_lines(lines)
        if not anchor_lines:
            self.status_label.config(text="No anchor tags found.")
            messagebox.showinfo("No Data", "No anchor tags found in the document.")
            return

        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, "Anchor Tags to be Added to the Database:\n\n")
        for line in anchor_lines:
            self.output_text.insert(tk.END, line.strip() + "\n\n")  # Add blank line between tags

        self.db_manager.initialize_database()
        for line in anchor_lines:
            self.db_manager.insert_into_database(line)

        # Inform the user about permanent storage
        self.output_text.insert(
            tk.END, f"\n\nA permanent copy of these anchor tags is stored in 'hyperlinks_storage.db'.\n"
        )
        self.status_label.config(text=f"Inserted {len(anchor_lines)} lines into the database.")
        messagebox.showinfo("Success", f"Inserted {len(anchor_lines)} lines into the database.")

    # Function: clear_output
    # Purpose: Clears the output text area.
    # Inputs: None
    # Returns: None
    def clear_output(self):
        self.output_text.delete(1.0, tk.END)
        self.status_label.config(text="Output cleared.")

    # Function: show_about
    # Purpose: Displays the About information.
    # Inputs: None
    # Returns: None
    @staticmethod
    def show_about():
        messagebox.showinfo("About", "Anchor Tag Extractor v1.0\nAuthor: William Richmond\nDate: 2024-12-11")

    # Function: show_user_guide
    # Purpose: Displays the user guide in a new window.
    # Inputs: None
    # Returns: None
    def show_user_guide(self):
        # Define the path to the user guide
        manual_path = os.path.join(os.getcwd(), "User Guide.md")

        if not os.path.exists(manual_path):
            messagebox.showerror("Error", f"User guide not found at:\n{manual_path}")
            return

        try:
            # Open a new window for the user guide
            manual_window = tk.Toplevel(self.root)
            manual_window.title("User Guide")
            manual_window.geometry("800x600")

            # Create an HTML frame to display the rendered Markdown
            html_frame = HtmlFrame(manual_window)
            html_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

            # Read and render the Markdown content
            with open(manual_path, "r", encoding="utf-8") as manual_file:
                markdown_content = manual_file.read()
                html_content = markdown(markdown_content, extensions=["extra"])  # Convert Markdown to HTML
                html_frame.load_html(html_content)  # Display the HTML content
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while opening the user guide:\n{e}")
