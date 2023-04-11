import re

def get_xyz(db_data:str, name:str)-> str:
    p = re.compile(f'(NAME = {name})(.*?)Date modified:(.*?)\)(.*?)NAME', flags=re.DOTALL)
    result = p.search(db_data)

    xyz_info = result.group(4)
    return xyz_info
