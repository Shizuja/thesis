import os
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

def extract_decimal_numbers_from_file(file_path):
    decimal_numbers = []

    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            if words:
                decimal_numbers.append(words[-1])

    return decimal_numbers

def read_out_files_from_directory(directory, sort):
    all_numbers = []

    #sort file names alphabetically
    filenames = [f for f in os.listdir(directory) if f.endswith('.out')]
    filenames = sorted(filenames, key=lambda s: s.casefold()) #case-insensitive

    for filename in filenames:
        file_path = os.path.join(directory, filename)
        numbers = extract_decimal_numbers_from_file(file_path)
        if sorted:
            all_numbers.append(sorted(numbers, key=float, reverse=True))
        else:
            all_numbers.append(numbers)

    return all_numbers

def sort_lines_by_last_float(filename, range1, range2):
    with open(filename, 'r') as file:
        lines = file.readlines()

    lines_with_floats = []
    for line in lines:
        stripped_line = line.strip()
        if stripped_line:
            last_word = stripped_line.split()[-1]  # Get the last word
            last_float = float(last_word)
            lines_with_floats.append((stripped_line, last_float))

    sorted_lines = sorted(lines_with_floats, key=lambda x: x[1], reverse=True)
    sorted_nodes_in_range = []

    for line in sorted_lines[range1:range2]:
        sorted_nodes_in_range.append(line[0].split()[1])
    
    return sorted_nodes_in_range

def top_k(filename1, filename2, range1, range2):
    set1 = set(sort_lines_by_last_float(filename1, range1, range2))
    set2 = set(sort_lines_by_last_float(filename2, range1, range2))
    print(set1)
    print(set2)
    print("--")
    return len(set1.intersection(set2))


directory_path_clique = "C:/Users/Yanneck/Downloads/output/cliqueExpansion"#input("Please provide a path to a folder that contains the .out files for the clique expansion data: ")
directory_path_line= "C:/Users/Yanneck/Downloads/output/lineExpansion"#input("Please provide a path to a folder that contains the .out files for the line expansion data: ")
directory_path_direct = "C:/Users/Yanneck/Downloads/output/lineGraph"#input("Please provide a path to a folder that contains the .out files for the line graph data: ")

directory_path_clique2 = "C:/Users/Yanneck/Downloads/output/cliqueExpansion2"
directory_path_line2= "C:/Users/Yanneck/Downloads/output/lineExpansion2"

clique_result = read_out_files_from_directory(directory_path_clique,True)
line_result = read_out_files_from_directory(directory_path_line,True)
direct_result = read_out_files_from_directory(directory_path_direct,True)

clique_result2 = read_out_files_from_directory(directory_path_clique2,True)
line_result2 = read_out_files_from_directory(directory_path_line2,True)

mode = 4
i = 4
range1 = 0
range2 = 20
fontsize_value = 20

if mode == 0:
    print(clique_result[i])
    print(line_result[i])
    print(direct_result[i])
if mode == 1:
    print(clique_result2[i][range1:range2])
    print(line_result2[i][range1:range2])
if mode == 2:
    filenames = ["diseasome","disgenenet","house-committees","plant-pollinator-mpl-015","plant-pollinator-mpl-016","plant-pollinator-mpl-049","plant-pollinator-mpl-062","senate-committees"]
    for j in range(len(filenames)):
        print("\n" + filenames[j])
        print("cliqueExpansion: ")
        sort_lines_by_last_float(directory_path_clique + "/" + filenames[j] + ".out",range1,range2)
        print("lineExpansion: ")
        sort_lines_by_last_float(directory_path_line + "/" + filenames[j] + ".out",range1,range2)
        print("lineGraph: ")
        sort_lines_by_last_float(directory_path_direct + "/" + filenames[j] + ".out",range1,range2)
if mode == 3:
    filenames = ["contact-primary-school","hospital-lyon","hypertext-conference","InVS13","malawi-village","NDC-classes","senate-bills","SFHH-conference"]
    for j in range(len(filenames)):
        print("\n" + filenames[j])
        print("cliqueExpansion: ")
        sort_lines_by_last_float(directory_path_clique2 + "/" + filenames[j] + ".out",range1,range2)
        print("lineExpansion: ")
        sort_lines_by_last_float(directory_path_line2 + "/" + filenames[j] + ".out",range1,range2)
if mode == 4:
    filenames = ["senate-bills","contact-primary-school","NDC-classes","plant-pollinator-mpl-015","SFHH-conference",
                 "algebra-questions","diseasome","geometry-questions","disgenenet","plant-pollinator-mpl-062","madison-restaurant-reviews","house-committees",
                 "vegas-bars-reviews","music-blues-reviews"]
    """
    ["senate-bills","malawi-village","contact-primary-school","hospital-lyon","NDC-classes","plant-pollinator-mpl-015","SFHH-conference",
                 "algebra-questions","hypertext-conference","diseasome","geometry-questions","disgenenet","InVS13","plant-pollinator-mpl-062","madison-restaurant-reviews","house-committees","senate-committees",
                 "vegas-bars-reviews","music-blues-reviews"]
    """
    values = [0]*len(filenames)
    for j in range(len(filenames)):
        values[j] = top_k("C:/Users/Yanneck/Downloads/output/cliqueExpansion_full/" + filenames[j] + ".out","C:/Users/Yanneck/Downloads/output/lineExpansion_full/" + "/" + filenames[j] + ".out",range1,range2)
    print(values)

    sorted_names_values = sorted(zip(filenames, values), key=lambda x: x[1])
    sorted_filenames, sorted_values = zip(*sorted_names_values)

    #plot
    fig, ax1 = plt.subplots()
    bar1 = ax1.bar(filenames, values, label="Overlap of Top 20 nodes")
    ax1.set_xlabel('data sets', fontsize=fontsize_value)
    ax1.set_ylabel('Overlap', fontsize=fontsize_value)
    ax1.set_title('Overlap of Top 20 Nodes for Clique Expansion Method and Line Expansion Method', fontsize=fontsize_value+5)
    ax1.legend(prop={'size': fontsize_value+5})
    ax1.yaxis.set_major_locator(MaxNLocator(integer=True))

    plt.setp(ax1.get_xticklabels(), rotation=30, horizontalalignment='right', fontsize=fontsize_value)

    # Show the plot
    plt.show()