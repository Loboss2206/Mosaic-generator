# Image Mosaic Generator

This is a simple Python script that generates an image mosaic using a collection of patch images. The mosaic is created by replacing each block of the main image with a patch image that best matches the color of the block.

## 🚀 Usage

1. Place your main image in the root directory or use one that is already there.
2. Change the **main_image_name** in the main of the file *mosaic_generator.py* by the name of your image.
3. Change the **block size** in the main of the *mosaic generator.py* file to the size you want each patch to have.
4. Run the script using the command:

```bash
python3 mosaic_generator.py
```

The resulting mosaic image will be displayed using matplotlib.

## 📋 Requirements

* Clone the project by assuming you have Git installed. Open your terminal and type:

```bash
git clone 'https://github.com/Loboss2206/Mosaic-generator.git'
```

* Python 3.10.0+

* Install all the necessary requirements by executing the following command in the project directory:

```bash
pip install -r requirements.txt
```

## 💡 How It Works

1. The main image and patch images are loaded.
2. The mean color of each patch image and each block of the main image is calculated.
3. For each block in the main image, the best-matching patch image is selected based on color similarity.
4. The selected patch images are resized to match the block size and assembled to create the mosaic image.

## 🙌 Credits

This mini-project was created as a demonstration of generating image mosaics using Python. It's meant to showcase the use of image processing and basic machine learning concepts for color matching.
