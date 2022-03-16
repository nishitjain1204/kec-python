# 3. SQL Query generator
# Build a logic to help the data science team to generate SQL queries that can perform INSERT
# operation based on the tablename, colums and input data.
# Example:
# Input:
# tablename : student
# columns :
# id, first_name, last_name, course, dob
# data :
# 101, Bob, Alice, CSE, 10-10-2100
# Output:
# INSERT INTO student ( "id", "first_name", "last_name", "course", "dob")
# VALUES ("101", "Bob", "Alice", "CSE", "2100-10-10");


tablename =  input()
columns = [i.strip() for i in input().strip().split(",") if len(i.strip())>=1]
data = [i.strip() if len(i.strip())>=1 else "NaN" for i in input().split(",")]

if len(data) != len(columns):
    print("Error, Insufficient data")
else:
    column_string = '''" , "'''.join(columns)
    column_string = f'("{column_string}")'
    
    data_string = '''" , "'''.join(data)
    data_string = f'("{data_string}")'
    
    print(f"INSERT INTO {tablename} {column_string}\nValues {data_string};")
