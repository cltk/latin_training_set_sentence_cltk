import os
import re

root = os.path.abspath('./')
orig = os.path.join(root,'training_set/')
files = os.listdir(orig)
training_set = ''
word_count = 0
for file in files:
    with open(orig + file) as f:
        print(file)
        read = f.read()
        line_breaks = re.sub(r'([a-z]+)(\.|;|\?|:)\s([\w]+)', r'\1\2\n\3', read)
        no_section_num = re.sub(r'\[.+\]', r'', line_breaks)
        no_digits = re.sub(r'\d', r'', no_section_num)
        no_file_data_1 = re.sub(r'The Latin Library|The Classics Page|', r'', no_digits)
        no_file_data_2 = re.sub(r'Cicero|\: In Catilinam .*|ORATIO.*', r'', no_file_data_1)
        no_file_data_3 = re.sub(r'Augstine|\: Confessions .*|AUGUSTINI.*', r'', no_file_data_2)
        no_file_data_4 = re.sub(r'Cato|\: M. PORCI CATONIS .*|DE AGRI CVLTVRA', r'', no_file_data_3)
        no_file_data_5 = re.sub(r'In Verrem .*|ACTIONIS IN C. VERREM .*|LIBER .*', r'', no_file_data_4)
        no_double_end_ns = re.sub(r'\n\s*', '\n', no_file_data_5)
        no_double_start_ns = re.sub(r'\s*\n', '\n', no_double_end_ns)
        no_ascii_junk = re.sub(r'@|#|\$|%|\^|&|\*', '', no_double_start_ns)
        print(no_ascii_junk)
        word_count += len(no_ascii_junk.split(' '))
print(word_count)