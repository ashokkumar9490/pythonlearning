### Python - Exercise-8  

## Create A python program to practice Python File Handling: CSV Data Processing and Analysis. This exercise involves creating a function called analyze_csv_data that reads and processes data from a CSV (Comma-Separated Values) file, calculates basic statistics, and saves the results to a new file.

Function: analyze_csv_data(input_file, output_file)

Parameters:

input_file (str): Path to the CSV file containing the data.
output_file (str): Path to the output file where the analysis results will be saved.
Expected format of the CSV file:

The CSV file should have a header row with column names and subsequent rows containing data points. You can assume a specific format for this exercise (e.g., comma-separated, first row as headers).

Analysis performed:

Count the total number of data points (rows excluding the header).
Calculate the average value for each numeric column.
Identify the minimum and maximum values for each numeric column.
Output format:

The function should create a new CSV file with the following content:

Header row: "Metric", "Value"
Rows for each analyzed aspect:
"Number of data points"
For each numeric column:
"Average of [column name]"
"Minimum of [column name]"
"Maximum of [column name]"


Sample Input (data.csv):
 
City,Population,Area (km²)  
New York City,8,625,405,833  
Los Angeles,3,971,883,13  


Sample Output (results.csv):  

Metric,Value  
Number of data points,2  
Average of Population,4,318,644,468  
Minimum of Population,3,971,883,13  
Maximum of Population,8,625,405,833  
Average of Area (km²),463,644,471  
Minimum of Area (km²),13  
Maximum of Area (km²),833  
