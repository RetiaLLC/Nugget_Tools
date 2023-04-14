import os
import sys
from glob import glob

def is_duckyscript(file_path, valid_commands):
    total_lines = 0
    valid_lines = 0

    with open(file_path, 'r') as file:
        for line in file:
            total_lines += 1
            first_word = line.split()[0] if line.split() else ''
            if first_word in valid_commands:
                valid_lines += 1

    valid_percentage = (valid_lines / total_lines) * 100
    return valid_percentage >= 80

def convert_to_catscratch(file_path, output_file_path):
    replacements = {
        'STRING': 'TYPE',
        'DELAY': 'WAIT',
        'REM': '//'
    }

    with open(file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        output_file.write("// Converted by ScratchChecker V0.1\n")

        for line in input_file:
            first_word = line.split()[0] if line.split() else ''
            rest = ' '.join(line.split()[1:])

            if first_word in replacements:
                output_file.write(f"{replacements[first_word]} {rest}\n")
            else:
                output_file.write(line)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Error: Please provide a valid file or directory.")
        sys.exit(1)

    input_path = sys.argv[1]

    if os.path.isdir(input_path):
        files = glob(os.path.join(input_path, '*.txt'))
    elif os.path.isfile(input_path):
        files = [input_path]
    else:
        print("Error: Please provide a valid file or directory.")
        sys.exit(1)

    valid_commands = {"REM", "DEFAULT_DELAY", "DELAY", "STRING", "GUI", "ALT", "SHIFT", "CONTROL", "MENU", "ENTER", "ESCAPE", "TAB", "SPACE", "DELETE", "INSERT", "HOME", 
"END", "PAGEUP", "PAGEDOWN", "UPARROW", "DOWNARROW", "LEFTARROW", "RIGHTARROW", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12", "PRINTSCREEN", 
"SCROLLLOCK", "PAUSE", "CAPSLOCK", "NUMLOCK", "BREAK", "REPEAT", "REM_ALL"}

    for file in files:
        if is_duckyscript(file, valid_commands):
            print(f"Processing {file}...")
            output_file = os.path.join(os.path.dirname(file), f"CatScratch_{os.path.basename(file)}")
            convert_to_catscratch(file, output_file)
        else:
            print(f"Skipping {file} (not a valid DuckyScript file)")

    print("Conversion completed.")

