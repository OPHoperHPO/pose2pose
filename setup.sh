git clone https://github.com/NVIDIA/pix2pixHD
git clone https://github.com/NVIDIA/apex
cd apex
pip install dominate
pip install -v --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" ./
cd ..