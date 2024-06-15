<div align="center">
  
# TinyML :cake:

### A convolutional neural network running on an [OpenMV Cam H7 Plus](https://www.polimarcheracingteam.com/it/) board for the course in Embedded Systems.

</div>

# Specifications

* **Hardware:** OpenMV Cam H7 Plus
* **Dataset:** [Food-101](https://data.vision.ee.ethz.ch/cvl/datasets_extra/food-101/)
* **Libraries:** Keras, TensorFlow
* **Environment:** Google Colab, OpenMV IDE
* **Language:** Python

# Description

This Convolutional Neural Network (CNN) has been trained to **classify** images from **3** different classes of food:

* **pizza**
* **spaghetti carbonara**
* **tiramisù**

and it reaches an **accuracy** of over **80%**.

<img src="media/accuracy.jpg" width="50%" height="50%">

# Usage

Both the cases explained below require to move the model *food101.tflite* inside the board's microSD.

## Images from memory

Inside the folder [test](https://github.com/ingtommi/TinyML/tree/main/test) there are [script](https://github.com/ingtommi/TinyML/blob/main/test/test_script.py) and images to test the algorithm without the need to capture real-time images.

*NOTE:* images must be uploaded on the microSD!

## Real-time images

If you want to use the sensor as shown in the [video](https://github.com/ingtommi/TinyML/blob/main/media/video.mp4), it is sufficient to run the other [script](https://github.com/ingtommi/TinyML/blob/main/script.py).

*NOTE:* latency in the video is higher than the expected one because this video was recorded while using an older version of the model!
