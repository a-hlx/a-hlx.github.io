

dir()
help()

Dataset
Dataloader

tensorboard

| PIL          | tensor                | narrys     |
|:-------------|:----------------------|:------------|
| Image.open() | transforms.ToTensor() | cv.imread() |  

使用GPU训练：

.cuda()


# MODULE

```python
import torch.nn as nn
import torch.nn.functional as F

class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 20, 5)
        self.conv2 = nn.Conv2d(20, 20, 5)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        return F.relu(self.conv2(x))
```

# TORCH.NN.FUNCTIONAL.CONV2D

torch.nn.functional.conv2d(_input_, _weight_, _bias=None_, _stride=1_, _padding=0_, _dilation=1_, _groups=1_) → [Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor "torch.Tensor")[](https://pytorch.org/docs/stable/generated/torch.nn.functional.conv2d.html#torch.nn.functional.conv2d)

Applies a 2D convolution over an input image composed of several input planes.

-   **input** – input tensor of shape $(\text{minibatch} , \text{in\_channels} , iH , iW)$
    
-   **weight** – filters of shape$(\text{out\_channels} , \frac{\text{in\_channels}}{\text{groups}} , kH , kW)$
    
-   **bias** – optional bias tensor of shape $(\text{out\_channels})$. Default: `None`
    
-   **stride** – the stride of the convolving kernel. Can be a single number or a tuple (sH, sW). Default: 1
    
-   **padding** –
    implicit paddings on both sides of the input. Can be a string {‘valid’, ‘same’}, single number or a tuple (padH, padW). Default: 0 `padding='valid'` is the same as no padding. `padding='same'` pads the input so the output has the same shape as the input. However, this mode doesn’t support any stride values other than 1.

```python
# With square kernels and equal stride
filters = torch.randn(8, 4, 3, 3)
inputs = torch.randn(1, 4, 5, 5)
F.conv2d(inputs, filters, padding=1)
```

# CONV2D

_CLASS_torch.nn.Conv2d(_in_channels_, _out_channels_, _kernel_size_, _stride=1_, _padding=0_, _dilation=1_, _groups=1_, _bias=True_, _padding_mode='zeros'_, _device=None_, _dtype=None_)[[SOURCE]]()[](https://pytorch.org/docs/stable/generated/torch.nn.Conv2d.html#torch.nn.Conv2d)

Applies a 2D convolution over an input signal composed of several input planes.

Parameters:

-   **in_channels** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.10)")) – Number of channels in the input image  
-   **out_channels** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.10)")) – Number of channels produced by the convolution    
-   **kernel_size** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.10)") _or_ [_tuple_](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.10)")) – Size of the convolving kernel   
-   **stride** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.10)") _or_ [_tuple_](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.10)")_,_ _optional_) – Stride of the convolution. Default: 1    
-   **padding** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.10)")_,_ [_tuple_](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.10)") _or_ [_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.10)")_,_ _optional_) – Padding added to all four sides of the input. Default: 0
-   **padding_mode** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.10)")_,_ _optional_) – `'zeros'`, `'reflect'`, `'replicate'` or `'circular'`. Default: `'zeros'`
-   **dilation** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.10)") _or_ [_tuple_](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.10)")_,_ _optional_) – Spacing between kernel elements. Default: 1
-   **groups** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.10)")_,_ _optional_) – Number of blocked connections from input channels to output channels. Default: 1
-   **bias** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.10)")_,_ _optional_) – If `True`, adds a learnable bias to the output. Default: `True`

# MAXPOOL2D
[](https://pytorch.org/docs/stable/generated/torch.nn.MaxPool2d.html#maxpool2d)
下采样
_CLASS_torch.nn.MaxPool2d(_kernel_size_, _stride=None_, _padding=0_, _dilation=1_, _return_indices=False_, _ceil_mode=False_)[[SOURCE]]()[](htthttps://pytorch.org/docs/stable/_modules/torch/nn/modules/pooling.html#MaxPool2dps://pytorch.org/docs/stable/generated/torch.nn.MaxPool2d.html#torch.nn.MaxPool2d)

Applies a 2D max pooling over an input signal composed of several input planes.

```python
# pool of square window of size=3, stride=2
m = nn.MaxPool2d(3, stride=2)
# pool of non-square window
m = nn.MaxPool2d((3, 2), stride=(2, 1))
input = torch.randn(20, 16, 50, 32)
output = m(input)
```

# RELU
[](https://pytorch.org/docs/stable/generated/torch.nn.ReLU.html#relu)

_CLASS_torch.nn.ReLU(_inplace=False_)[[SOURCE]](https://pytorch.org/docs/stable/_modules/torch/nn/modules/activation.html#ReLU)[](https://pytorch.org/docs/stable/generated/torch.nn.ReLU.html#torch.nn.ReLU)

Applies the rectified linear unit function element-wise:

$\text{ReLU}(x) = (x)^+ = \max(0, x)ReLU(x)=(x)+=max(0,x)$

Parameters:

**inplace** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.10)")) – can optionally do the operation in-place. Default: `False`

Shape:

-   Input: (*)(∗), where *∗ means any number of dimensions.
    
-   Output: (*)(∗), same shape as the input.

```python
  >>> m = nn.ReLU()
  >>> input = torch.randn(2)
  >>> output = m(input)

An implementation of CReLU - https://arxiv.org/abs/1603.05201

  >>> m = nn.ReLU()
  >>> input = torch.randn(2).unsqueeze(0)
  >>> output = torch.cat((m(input),m(-input)))
```

