import os
import zipfile
import numpy as np

def infolist_to_dict(infolist):

    """return a dict with some key attributes from the ZipInfo object"""
     
    info_dict = {
        'filename':[],
        'file_size':[],
        'file_type':[],
        }

    for info in infolist:
        # is it faster to store fname as a temp var or access the attribute twice?
        fname = info.filename
        ftype = fname.split('.')[-1].lower()
        info_dict['filename'].append(fname)
        info_dict['file_size'].append(info.file_size)
        info_dict['file_type'].append(ftype)

    for k,v in info_dict.items():
        info_dict[k] = np.array(v)
    
    return info_dict


def number_of_files_summary(info_dict):
    
    ftypes = np.unique(info_dict['file_type'])
    print(f"number of files: {len(info_dict['file_type'])}")

    for ftype in ftypes:
        count = np.sum(info_dict['file_type'] == ftype)
        print("    {}: {:,}".format(ftype, count))  
    

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


def main(zipfile_obj):

    infolist = zipfile_obj.infolist()
    info_dict = infolist_to_dict(infolist)
    number_of_files_summary(info_dict)

    for find in ['max','min']:
        fname, size = find_max_or_min_file_size(info_dict, find=find)
        print('{} file size:\n    {} \n    {}'.format(find, fname, format_bytes(size)))

    size = info_dict['file_size'].mean()
    print('{} file size:\n    {}'.format('average', format_bytes(size)))

    return


if __name__ =='__main__':

    fpath = "../data/raw/graphische_sammlung_sample.zip"
    zipfile_obj = zipfile.ZipFile(fpath, "r")
    main(zipfile_obj)
