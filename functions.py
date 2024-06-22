# We put 'FILEPATH' in below so that if we change
# the file name we can just do it in one place

FILEPATH = "todos.txt"


def get_todos(filepath="todos.txt"):
    """ Read a text file and return the list of
     to-do items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
