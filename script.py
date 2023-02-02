# Food101 Image Classification -  Tommaso Fava

# DESCRIPTION

# Convolutional Neural Network (CNN) built with TensorFlow Lite which allows classification of
# the following classes of food:

# 0: pizza
# 1: spaghetti carbonara
# 2: tiramisù

# USAGE

# Insert a microSD card into the camera and put the model inside its root folder

import sensor, image, time, tf

sensor.reset()                         # reset and initialize the sensor
sensor.set_pixformat(sensor.RGB565)    # set pixel format to RGB565
sensor.set_framesize(sensor.VGA)       # set frame size to 320x240
sensor.skip_frames(time = 2000)        # let the camera adjust
clock = time.clock()

net = "food101.tflite"                            # load model
labels = ['pizza', 'carbonara', 'tiramisù']       # load labels

while(True):
    clock.tick()
    # take image
    img = sensor.snapshot()
    # classify
    for obj in tf.classify(net, img):
        print("\nPREDICTION:\n")
        # create a list of tuples (label, prediction) and sort it in descending order of probability
        sorted_list = sorted(zip(labels, obj.output()), key = lambda x: x[1], reverse = True)
        # print predictions
        for i in range(len(labels)):
            print("%s = %f" % (sorted_list[i][0], sorted_list[i][1]))
    print("\nFPS: ", clock.fps())
