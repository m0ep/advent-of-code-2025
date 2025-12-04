

def read_file_as_2d_array(input_file):
    with open(input_file) as f:
        return [list(line) for line in f.read().splitlines()]

def num_digits(num):
    return len(str(num))