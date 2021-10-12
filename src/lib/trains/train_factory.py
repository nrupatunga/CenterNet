from __future__ import absolute_import, division, print_function

from .ctdet import CtdetTrainer
from .ddd import DddTrainer
from .exdet import ExdetTrainer
from .multi_pose import MultiPoseTrainer

train_factory = {
    'exdet': ExdetTrainer,
    'ddd': DddTrainer,
    'ctdet': CtdetTrainer,
    'multi_pose': MultiPoseTrainer,
}
