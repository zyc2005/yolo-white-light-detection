# YOLO White Light Detection

This repository contains a YOLO-based object detection project for detecting white light in images. The project includes dataset configuration, image preprocessing scripts, label correction, model weights, and training/inference setup.

## Project Overview

The goal of this project is to build a computer vision pipeline for detecting white light using YOLO. The project focuses on a single object class:

```text
white_light
```

The pipeline includes:

* Preparing a YOLO-format dataset
* Correcting image orientation using EXIF metadata
* Fixing YOLO label class IDs
* Training a YOLO object detection model
* Saving and reusing trained model weights

## Repository Structure

```text
.
├── README.md
├── data.yaml
├── scripts/
│   ├── fix_labels.py
│   └── fix_orientation.py
├── weights/
│   ├── previous_best.pt
│   └── yolo11n.pt
└── .gitignore
```

## Dataset Configuration

The dataset is configured in `data.yaml`:

```yaml
train: dataset_white_light/images/train
val: dataset_white_light/images/val

nc: 1
names: ['white_light']
```

The dataset should follow the standard YOLO format:

```text
dataset_white_light/
├── images/
│   ├── train/
│   └── val/
└── labels/
    ├── train/
    └── val/
```

## Preprocessing Scripts

### Fix Image Orientation

Some images may contain EXIF orientation metadata, which can cause them to appear rotated incorrectly during training or annotation.

The script below fixes image orientation and saves corrected images to a new folder:

```text
scripts/fix_orientation.py
```

By default, it reads images from:

```text
new_picture/
```

and saves corrected images to:

```text
fixed_new_picture/
```

### Fix YOLO Labels

Because this project only has one class, all YOLO label files should use class ID `0`.

The script below checks YOLO label files and changes any incorrect class ID to `0`:

```text
scripts/fix_labels.py
```

This ensures that all labels correspond to:

```text
white_light
```

## Model Weights

The `weights/` folder contains model weight files:

```text
weights/
├── yolo11n.pt
└── previous_best.pt
```

* `yolo11n.pt`: base YOLO model weights
* `previous_best.pt`: saved best checkpoint from previous training

## Installation

Install the required packages:

```bash
pip install ultralytics pillow
```

If you need to run map or visualization-related scripts in future extensions, additional packages may be required.

## Training

A typical YOLO training command is:

```bash
yolo detect train data=data.yaml model=weights/yolo11n.pt epochs=100 imgsz=640
```

After training, YOLO will save training outputs under the `runs/` directory.

## Inference

To run prediction using the saved model checkpoint:

```bash
yolo detect predict model=weights/previous_best.pt source=path/to/images
```

Replace `path/to/images` with the image folder or image file you want to test.

## Notes

Large datasets and training outputs are not included in this repository. If needed, they should be stored separately or managed with Git LFS.

Recommended files to exclude from normal Git tracking:

```text
runs/
dataset_white_light/
__pycache__/
```

## Author

Yuchen Zhang
