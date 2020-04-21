


from typing import Callable, List, Tuple, Union

import numpy as np
import torch
from clloader.datasets import BaseDataset
from clloader import TaskSet
from torch.utils.data import Dataset as TorchDataset
from torchvision import transforms
from clloader import CLLoader

############
# IDEE: Avoir une classe CLLoader de base et plusieur autres spécifiques au scenarii

class ClassIncremental(CLLoader):
    """Continual Loader, generating datasets for the consecutive tasks.

    :param cl_dataset: A continual dataset.
    :param increment: Either number of classes per task, or a list specifying for
                      every task the amount of new classes.
    :param initial_increment: A different task size applied only for the first task.
                              Desactivated if `increment` is a list.
    :param train_transformations: A list of data augmentation applied to the train set.
    :param common_transformations: A list of transformations applied to both the
                                   the train set and the test set. i.e. normalization,
                                   resizing, etc.
    :param evaluate_on: How to evaluate on val/test, either on all `seen` classes,
                        on the `current` classes, or on `all` classes.
    :param class_order: An optional custom class order, used for NC.
    """

    # TODO

