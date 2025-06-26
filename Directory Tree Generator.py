import os

def generate_tree(start_path, prefix=""):
    """
    Recursively generates and prints a visual tree structure for a given path.

    Args:
        start_path (str): The absolute path of the directory to start from.
        prefix (str): A string of characters used to format the tree structure.
                      This is handled by the recursive calls.
    """
    # --- Check for valid path ---
    if not os.path.isdir(start_path):
        print(f"Error: The provided path '{start_path}' is not a valid directory.")
        return

    # --- Get directory contents ---
    # os.listdir gives us all files and folders in the current path.
    # We'll sort them to ensure a consistent output every time.
    try:
        items = sorted(os.listdir(start_path))
    except PermissionError:
        print(f"Skipping '{start_path}' due to a permission error.")
        return

    # --- Prepare for iteration ---
    # We need to know which item is the last one to draw the tree lines correctly.
    item_count = len(items)
    
    # --- Recursive Loop ---
    for i, item_name in enumerate(items):
        # Determine if this is the last item in the list
        is_last = (i == item_count - 1)
        
        # This is the core of the visual representation.
        # '├──' is for an item in the middle.
        # '└──' is for the last item.
        connector = "└── " if is_last else "├── "
        
        # Print the current item with its tree prefix
        print(prefix + connector + item_name)
        
        # --- The RECURSIVE step ---
        # If the current item is a directory, we call the function again
        # for that directory.
        full_path = os.path.join(start_path, item_name)
        if os.path.isdir(full_path):
            # We extend the prefix for the next level of the tree.
            # '    ' is for an item that was the last in its list.
            # '|   ' is for an item that was in the middle.
            new_prefix = prefix + ("    " if is_last else "|   ")
            generate_tree(full_path, prefix=new_prefix)


# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # Get the path of the current working directory
    # This is safer than picking a specific folder like "Downloads"
    current_directory = os.getcwd()

    print(f"Generating tree for the current directory: {current_directory}\n")
    print(os.path.basename(current_directory)) # Print the root folder name

    # Start the recursive generation
    generate_tree(current_directory)
  
    print("\n--- How to use ---")
    print("1. Run this Python script inside any folder.")
    print("2. It will automatically print a tree structure of that folder.")
    print("3. To analyze a different folder, you can run this script from there.")