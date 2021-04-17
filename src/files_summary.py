import os
import zipfile
import numpy as np
from pprint import pprint

from make_info_dict import make_info_dict


def number_of_files_summary(info_dict):
    
    ftypes = np.unique(info_dict['file_type'])
    print(f"number of files: {len(info_dict['file_type'])}")

    num_files_lst = []

    for ftype in ftypes:
        count = np.sum(info_dict['file_type'] == ftype)
        obj = {
            'type':ftype,
            'number':count
        }
        num_files_lst.append(obj)
        print("    {}: {:,}".format(ftype, count))


    return num_files_lst
    

def find_max_or_min_file_size(info_dict, find='max'):

    if find=='max':
        size = info_dict['file_size'].max()

    if find=='min':
        size = info_dict['file_size'].min()
    
    idx = np.where(info_dict['file_size'] == size)[0] # take first result
    fname = info_dict['filename'][idx][0]

    return fname, size


def format_bytes(size):
    # from https://stackoverflow.com/questions/12523586/python-format-size-application-converting-b-to-kb-mb-gb-tb
    # 2**10 = 1024
    power = 2**10
    n = 0
    power_labels = {0 : '', 1: 'kilo', 2: 'mega', 3: 'giga', 4: 'tera'}
    while size > power:
        size /= power
        n += 1

    label = power_labels[n]+'bytes'

    return "{:.3f} {}".format(size,label)


def main(info_dict):
    
    summary_dict = {}
    summary_dict['num_files'] = number_of_files_summary(info_dict)

    
    #num of images
    num_images = info_dict['is_image'].sum()

    print('number of images: {:,}'.format(num_images))
    summary_dict['num_images'] = num_images

    for find in ['max','min']:
        fname, size = find_max_or_min_file_size(info_dict, find=find)
        
        file_size_str = '{}  {}'.format(fname, format_bytes(size))
        print(f'{find} file size: {file_size_str}')
        summary_dict['{}_file_size'.format(find)] = file_size_str

    mean_file_size = info_dict['file_size'].mean()
    mean_file_size_frmtd = format_bytes(mean_file_size)
    mean_file_size_str = '{} file size:\n    {}'.format('average', mean_file_size_frmtd)
    print(mean_file_size_str)
    summary_dict['mean_file_size'] = mean_file_size_str

    return summary_dict


if __name__ =='__main__':

    fpath = "../data/raw/graphische_sammlung_sample.zip"
    zipfile_obj = zipfile.ZipFile(fpath, "r")
    info_dict = make_info_dict(zipfile_obj)
    main(info_dict)
