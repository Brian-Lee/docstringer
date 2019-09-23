# Add embarassing docstrings to all undocstrung functions
# Embarass yourself into adding real docstrings
# TODO: improve is_function_def() - at least some false positives
#       improve is_not_docstring() - at least some false negatives
#
#   It would be nice if we could get all the help docs for all functions and see thst they are all done correctly
#
##################################################################


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
    if((line.lstrip()[:3] == 'def') and line.rstrip()[-1] == ':' ):
        return True

def is_not_docstring(line):
    if (line.lstrip()[:3] != "'''"):
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

    out_filename = filename #write to the same file we read from
    out_file = open(out_filename, "w")
    out_file.writelines(new_lines)
    out_file.close()

for python_file in python_files:
    add_docstrings_to_python_file(python_file)

#print(add_docstrings_to_python_file.__doc__)