#remove duplicates from first file
with open('rmc.csv', 'r') as csvfile_1:
    line_csvfile_1 = set(csvfile_1.readlines())

#remove duplicates from second file
with open('r-m-c.csv', 'r') as csvfile_2:
    line_csvfile_2 = set(csvfile_2.readlines())

#Symmetric Difference for bouth files
two_files_without_duplecates = line_csvfile_1.symmetric_difference(line_csvfile_2)

#write to new csv file
with open('rmc_without_duplic.csv', 'w') as csvfile:
    for elements in two_files_without_duplecates:
        csvfile.write(elements)