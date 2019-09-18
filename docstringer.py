# Add embarassing docstrings to all undocstrung functions
# Embarass yourself into adding real docstrings

import os
import getpass
getpass.getuser()


try:
    embarassee = getpass.getuser()#can we make this insult personal?
except:
    embarassee = 'ThisProgrammer' #good enough

docstring = "'''" + str(embarassee) + "IsAnIdiot'''\n"
current_indentation = ''


dir_contents = os.listdir()
python_files = []
for file_or_dir in dir_contents:
    if file_or_dir[-3:] == '.py':
        python_files.append(file_or_dir)

def is_function_def(line):
    if(('def ' in line) and (':' in line)):
        return True


def is_not_docstring(line):
    if ("'''" not in line):
        return True


def get_indentation_of_line(line):
    try:
        stripped = line.lstrip()
        length_difference = len(line) - len(stripped)
        indentation_whitespace = line[:length_difference]
    except:
        indentation_whitespace = '\t'

    if len(indentation_whitespace) < 1:
        indentation_whitespace = '\t'

    assert(len(indentation_whitespace) > 0)
    return indentation_whitespace

def add_docstrings_to_python_file(filename):
    new_lines = []
    with(open(filename,'r')) as f:
        lines = f.readlines()

        line_above = '' #keep track of the previous line - initialize empty
        for line in lines:

            if(is_function_def(line_above) and is_not_docstring(line)):
                current_indentation = get_indentation_of_line(line)
                new_lines.append(current_indentation + docstring)
            new_lines.append(line)
            line_above = line
    f.close()

    out_filename = filename
    out_file = open(out_filename, "w")
    out_file.writelines(new_lines)
    out_file.close()

for python_file in python_files:
    add_docstrings_to_python_file(python_file)

print(add_docstrings_to_python_file.__doc__)