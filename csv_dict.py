def retrieve_csv_data(csv_filename: str) -> dict:
    """Retreive data from CSV file and place it into a python dict

    Args:
        csv_filename (str): name of the csv file containing the site data

    Returns:
        dict: dictionary containing the data
    """
    data = []
    with open(csv_filename, 'r') as csv_file:
        for line in csv.DictReader(csv_file):
            data.append(line)
    return data