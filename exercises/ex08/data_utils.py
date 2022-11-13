"""Dictionary related utility functions."""

__author__ = "730615558"

from csv import DictReader

# Define your functions below


def read_csv_rows(filename: str) -> list[dict[str, str]]: 
    """Read the rows of a CSV into a table."""
    result: list[dict[str, str]] = []

    # TODO More work!

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV frather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line by line
    for row in csv_reader:
        result.append(row)
    
    # Read that file 

    # Close the file when we're done, to free its resources
    file_handle.close()
    
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]: 
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column] 
        result.append(item)
    return result 


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]: 
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
        
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
            
    return result


def head(column_table: dict[str, list[str]], row_num: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    for column in column_table:
        new_list: list[str] = []
        i: int = 0

        if len(column_table[column]) <= row_num:
            result[column] = column_table[column]
        else: 
            while len(new_list) < row_num:
                new_list.append(column_table[column][i])
                i += 1
            result[column] = new_list

    return result


def select(column_table: dict[str, list[str]], column_copy: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for column in column_copy:
        result[column] = column_table[column]

    return result


def concat(column_table: dict[str, list[str]], column_table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tabled combined."""
    result: dict[str, list[str]] = {}
    for column in column_table: 
        result[column] = column_table[column]
    for column in column_table_2: 
        if column in result: 
            result[column] += column_table_2[column] 
        else: 
            result[column] = column_table_2[column]
    return result 


def count(list_values: list[str]) -> dict[str, int]: 
    """Produce a dictionary where each key is a unique value in the given list and each value associated is the ocunt of the number of times that value appeared in the input list."""
    result: dict[str, int] = {}
    for item in list_values: 
        if item in result:
            result[item] += 1 
        else: 
            result[item] = 1

    return result
