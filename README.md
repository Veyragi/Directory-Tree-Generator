Directory Tree Generator
A simple, cross-platform Python script that generates a visual directory tree structure, similar to the tree command on Linux and macOS. This project was created as a practical exercise to understand and implement recursion for file system traversal. It uses only Python's standard libraries, so it runs anywhere Python is installed with no dependencies.

Features
Visual Directory Mapping: Creates a clean, easy-to-read visual map of any folder's structure.

Cross-Platform: Works on Windows, macOS, and Linux without any modification.

Zero Dependencies: Uses only the built-in os library. No pip install required.

Lightweight & Fast: Scans and prints the directory structure quickly.

Great Learning Tool: A clear and simple implementation of recursion for a real-world problem.

How to Use
Save the Script: Save the code as generate_tree.py.

Navigate to a Folder: Open your terminal or command prompt and use the cd command to navigate to the directory you want to analyze.

Place the Script: Make sure the generate_tree.py file is located inside the folder you want to map.

Run the Command: Execute the script with the following command:

python generate_tree.py

The script will automatically detect the current directory and print the tree structure to your console.

Example Output
Running the script in a simple project folder would produce an output like this:

my_project
├── documents
│   ├── proposal.docx
│   └── report.pdf
├── images
│   ├── logo.png
│   └── main_banner.jpg
└── scripts
    ├── analyze.py
    └── main.py
