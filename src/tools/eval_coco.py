from __future__ import absolute_import, division, print_function

import os
import pickle
import sys

import cv2
import numpy as np
import pycocotools.coco as coco
from pycocotools.cocoeval import COCOeval

this_dir = os.path.dirname(__file__)
ANN_PATH = this_dir + '../../data/coco/annotations/instances_val2017.json'
print(ANN_PATH)
if __name__ == '__main__':
    pred_path = sys.argv[1]
    coco = coco.COCO(ANN_PATH)
    dets = coco.loadRes(pred_path)
    img_ids = coco.getImgIds()
    num_images = len(img_ids)
    coco_eval = COCOeval(coco, dets, "bbox")
    coco_eval.evaluate()
    coco_eval.accumulate()
    coco_eval.summarize()
