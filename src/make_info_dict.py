import os
import zipfile
import numpy as np



def check_is_image(ftype):

    return ftype in ['jpg', 'jpeg', 'png']


def infolist_to_dict(infolist):

    """return a dict with some key attributes from the ZipInfo object"""
     
    info_dict = {
        'filename':[],
        'file_size':[],
        'file_type':[],
        'is_image':[]
        }

    for info in infolist:
        # is it faster to store fname as a temp var or access the attribute twice?
        fname = info.filename
        ftype = fname.split('.')[-1].lower()
        info_dict['filename'].append(fname)
        info_dict['file_size'].append(info.file_size)
        info_dict['file_type'].append(ftype)
        info_dict['is_image'].append(check_is_image(ftype))

    for k,v in info_dict.items():
        info_dict[k] = np.array(v)
    
    return info_dict