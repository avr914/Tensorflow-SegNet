# Credit to https://stackoverflow.com/a/39110.

from tempfile import mkstemp
from shutil import move
from os import fdopen, remove, getcwd

DEFAULT_ROOT_PATH="/SegNet"

def replace_inplace(file_path, new_root_path, old_root_path=DEFAULT_ROOT_PATH):
    # Create temp file.
    fh, abs_path = mkstemp()
    with fdopen(fh,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(old_root_path, new_root_path))
    # Remove original file.
    remove(file_path)
    # Move new file.
    move(abs_path, file_path)

def replace(file_path, new_file_path, new_root_path, old_root_path=DEFAULT_ROOT_PATH):
    # Create new file
    with open(new_file_path, 'w') as new_file:
        with open(file_path, 'r') as old_file:
            for line in old_file:
                new_file.write(line.replace(old_root_path, new_root_path))

if __name__=="__main__":
    current_working_dir = getcwd()
    replace("test.txt", "test_fixed.txt", current_working_dir)
    replace("train.txt", "test_fixed.txt", current_working_dir)
    replace("val.txt", "test_fixed.txt", current_working_dir)