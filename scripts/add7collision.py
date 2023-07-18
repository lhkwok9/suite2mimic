#!/usr/bin/env python
"""Copying the correct model.xml in the eldest demo to all other demo in the folder"""
import os
import shutil

data_folder = "../data_collection/PickPlaceCan_Jul18_original/"

for i, ep in enumerate(sorted(os.listdir(data_folder))):
    if i == 0:
        print('Reading the eldest xml file')
        xml_path = data_folder + ep + '/' + 'model.xml'
        continue
    shutil.copyfile(xml_path, data_folder + ep + '/' + 'model.xml')
print('Finished copying')