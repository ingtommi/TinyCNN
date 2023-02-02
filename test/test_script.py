# USE THIS TO AVOID REAL-TIME DETECTION

# This code allows the detection of images loaded into the microSD card

import image, time, tf

clock = time.clock()

net = "food101.tflite"                        # load model
labels = ['pizza', 'carbonara', 'tiramisù']   # load labels

img1 = image.Image("pizza.jpg")
img2 = image.Image("carbonara.jpg")
img3 = image.Image("tiramisu.jpg")
images = [img1, img2, img3]

while(True):
    clock.tick()
    # classify
    for img in images:
        for obj in tf.classify(net, img):
            print("\nPREDICTION:\n")
            # create a list of tuples (label, prediction) and sort it in descending order of probability
            sorted_list = sorted(zip(labels, obj.output()), key = lambda x: x[1], reverse = True)
            # print predictions
            for i in range(len(labels)):
                print("%s = %f" % (sorted_list[i][0], sorted_list[i][1]))
        print("\nFPS: ", clock.fps())
