#!/usr/bin/env python
import os
import shutil

data_folder = "/home/jk/dvrk2robosuite/src/dvrk2robosuite/data_collection/PickPlaceCan_Jul18/"

for i, ep in enumerate(sorted(os.listdir(data_folder))):
    if i == 0:
        xml_path = data_folder + ep + '/' + 'model.xml'
        continue
    shutil.copyfile(xml_path, data_folder + ep + '/' + 'model.xml')