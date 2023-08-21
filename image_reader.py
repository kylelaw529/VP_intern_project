import os

directory = 'static'

# this dictionary is for testing purposes.
image_dictionary = {}
tagged_images = {}


file_paths = []

def image_reader(dict):
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            name = f.split('\\')[-1]
            dict[name] = f
            # storing image paths in file_paths for easy access
            file_paths.append(f)



def invert_tags(dict):
    inverted_dict = {}
    for k, v in dict.items():
        for i in range(len(v)):
            inverted_dict.setdefault(v[i], list()).append(k.split('\\')[-1])
    return inverted_dict
