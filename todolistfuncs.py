import os
FILE_PATH = "todo_list.txt"


def get_todos(file_path_arg = FILE_PATH):
    """
    Docstring for get_todos
    """
    if os.path.isfile(FILE_PATH):
        with open(file_path_arg, "r") as TDfile:
            todos = TDfile.readlines()
        return todos
    else:  
         with open(file_path_arg, "w") as TDfile:
             pass
         with open(file_path_arg, "r") as TDfile:
            todos = TDfile.readlines()
            return todos

def write_todos(todos_arg,file_path_arg = FILE_PATH):
    """
    Docstring for write_todos
    """
    with open(file_path_arg, "w") as TDfile:
        TDfile.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello From Funcs Module")
    print(get_todos())