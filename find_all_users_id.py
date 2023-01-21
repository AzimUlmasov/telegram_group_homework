from read_data import read_data

def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    return set([_tid['from_id']for _tid in data['messages'] if _tid['type'] == 'message' and _tid['from_id'] not in _tid])


data = read_data('data/result.json')

print(find_all_users_id(data))