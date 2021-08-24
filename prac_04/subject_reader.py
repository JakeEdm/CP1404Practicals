"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    records = get_data()
    display_subject_details(records)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data.append(parts)
    input_file.close()
    return data


def display_subject_details(records):
    for record in records:
        print(f'{record[0]} is taught by {record[1]:>12} and has {record[2]:>3} students')


main()
