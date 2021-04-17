import os
from make_info_dict import make_info_dict
import zipfile
import numpy as np
from pathlib import Path
import webbrowser

import make_collage
import files_summary

def make_nested_filepath_tree(paths):
    
    """https://stackoverflow.com/questions/66994061/convert-list-of-file-paths-to-a-nested-dictionary-similar-to-a-json-file"""
        
    # Sort so deepest paths are first
    paths = sorted(paths, key = lambda s: len(s.lstrip('/').split('/')), reverse = True)

    tree_path = {}
    for path in paths:
        # Split into list and remove leading '/' if present
        levels = path.lstrip('/').split("/")
        
        file = levels.pop()
        acc = tree_path
        for i, p in enumerate(levels, start = 1):
            if i == len(levels):
                # Reached termination of a path
                # Use current terminal object is present, else use list
                acc[p] = acc[p] if p in acc else []
                if isinstance(acc[p], list):
                    # Only append if we are at a list
                    acc[p].append(file)
            else:
                # Exaand with dictionary by default
                acc.setdefault(p, {})
            acc = acc[p]

    return tree_path


def reformat_nested_dict_for_treeviewer(in_dict):
    
    """recursive function to convert nested dictionary to format needed for vuetify treeviewer copmonent"""
    tree = []
    sorted_keys = np.sort(list(in_dict.keys()))
    for i, key in enumerate(sorted_keys):
        
        value = in_dict[key]
        if isinstance(value, dict):
            # call function recursively if the children are a dictionary
            children = format_for_treeviewer(value)
        elif isinstance(value, list):
            children = []
            for i, val in enumerate(value):
                children.append(
                    {'id':i,
                    'name':val
                    }
                )
        
        obj = {
            'id':i,
            'name':key,
            'children': children
            }
        
        tree.append(obj)
    
    return tree


def format_filelist_for_treeview(fpath_list):
    tree = make_nested_filepath_tree(fpath_list)
    treeviewer = reformat_nested_dict_for_treeviewer(tree)
    
    return treeviewer


def get_output_dir():
    downloads_path = os.path.join(Path.home(), "Downloads")
    #overwrite for WSL2
    downloads_path = '/mnt/c/users/barry/Downloads'
    output_dir = str(os.path.join(downloads_path, "DataDiver-Report"))

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    return output_dir


if __name__ == '__main__':


    fpath = "../data/raw/graphische_sammlung_sample.zip"
    zipfile_obj = zipfile.ZipFile(fpath, "r")

    output_dir = get_output_dir()


    # Outputs from the other modules
    info_dict = make_info_dict(zipfile_obj)
    summary_dict = files_summary.main(info_dict)
    treeview_list = format_filelist_for_treeview(info_dict['filename'])

    make_collage.main(zipfile_obj, info_dict, output_dir)


    # format template
    with open('../reports/template.html', mode='r') as temp:
      template = temp.read()

    template = template.replace('-FILETREE-', str(treeview_list))
    template = template.replace('-FILENAME-', f"'{fpath}'")
    template = template.replace('-SUMMARY_DICT-', str(summary_dict))


    # write html preview
    fpath = os.path.join(output_dir,'preview.html')
    with open(fpath,'w') as f:
        f.write(template)

    fpath = "file://" + os.path.abspath(fpath)
    print("wrote file summary to : ", fpath)
    fpath = fpath.replace('/mnt/c/users','/C:/Users')
    webbrowser.open(fpath)