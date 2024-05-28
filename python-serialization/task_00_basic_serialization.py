import json

def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to a JSON file.
    
    Parameters:
    data (dict): The dictionary to be serialized.
    filename (str): The filename of the output JSON file. If the output file already exists it should be replaced.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """
    Loads a JSON file and deserializes it to a Python dictionary.
    
    Parameters:
    filename (str): The filename of the input JSON file.
    
    Returns:
    dict: The deserialized Python dictionary.
    """
    with open(filename, 'r') as file:
        return json.load(file)

