def get_value(data_dict, key):
    if key in data_dict:
        return data_dict[key]
    else:
        return None
  #Replace with your code


def remove_key(data_dict, key):
    if key in data_dict:
        del data_dict[key] 
        return data_dict
    else:
        None
    """
    Removes the entry with the specified key from the dictionary.
    If the key is not found, the dictionary should remain unchanged.
    Returns the modified dictionary.
    """
    pass #Replace with your code