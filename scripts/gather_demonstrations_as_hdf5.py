#!/usr/bin/env python
"""Convert Recorded Data to hdf5 for Robomimic"""
import os, json

from robosuite import load_controller_config
from robosuite.scripts import collect_human_demonstrations

# simulator settings
controller_setting_fpath = os.path.join( os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) ), 'config/tele_osc.json')
controller_config = load_controller_config(custom_fpath=controller_setting_fpath)

config = {
    "env_name": "PickPlaceCan", #NutAssemblySingle PickPlace
    "robots": "Panda",
    "controller_configs": controller_config,
}

# data collection dir to be converted
folder_name = "PickPlaceCan_Jul18"
data_directory = os.path.join( os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) ), 'data_collection', folder_name)

goal_folder_name = "PickPlaceCan_Jul18_hdf5"
goal_data_directory = os.path.join( os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) ), 'data_collection', goal_folder_name)

env_info = json.dumps(config)

collect_human_demonstrations.gather_demonstrations_as_hdf5(data_directory, goal_data_directory, env_info)