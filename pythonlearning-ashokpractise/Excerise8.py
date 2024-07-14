def analyze_csv_data(input_file, output_file):
    data = []  
    column_names = []  
    with open(input_file, 'r') as file:
        for line_num, line in enumerate(file):
            if line_num == 0:
                column_names = line.strip().split(',')
                print(column_names)
                continue  
            row = line.strip().split(',')
            data.append(row)
        print(data)
    if not data:
        raise ValueError("CSV file is empty or has no data rows")
    num_rows = len(data)
    column_statistics = {}  
    for col_index, col_name in enumerate(column_names):
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
            pass
    with open(output_file, 'w') as file:
        file.write(f"Column,Count,Average,Min,Max\n")
        for col_name, stats in column_statistics.items():
            file.write(f"{col_name},{stats['count']},{stats['average']:.2f},{
                       stats['min']:.2f},{stats['max']:.2f}\n")
analyze_csv_data('ex08in.csv', 'ex08ot.txt')
