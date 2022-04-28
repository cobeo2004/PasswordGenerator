import os
__path = "./src/Saves/"
__file_name = "temp.txt"

def save_to_txt(__data:any) -> None:
    if not os.path.exists(__path):
        os.makedirs(__path)
    else:
        with open(__path + __file_name, "w+") as op:
            op.writelines(__data)
            op.close()


def delete_everything_from_path() -> None:
    if not os.path.exists(__path):
        os.makedirs(__path)
    else:
        with open(__path + __file_name, "r+") as op:
            op.truncate(0)
            op.close()


def read_from_path() -> str:
    if not os.path.exists(__path):
        os.makedirs(__path)
    
    else:
        with open(__path + __file_name, "r+") as op:
            ct = op.readline()
            op.close()
            return ct