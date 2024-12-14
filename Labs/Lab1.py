def read_file_python(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read()
            print("File content:")
            print(data)
    except FileNotFoundError:
        print("Error: file not found")
    except PermissionError:
        print("Error: Permission denied")
    except Exception as e:
        print(f"error occurred: {e}")

read_file_python("randomtext.txt")