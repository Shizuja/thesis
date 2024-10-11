import os

def extract_last_float(file_path):
    """Extracts the last float from the last line of the file."""
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if lines:  # Ensure the file is not empty
                last_line = lines[-1]
                # Get the last word from the last line, convert to float
                last_word = last_line.split()[-1]
                return float(last_word)
    except (ValueError, IndexError, FileNotFoundError) as e:
        print(f"Error processing file {file_path}: {e}")
    return None

def calculate_average_float_from_status_files(directory):
    """Calculates the average of the last float numbers from all .status files in a directory."""
    float_values = []
    
    # Loop over all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".status"):  # Only process .status files
            file_path = os.path.join(directory, filename)
            float_value = extract_last_float(file_path)
            if float_value is not None:
                float_values.append(float_value)
                print(filename, float_value)
    
    if float_values:
        average = sum(float_values) / len(float_values)
        print(f"Average of the float values: {average}")
    else:
        print("No valid float values found in the .status files.")

directory_path = "C:/Users/Yanneck/Downloads/output/times/direct"
calculate_average_float_from_status_files(directory_path)