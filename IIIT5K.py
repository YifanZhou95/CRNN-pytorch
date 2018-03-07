import os
import torch
import torchvision.transforms as transforms
from torch.utils.data import Dataset, DataLoader
import PIL

class IIIT5K(Dataset):
    
    def __init__(self, root_dir, transform=None, train = True):
        self.root_dir = root_dir
        self.transform = transform
        self.train = train
        curr_dir=os.path.join(root_dir,'train' if train else 'test')
        file=open(os.path.join(root_dir,'train_Data.txt' if train else 'test_Data.txt'))
        self.files={os.path.join(curr_dir,line.strip().split(',')[0]):line.strip().split(',')[1] for line in file}
        vocab=[chr(ord('a')+i) for i in range(26)]+[chr(ord('A')+i) for i in range(26)]+[chr(ord('0')+i) for i in range(10)]
        self.chrToindex={}
        cnt=0
        for c in vocab:
            self.chrToindex[c]=cnt
            cnt+=1
                 
    def __len__(self):
        return len(self.files)
    
    def __getitem__(self, idx):
        img_name, label = list(self.files.items())[idx]
        image = PIL.Image.open(img_name).convert("RGB") # A few images are grayscale
        if self.transform:
            image = self.transform(image)
        sample = (image, label)
        return sample
