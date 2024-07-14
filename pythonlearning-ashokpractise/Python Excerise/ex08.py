def analyze_csv_data(input_file, output_file):
    """
    Analyzes data from a CSV file and saves basic statistics to a new file.
    Args:
        input_file (str): Path to the CSV file containing the data.
        output_file (str): Path to the output file where results will be saved.
    """
    # Data structures
    data = []  # List of lists to store data
    column_names = []  # List to store column names
    # Open the file and read data
    with open(input_file, 'r') as file:
        for line_num, line in enumerate(file):
            # Skip header on first iteration
            if line_num == 0:
                column_names = line.strip().split(',')
                print(column_names)
                continue  # Skip header row processing
            # Process data row
            row = line.strip().split(',')
            data.append(row)
        print(data)
    # Validate data (optional)
    if not data:
        raise ValueError("CSV file is empty or has no data rows")
    # Analyze data (calculate statistics)
    num_rows = len(data)
    column_statistics = {}  # Dictionary to store column statistics
    for col_index, col_name in enumerate(column_names):
        # Check for numeric column (can be improved with type checks)
        try:
            column_data = [float(val)
                           for val in [row[col_index] for row in data]]
            column_statistics[col_name] = {
                'count': num_rows,
                'average': sum(column_data) / num_rows,
                'min': min(column_data),
                'max': max(column_data)
            }
        except ValueError:
            # Handle non-numeric columns (optional: log, ignore, etc.)
            pass
    # Save results to output file
    with open(output_file, 'w') as file:
        # Write header row
        file.write(f"Column,Count,Average,Min,Max\n")
        # Write statistics for each column
        for col_name, stats in column_statistics.items():
            file.write(f"{col_name},{stats['count']},{stats['average']:.2f},{
                       stats['min']:.2f},{stats['max']:.2f}\n")
