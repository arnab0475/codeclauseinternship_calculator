def copy_file(source_path, destination_path):
    with open(source_path, 'r') as source_file:
        content = source_file.read()

    with open(destination_path, 'w') as destination_file:
        destination_file.write(content)

source_file_path = input("Enter the file name: ")
destination_file_path = 'destination.txt'
copy_file(source_file_path, destination_file_path)
