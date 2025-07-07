def show_file_content(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print("Содержимое файла:")
            print(content)
    except FileNotFoundError:
        print(f"Файл по пути '{file_path}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Пример использования
if __name__ == "__main__":
    # Укажи путь к файлу относительно места запуска скрипта
    show_file_content("src/names.txt")