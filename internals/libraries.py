import random
import json
import os

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

import numpy as np

import nltk
nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

