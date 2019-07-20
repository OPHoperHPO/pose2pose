# Setup pose utils:
#### 1. Build [openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)
Build openpose with instruction documents of openpose python module API and install it.
Then you will get openpose libraries include `pyopenpose.lib`.

#### 3. Set an environment variable.
Set `OPENPOSE_ROOT` which includes `models` folder.  This is necessary to use pretrained models of openpose.

In Windows system, you can set with the command below.
```
set %OPENPOSE_ROOT%=YOUR_OPENPOSE_DIR 
```
Linux analog:
```
export OPENPOSE_ROOT=YOUR_OPENPOSE_DIR
```