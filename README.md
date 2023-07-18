# suite2mimic

## Installation

### Requirements
- Linux machine
- python 3.8.0
- conda
-------
### Option 1
Follow [installation](https://robomimic.github.io/docs/introduction/installation.html) of robomimic.
-------
### Option 2 (tested and adapted from Option 1) 

#### Create and activate conda environemnt
```
conda create -n robomimic python=3.8.0
conda activate robomimic
```
-------
#### Install [Pytorch](https://pytorch.org/get-started/previous-versions/) that match the cuda version
Check CUDA Version:
```
nvidia-smi
```
For example, for CUDA Version 11.4:
```
conda install pytorch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 cudatoolkit=11.3 -c pytorch
```
-------
#### Install robomimic from source
```
cd ~/suite2mimic
git clone https://github.com/ARISE-Initiative/robomimic.git
cd robomimic
pip install -e .
```
-------
#### Install robosuite from source (simulator)
Note: git checkout is for reproducing experiments
```
cd ~/suite2mimic
git clone https://github.com/ARISE-Initiative/robosuite.git
cd robosuite
git checkout v1.4.1
pip install -r requirements.txt
```
-------
### Test installation
This assumes you follow option 2.
Run a quick debugging 2 epoch training, record testing videos and save the models:
```
cd ~/suite2mimic/robomimic
python examples/train_bc_rnn.py --debug
```
EGL exception is normal and is ignored
-------
Run a much more thorough test of several algorithms and scripts:
```
cd ~/suite2mimic/robomimic/tests
bash test.sh
```

## robosuite datasets (Demo with data_collection/PickPlaceCan_Jul18_original)


