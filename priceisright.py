# Edge Impulse - OpenMV Image Classification Example

import sensor, image, time, os, tf, pyb

sensor.reset()                         # Reset and initialize the sensor.
sensor.set_pixformat(sensor.GRAYSCALE) # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QVGA)      # Set frame size to QVGA (320x240)
sensor.set_windowing((160, 240))       # Set 160x240 window.
sensor.set_auto_exposure(True)

sensor.skip_frames(time=2000)          # Let the camera adjust.

net = "trained.tflite"
labels = [line.rstrip('\n') for line in open("labels.txt")]

clock = time.clock()
price = [0,0,0]
count = 0
index = 0

while(True):
    clock.tick()
    count+=1
    print("%d" % count)
    img = sensor.snapshot()

    # default settings just do one detection... change them to search the image...
    for obj in tf.classify(net, img, min_scale=1.0, scale_mul=0.8, x_overlap=0.5, y_overlap=0.5):
        print("**********\nPredictions at [x=%d,y=%d,w=%d,h=%d]" % obj.rect())
        img.draw_rectangle(obj.rect())
        # This combines the labels and confidence values into a list of tuples
        predictions_list = list(zip(labels, obj.output()))


        for i in range(len(predictions_list)):
           print("%s = %f" % (predictions_list[i][0], predictions_list[i][1]))

           if predictions_list[i][0] == '0' and predictions_list[i][1] > 0.6:
             print("0")
             if count > 20:
               price[index] = predictions_list[i][0]
               index+=1
               count = 0
               if index > 2:
                 index = 0
             buf = "Price = \n%s.%s%s\n" % (price[0], price[1], price[2])
             img.draw_string(10,150, buf, scale=4, mono_space=False)
             img.draw_string(10,0, "0", scale=5, mono_space=False)
           elif predictions_list[i][0] == '1' and predictions_list[i][1] > 0.6:
             print("1")
             if count > 20:
               price[index] = predictions_list[i][0]
               index+=1
               count = 0
               if index > 2:
                 index = 0
             buf = "Price = \n%s.%s%s\n" % (price[0], price[1], price[2])
             img.draw_string(10,150, buf, scale=4, mono_space=False)
             img.draw_string(10,0, "1", scale=5, mono_space=False)
           elif predictions_list[i][0] == '2' and predictions_list[i][1] > 0.6:
             print("2")
             if count > 20:
               price[index] = predictions_list[i][0]
               index+=1
               count = 0
               if index > 2:
                 index = 0
             buf = "Price = \n%s.%s%s\n" % (price[0], price[1], price[2])
             img.draw_string(10,150, buf, scale=4, mono_space=False)
             img.draw_string(10,0, "2", scale=5, mono_space=False)
           elif predictions_list[i][0] == '3' and predictions_list[i][1] > 0.6:
             print("3")
             if count > 20:
               price[index] = predictions_list[i][0]
               index+=1
               count = 0
               if index > 2:
                 index = 0
             buf = "Price = \n%s.%s%s\n" % (price[0], price[1], price[2])
             img.draw_string(10,150, buf, scale=4, mono_space=False)
             img.draw_string(10,0, "3", scale=5, mono_space=False)
           elif predictions_list[i][0] == '4' and predictions_list[i][1] > 0.6:
             print("4")
             if count > 20:
               price[index] = predictions_list[i][0]
               index+=1
               count = 0
               if index > 2:
                 index = 0
             buf = "Price = \n%s.%s%s\n" % (price[0], price[1], price[2])
             img.draw_string(10,150, buf, scale=4, mono_space=False)
             img.draw_string(10,0, "4" ,scale=5, mono_space=False)
           elif predictions_list[i][0] == '5' and predictions_list[i][1] > 0.5:
             print("5")
             if count > 20:
               price[index] = predictions_list[i][0]
               index+=1
               count = 0
               if index > 2:
                 index = 0
             buf = "Price = \n%s.%s%s\n" % (price[0], price[1], price[2])
             img.draw_string(10,150, buf, scale=4, mono_space=False)
             img.draw_string(10,0, "5", scale=5, mono_space=False)
           elif predictions_list[i][0] == '6' and predictions_list[i][1] > 0.6:
             print("6")
             if count > 20:
               price[index] = predictions_list[i][0]
               index+=1
               count = 0
               if index > 2:
                 index = 0
             buf = "Price = \n%s.%s%s\n" % (price[0], price[1], price[2])
             img.draw_string(10,150, buf, scale=4, mono_space=False)
             img.draw_string(10,0, "6", scale=5, mono_space=False)

           elif predictions_list[i][0] == '7' and predictions_list[i][1] > 0.6:
             print("7")
             if count > 20:
               price[index] = predictions_list[i][0]
               index+=1
               count = 0
               if index > 2:
                 index = 0
             buf = "Price = \n%s.%s%s\n" % (price[0], price[1], price[2])
             img.draw_string(10,150, buf, scale=4, mono_space=False)
             img.draw_string(10,10, "7", scale=5, mono_space=False)
           elif predictions_list[i][0] == '8' and predictions_list[i][1] > 0.6:
             print("8")
             if count > 20:
               price[index] = predictions_list[i][0]
               index+=1
               count = 0
               if index > 2:
                 index = 0
             buf = "Price = \n%s.%s%s\n" % (price[0], price[1], price[2])
             img.draw_string(10,150, buf, scale=4, mono_space=False)
             img.draw_string(10,0, "8", scale=5, mono_space=False)
           elif predictions_list[i][0] == '9' and predictions_list[i][1] > 0.6:
             print("9")
             if count > 20:
               price[index] = predictions_list[i][0]

               index+=1
               count = 0
               if index > 2:
                 index = 0
             buf = "Price = \n%s.%s%s\n" % (price[0], price[1], price[2])
             img.draw_string(10,150, buf, scale=4, mono_space=False)
             img.draw_string(10,0, "9", scale=5, mono_space=False)

        print(clock.fps(), "fps")
        print(price)
        buf2 = "%s" % index
        img.draw_string(120,0, buf2, scale = 4, mono_space=False)
