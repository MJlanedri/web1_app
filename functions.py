FILEPATH = 'todos.txt'
def get_methods(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
        file_local.close()


if __name__ == "__main__":
    print(__name__)
