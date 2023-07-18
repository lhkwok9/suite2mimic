# Installation

## Requirements
- Linux machine
- python 3.8.0
- conda
-------
## Option 1
Follow [installation](https://robomimic.github.io/docs/introduction/installation.html) of robomimic.

-------
## Option 2 (tested and adapted from Option 1) 

### Create and activate conda environemnt
```
conda create -n robomimic python=3.8.0
conda activate robomimic
```

### Install [Pytorch](https://pytorch.org/get-started/previous-versions/) that match the cuda version
Check CUDA Version:
```
nvidia-smi
```
For example, for CUDA Version 11.4:
```
conda install pytorch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 cudatoolkit=11.3 -c pytorch
```

### Install robomimic from source
```
cd ~/suite2mimic
git clone https://github.com/ARISE-Initiative/robomimic.git
cd robomimic
pip install -e .
```

### Install robosuite from source (simulator)
Note: git checkout is for reproducing experiments
```
cd ~/suite2mimic
git clone https://github.com/ARISE-Initiative/robosuite.git
cd robosuite
git checkout v1.4.1
pip install -r requirements.txt
```
-------
## Test installation
This assumes you follow option 2.
Run a quick debugging 2 epoch training, record testing videos and save the models:
```
cd ~/suite2mimic/robomimic
python examples/train_bc_rnn.py --debug
```
EGL exception is normal and is ignored.

Run a much more thorough test of several algorithms and scripts:
```
cd ~/suite2mimic/robomimic/tests
bash test.sh
```

# robosuite datasets
---
The following command are for [Demo data](data_collection/PickPlaceCan_Jul18_original)
1. get robosuite hdf5 format (edit folder_names and robosuite env config in the program)
```
cd ~/suite2mimic/scripts
python gather_demonstrations_as_hdf5.py
```

2. convert robsuite data to robomimic format ([robomimic instruction](https://robomimic.github.io/docs/datasets/robosuite.html#extracting-observations-from-mujoco-states))
```
cd ~/suite2mimic/robomimic/robomimic/scripts
python conversion/convert_robosuite.py --dataset ../../../data_collection/PickPlaceCan_Jul18_original_hdf5/demo.hdf5
```

3. extract observation from mujoco states
```
# For low dimensional observations only, with done on task success
python dataset_states_to_obs.py --dataset ../../../data_collection/PickPlaceCan_Jul18_original_hdf5/demo.hdf5 --output_name low_dim.hdf5 --done_mode 2

# For including image observations
python dataset_states_to_obs.py --dataset ../../../data_collection/PickPlaceCan_Jul18_original_hdf5/demo.hdf5 --output_name image.hdf5 --done_mode 2 --camera_names agentview robot0_eye_in_hand --camera_height 84 --camera_width 84

```

Possible error 1:
```
ValueError: No "geom" with name ... exists.
```
Reason to error 1:
the model.xml from the raw data of robosuite does not match that of robosuite that we are using

Solution to error 1:
run the following line and Ctrl-C after a few seconds
```
python /home/jk/suite2mimic/robosuite/robosuite/scripts/collect_human_demonstrations.py --environment PickPlaceCan
```
then [check the difference](https://www.diffchecker.com/text-compare/) and find the missing geom between the [model.xml](data_collection/PickPlaceCan_Jul18_original/ep_1689660868_9146771/model.xml) from the raw data and the model.xml generated in /tmp,
then add the geom line to the eldest file in the demo(e.g. add <geom name="robot0_link7_collision" type="mesh" rgba="0 0.5 0 1" mesh="robot0_link7"/> after line 281 in [ep_1689660868_9146771/model.xml](data_collection/PickPlaceCan_Jul18_original/ep_1689660868_9146771/model.xml))

