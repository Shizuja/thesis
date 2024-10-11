import os

def read_file(file_path):
    """Reads the text file and returns a list of lines with numbers split by spaces."""
    with open(file_path, 'r') as file:
        lines = [list(map(int, line.split())) for line in file.readlines()[1:]]  #ignore the first line where the amount of nodes is stored
    return lines

def is_subset_of_any(line, lines):
    """Checks if a given line is a subset of any other line in the list."""
    line_set = set(line)
    for other_line in lines:
        if line_set != set(other_line) and line_set.issubset(set(other_line)):
            return True
    return False

def calculate_subset_proportion(lines):
    """Calculates the proportion of lines that are subsets of other lines."""
    subset_count = 0
    total_lines = len(lines)

    i = 0

    for line in lines:
        print(i,"/",total_lines)
        i +=1
        if is_subset_of_any(line, lines):
            subset_count += 1

    subset_proportion = subset_count / total_lines if total_lines > 0 else 0
    return subset_proportion

def process_file(file_path):
    """Main function to process the input file and calculate the subset proportion."""
    lines = read_file(file_path)  # Read input file
    subset_proportion = calculate_subset_proportion(lines)  # Calculate subset proportion
    return subset_proportion
dir_name = "C:/Users/Yanneck/Documents/bachelor_instances/"
#for file in os.listdir(dir_name):
proportion = process_file(dir_name+"contact-primary-school.hypergraph")
#print(file)
print(f"Proportion of lines that are subsets of other lines: {proportion:.2%}")
