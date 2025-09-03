def process_file_with_error_handling():
    """
    Prompts the user for a filename, reads its content, modifies it,
    writes the modified content to a new file, and handles potential errors.
    """
    input_filename = input("Enter the name of the file to read: ")
    output_filename = "modified_" + input_filename

    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()
            # Example modification: Convert content to uppercase
            modified_content = content.upper()

        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Successfully read '{input_filename}', modified content, and wrote to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except IOError as e:
        print(f"Error: An I/O error occurred while reading or writing the file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    process_file_with_error_handling()