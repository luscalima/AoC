import re

directories = {}

def path_return(full_path):
    full_path = full_path.split('/')
    full_path.pop()

    return '/'.join(full_path)

def to_path(current_path, new_path):
    paths = re.findall('\w+', current_path)
    paths.append(new_path)

    return '/' + '/'.join(paths)

def mount(statements, directories):
    full_path = ''

    for statement in statements:
        if statement[0] =='$':
            _, cmd, *path = statement.split(' ')

            if cmd == 'cd':
                path = path[0]

                if path == '/':
                    full_path = path
                elif path == '..':
                    full_path = path_return(full_path)
                else:
                    full_path = to_path(full_path, path)

                if full_path not in directories:
                    directories[full_path] = 0

        else:
            file_size, file_name = statement.split(' ')

            if file_size != 'dir':
                directories[full_path] += int(file_size)
            else:
                directories[to_path(full_path, file_name)] = 0

def directory_size(directories, path):
    size = 0

    for directorie in directories:
        if path in directorie:
            size += directories[directorie]
    
    return size

with open('input.txt') as f:
    statements = f.read().strip().split('\n')
    
    mount(statements, directories)

    # Início - Código primeira parte
    size_sum = 0

    for path in directories:
        size = directory_size(directories, path)

        if size <= 100000:
            size_sum += size

    print(size_sum)
    # Fim

    # Início - Código segunda parte
    SPACE_AVALIABLE = 70000000
    REQUIRED_SPACE = 30000000
    root_directory_size = directory_size(directories, '/')
    current_unused_space = SPACE_AVALIABLE - root_directory_size
    need_to_release = REQUIRED_SPACE - current_unused_space

    is_enough = root_directory_size

    for path in directories:
        size = directory_size(directories, path)

        if size >= need_to_release and size <= is_enough:
            is_enough = size
    
    print(is_enough)
    # Fim

