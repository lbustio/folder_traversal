import os
import argparse

def list_directory(directory, level=0):
    """
    Recursively lists the contents of the specified directory.
    
    Args:
        directory (str): The path of the directory to list.
        level (int): The current depth level in the directory structure (for indentation).
    
    Returns:
        str: A formatted string representing the directory structure.
    """
    structure = ""
    try:
        # List the contents of the directory
        for name in os.listdir(directory):
            full_path = os.path.join(directory, name)
            structure += "  " * level + "- " + name + "\n"  # Indent based on the level of depth
            if os.path.isdir(full_path):  # Check if the path is a directory
                structure += list_directory(full_path, level + 1)  # Recursively list subdirectory
    except PermissionError:
        print(f"Permission denied to access {directory}.")  # Handle permission errors
    except FileNotFoundError:
        print(f"The directory {directory} does not exist.")  # Handle directory not found errors
    except Exception as e:
        print(f"An error occurred: {e}")  # Handle any other exceptions
    return structure

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="List the contents of a directory.")
    parser.add_argument('directory', type=str, help='The path of the directory to list.')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Use the provided directory path
    base_path = args.directory

    # Print the start of the directory listing process
    print(f"Starting to list the directory: {base_path}")
    structure = list_directory(base_path)

    # Print the generated directory structure
    if structure:
        print("\nDirectory structure:")
        print(structure)  # Print the directory structure
    else:
        print("No files or directories found.")  # Inform if nothing was found

    # Save the structure to a text file
    try:
        os.makedirs("output", exist_ok=True)  # Ensure the 'output' directory exists
        with open("output/directory_structure.txt", "w", encoding="utf-8") as file:
            file.write(structure)  # Write the structure to the file
        print("Structure generated and saved to 'output/directory_structure.txt'.")  # Confirmation message
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")  # Handle any errors during file saving

if __name__ == "__main__":
    main()  # Call the main function to execute the script
