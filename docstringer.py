# Add embarassing docstrings to all undocstrung functions
# Embarass yourself into adding real docstrings

filename = 'brians_test_file.py'
docstring = "'''BrianIsAnidiot'''\n"
new_lines = []

def is_function_def(line):
    if(('def ' in line) and (':' in line)):
        return True


def is_not_docstring(line):
    if ("'''" not in line):
        return True

with(open(filename,'r')) as f:
    lines = f.readlines()

    line_above = '' #keep track of the previous line - initialize empty
    for line in lines:

        if(is_function_def(line_above) and is_not_docstring(line)):
            new_lines.append(docstring)
        new_lines.append(line)
        line_above = line
f.close()

#out_filename = 'outfile.py'
out_filename = filename
out_file = open(out_filename, "w")
out_file.writelines(new_lines)
out_file.close()
