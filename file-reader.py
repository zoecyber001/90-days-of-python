def count_lines_and_words(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            line_count = len(lines)
            word_count = sum(len(line.split()) for line in lines)
        
        print(f'Total number of lines: {line_count}')
        print(f'Total number of words: {word_count}')
    
    except FileNotFoundError:
        print("The specified file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = input("Enter the path to the text file: ")
count_lines_and_words(file_path)
