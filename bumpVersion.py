import os
def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return content.split('.')
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return []
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
        return []

def write_file(file_path, data):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(data)
    except Exception as e:
        print(f"Произошла ошибка при записи в файл: {e}")

def version_up(file_path, version_type):
    parts = read_file(file_path)

    if not parts:
        print("Файл пуст или не удалось прочитать его содержимое.")
        return

    try:
        major, minor, patch = map(int, parts)
    except ValueError:
        print("Файл содержит некорректные данные (ожидались числа, разделённые точками).")
        return


    if version_type == 'major':
        major += 1
        minor = 0
        patch = 0
    elif version_type == 'minor':
        minor += 1
        patch = 0
    elif version_type == 'patch':
        patch += 1
    else:
        print("Некорректный тип версии. Используйте 'major', 'minor' или 'patch'.")
        return


    new_version = f"{major}.{minor}.{patch}"
    write_file(file_path, new_version)
    print(f"Версия успешно обновлена: {new_version}")

def check_file(file_path):
    if not os.path.isfile(file_path):
        write_file(file_path, '1.0.0')

file_path = "/Users/li6ri9ka/PycharmProjects/version_up/src/version_controller"
check_file(file_path)
version_up(file_path, 'minor')