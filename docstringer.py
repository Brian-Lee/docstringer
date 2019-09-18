# Add embarassing docstrings to all undocstrung functions
# Embarass yourself into adding real docstrings

filename = 'brians_test_file.py'
docstring = "'''BrianIsAnidiot'''"
new_lines = []

def is_function_def(line):
    return True


def is_not_docstring(line):
    return True


with(open(filename,'r')) as f:
    lines = f.readlines()

    line_above = '' #keep track of the previous line - initialize empty
    for line in lines:
        new_lines.append(line)
        if(is_function_def(line_above) and is_not_docstring(line)):
            new_lines.append(docstring)
f.close()

print(new_lines)
#with(open(filename,'w')) as f: