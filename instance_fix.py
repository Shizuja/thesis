def read_file(file_path):
    """Reads the text file and returns a list of lines with numbers split by spaces."""
    with open(file_path, 'r') as file:
        lines = [list(map(int, line.split())) for line in file]
    return lines

def write_file(file_path, lines):
    """Writes the modified lines back to a text file."""
    with open(file_path, 'w') as file:
        for line in lines:
            file.write(' '.join(map(str, line)) + '\n')

def normalize_numbers(lines):
    """Changes the numbers so they range from 0 to lines-1."""
    # Collect all unique numbers from the lines
    unique_numbers = sorted(set(num for line in lines for num in line))

    # Create a mapping from original number to normalized range 0 to n-1
    number_map = {original: new for new, original in enumerate(unique_numbers)}

    # Replace numbers in the lines based on the number_map
    normalized_lines = [[number_map[num] for num in line] for line in lines]

    return normalized_lines

def process_file(input_path, output_path):
    """Main function to process the input file and write the normalized content to the output."""
    lines = read_file(input_path)  # Read input file
    normalized_lines = normalize_numbers(lines)  # Normalize numbers
    write_file(output_path, normalized_lines)  # Write output file

# Beispielaufruf
input_path = "C:/Users/Yanneck/Downloads/cat-edge-madison-restaurant-reviews/cat-edge-madison-restaurant-reviews"  # Ersetze dies durch den Pfad zur Eingabedatei

process_file(input_path+"/hyperedges.txt", "C:/Users/Yanneck/Downloads/instances/madison-restaurant-reviews.hypergraph")