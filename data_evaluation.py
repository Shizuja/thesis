import os
import numpy as np
import matplotlib.pyplot as plt

def extract_decimal_numbers_from_file(file_path):
    decimal_numbers = []

    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            if words:
                decimal_numbers.append(words[-1])

    return decimal_numbers

def read_out_files_from_directory(directory):
    all_numbers = []

    #sort file names alphabetically
    filenames = [f for f in os.listdir(directory) if f.endswith('.out')]
    filenames = sorted(filenames, key=lambda s: s.casefold()) #case-insensitive

    for filename in filenames:
        file_path = os.path.join(directory, filename)
        numbers = extract_decimal_numbers_from_file(file_path)
        all_numbers.append(numbers)

    return all_numbers

def calculate_zero_fraction(arrays):
    # all arrays should have the same length
    zero_fractions = []
    length = len(arrays)
    for i in range(len(arrays[0])):
        temp = [0]*length
        for j in range(length):
            zero_count = 0
            total_count = len(arrays[j][i])
            for value in arrays[j][i]:
                if value == "0":
                    zero_count += 1
            temp[j] = zero_count / total_count if total_count > 0 else 0
        zero_fractions.append(temp)

    return zero_fractions

directory_path_clique = "C:/Users/Yanneck/Downloads/output/cliqueExpansion"#input("Please provide a path to a folder that contains the .out files for the clique expansion data: ")
directory_path_line= "C:/Users/Yanneck/Downloads/output/lineExpansion"#input("Please provide a path to a folder that contains the .out files for the line expansion data: ")
directory_path_direct = "C:/Users/Yanneck/Downloads/output/lineGraph"#input("Please provide a path to a folder that contains the .out files for the line graph data: ")

directory_path_clique1 = "C:/Users/Yanneck/Downloads/output/cliqueExpansion1"
directory_path_line1= "C:/Users/Yanneck/Downloads/output/lineExpansion1"
directory_path_direct1 = "C:/Users/Yanneck/Downloads/output/lineGraph1"

directory_path_clique2 = "C:/Users/Yanneck/Downloads/output/cliqueExpansion2"
directory_path_line2= "C:/Users/Yanneck/Downloads/output/lineExpansion2"

clique_result = read_out_files_from_directory(directory_path_clique)
line_result = read_out_files_from_directory(directory_path_line)
direct_result = read_out_files_from_directory(directory_path_direct)

clique_result1 = read_out_files_from_directory(directory_path_clique1)
line_result1 = read_out_files_from_directory(directory_path_line1)
direct_result1 = read_out_files_from_directory(directory_path_direct1)

clique_result2 = read_out_files_from_directory(directory_path_clique2)
line_result2 = read_out_files_from_directory(directory_path_line2)

zero_fractions = calculate_zero_fraction([clique_result, line_result, direct_result])
zero_fractions1 = calculate_zero_fraction([clique_result1, line_result1, direct_result1])
zero_fractions2 = calculate_zero_fraction([clique_result2, line_result2])

fontsize_value=25

#Plot 1
labels = ["diseasome","disgenenet","house-committees","plant-pollinator-mpl-015","plant-pollinator-mpl-016","plant-pollinator-mpl-049","plant-pollinator-mpl-062","senate-committees"]
x = np.arange(len(labels)) 
width = 0.25

fig, ax = plt.subplots()
bars0 = ax.bar(x - width, [zero_fractions[i][0] for i in range(len(zero_fractions))], width, label='Clique Expansion Method')
bars1 = ax.bar(x, [zero_fractions[i][1] for i in range(len(zero_fractions))], width, label='Line Expansion Method')
bars2 = ax.bar(x + width, [zero_fractions[i][2] for i in range(len(zero_fractions))], width, label='Line Graph Method')

ax.set_xlabel('data sets', fontsize=fontsize_value)
ax.set_ylabel('proportion of zero values', fontsize=fontsize_value)
ax.set_title('The Proportion of Zero Values in each Data Set', fontsize=fontsize_value+5)
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=fontsize_value)
ax.legend(prop={'size': fontsize_value+5})

plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')
plt.yticks(fontsize=fontsize_value+5)
plt.show()

#Plot2
labels = ["algebra-questions","geometry-questions","madison-restaurant-reviews","music-blues-reviews","vegas-bars-reviews"]
x = np.arange(len(labels)) 
width = 0.25

fig, ax1 = plt.subplots()
bars0 = ax1.bar(x - width, [zero_fractions1[i][0] for i in range(len(zero_fractions1))], width, label='Clique Expansion Method')
bars1 = ax1.bar(x, [zero_fractions1[i][1] for i in range(len(zero_fractions1))], width, label='Line Expansion Method')
bars2 = ax1.bar(x + width, [zero_fractions1[i][2] for i in range(len(zero_fractions1))], width, label='Line Graph Method')

ax1.set_xlabel('data sets', fontsize=fontsize_value)
ax1.set_ylabel('proportion of zero values', fontsize=fontsize_value)
ax1.set_title('The Proportion of Zero Values in each Data Set', fontsize=fontsize_value+5)
ax1.set_xticks(x)
ax1.set_xticklabels(labels, fontsize=fontsize_value)
ax1.legend(prop={'size': fontsize_value+5})

plt.setp(ax1.get_xticklabels(), rotation=30, horizontalalignment='right')
plt.yticks(fontsize=fontsize_value+5)
plt.show()

#Plot3
labels = ["contact-primary-school","hospital-lyon","hypertext-conference","InVS13","malawi-village","NDC-classes","senate-bills","SFHH-conference"]
selection = [4,5,6]
x = np.arange(len(selection)) 
width = 0.25

fig2, ax2 = plt.subplots()
bars20 = ax2.bar(x - width/2, [zero_fractions2[i][0] for i in selection], width, label='Clique Expansion Method')
bars21 = ax2.bar(x + width/2, [zero_fractions2[i][1] for i in selection], width, label='Line Expansion Method')

ax2.set_xlabel('data sets', fontsize=fontsize_value)
ax2.set_ylabel('proportion of zero values', fontsize=fontsize_value)
ax2.set_title('The Proportion of Zero Values in each Data Set', fontsize=fontsize_value+5)
ax2.set_xticks(x)
ax2.set_xticklabels([labels[j] for j in selection], fontsize=fontsize_value)
ax2.legend(prop={'size': fontsize_value+5})

plt.setp(ax2.get_xticklabels(), rotation=30, horizontalalignment='right')
plt.yticks(fontsize=fontsize_value+5)
plt.show()

#Plot3
labels = ["contact-primary-school","hospital-lyon","hypertext-conference","InVS13","malawi-village","NDC-classes","senate-bills","SFHH-conference"]
selection = [0,1,2,3,7]
x = np.arange(len(selection)) 
width = 0.25

fig2, ax2 = plt.subplots()
bars20 = ax2.bar(x - width/2, [zero_fractions2[i][0] for i in selection], width, label='Clique Expansion Method')
bars21 = ax2.bar(x + width/2, [zero_fractions2[i][1] for i in selection], width, label='Line Expansion Method')

ax2.set_xlabel('data sets', fontsize=fontsize_value)
ax2.set_ylabel('proportion of zero values', fontsize=fontsize_value)
ax2.set_title('The Proportion of Zero Values in each Data Set', fontsize=fontsize_value+5)
ax2.set_xticks(x)
ax2.set_yticks([0.001,0.002,0.003,0.004,0.005,0.006,0.007,0.008,0.009])
ax2.set_xticklabels([labels[j] for j in selection], fontsize=fontsize_value)
ax2.legend(prop={'size': fontsize_value+5})

plt.setp(ax2.get_xticklabels(), rotation=30, horizontalalignment='right')
plt.yticks(fontsize=fontsize_value+5)
plt.show()