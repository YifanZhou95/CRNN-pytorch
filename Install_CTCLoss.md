How to install CTCloss
see https://github.com/SeanNaren/warp-ctc/tree/pytorch_bindings/pytorch_binding

In ieng6 cluster:
```
launch-py3torch-gpu.sh -i ucsdets/instructional:ets-pytorch-py3-20180228v4
```

In workspace:
```
git clone https://github.com/SeanNaren/warp-ctc.git
cd warp-ctc
mkdir build; cd build
cmake ..
make
CUDA_HOME=/usr/local/cuda-8.0 python
cd ../pytorch_binding
python setup.py install --install-lib ~/warp-ctc/lib
```

In python code:
```
import sys
sys.path.append('YOUR_WORKSPACE_PATH/warp-ctc/lib')
```
To get the current workspace path, refer to linux command "pwd"
