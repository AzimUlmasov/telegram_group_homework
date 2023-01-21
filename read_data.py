import json
def read_data(file_path: str)->dict:
    """
    This function will read the json file and return the data as a dictionary.
    
    Parameters:
        file_path (str): Path of the file to be read
    Returns:
        dict: Dictionary containing the data of the json file.
    
    """
    f = (file_path).read()

    return json.loads(f)

# print(__name__.upper())

# def main():
#     print(read_data('data/result.json'))

# if __name__ == '__main__':
#     main()

