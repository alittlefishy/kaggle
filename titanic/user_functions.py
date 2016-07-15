"""
@author: alittlefishy
"""

# Imports

import csv
import random

#Arguments

#Function Definitions

def read_csv(input_file, delimiter=','):
    '''
    Parameters:
    1. input_file: input file name
    2. delimiter: default delimiter=','
    '''

    with open(input_file, 'rb') as f:
        reader = csv.reader(f, delimiter)
        for row in reader:
            yield row

def read_csv_in_dict(input_file, delimiter=','):
    '''
    Parameters:
    1. input_file: input file name
    2. delimiter: default delimiter=','
    '''

    with open(input_file, 'rb') as f:
        reader = csv.DictReader(f, delimiter=delimiter)
        for row in reader:
            yield row

def generate_lst_of_index(big_lst, small_lst):
    '''
    Parameters:
    1. big_lst: a big list
    2. small_lst: a small list
    '''

    pos=[]
    for index, s in enumerate(big_lst):
        if s in small_lst:
            pos.append(index)
    return pos

def write_selected_col_to_file(input_file, output_file, lst_of_pos, delimiter=','):
    '''
    Parameters:
    1. input_file: input file name
    2. output_file: output file name
    3. lst_of_pos: a list containing the index of columns needed
    4. delimiter: default delimiter=','
    '''

    input_rows = read_csv(input_file)
    with open(output_file, 'wb') as f:
        writer = csv.writer(f, delimiter=delimiter)
        for input_row in input_rows:
            writer.writerow([input_row[i] for i in lst_of_pos])

def random_sampling(input_file, prop, output_file, delimiter=','):
    '''
    Parameters:
    1. input_file: input file name
    2. prop: proportion of observations sampled
    3. output_file: output file name
    4. delimiter: default delimiter=','
    '''

    input_rows = read_csv(input_file)
    headers = input_rows.next()
    with open(output_file, 'wb') as f:
        writer = csv.writer(f, delimiter=delimiter)
        writer.writerow(headers)
        for input_row in input_rows:
            if random.random() <= prop:
                writer.writerow(input_row)

def split_into_build_and_val(input_file, test_prop, build_file, val_file, delimiter=','):
    '''
    Parameters:
    1. input_file: input file name
    2. test_prop: proportion of observations used for validation
    3. build_file: output file name for build dataset
    4. val_file: output file name for validation dataset
    5. delimiter: default delimiter=','
    '''

    input_rows = read_csv(input_file)
    headers = input_rows.next()
    with open(build_file, 'wb') as bf:
        bwriter=csv.writer(bf, delimiter=delimiter)
        bwriter.writerow(headers)
        with open(val_file, 'wb') as vf:
            vwriter = csv.writer(vf, delimiter=delimiter)
            vwriter.writerow(headers)
            for input_row in input_rows:
                if random.random() <= test_prop:
                    vwriter.writerow(input_row)
                else:
                    bwriter.writerow(input_row)

def select_time_range(input_file, output_file, time_var, time_range, delimiter=','):
    '''
    Parameters:
    1. input_file: input file name
    2. output_file: output file name
    3. time_var: name of column that contains the time variable
    4. time_range: a list that contains the desired time range
    5. delimiter: default delimiter=','
    '''

    input_rows = read_csv(input_file)
    headers = input_rows.next()
    ind = headers.index(time_var)
    with open(output_file, 'wb') as f:
        writer = csv.writer(f, delimiter=delimiter)
        writer.writerow(headers)
        for input_row in input_rows:
            if input_row[ind] in time_range:
                writer.writerow(input_row)

def main():
    pass

# Main

if __name__ == '__main__':
    pass
