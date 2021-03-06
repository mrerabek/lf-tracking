from LFImage import LFImage
from TestSession import TestSession
from helper import Helper

# ---------------
# -- MAIN CODE --
# ---------------

images = []

# Add the images to be tested here
images.append(LFImage("I01R1"))
images.append(LFImage("I02R2"))
images.append(LFImage("I04R3"))

question = "How would you rate the impairment of the test image compared to the reference image?"
answers = [1, 2, 3, 4, 5]
answers_description = ["Very annoying",
                       "Annoying",
                       "Slightly annoying",
                       "Perceptible, but not annoying",
                       "Imperceptible"]

TestSession(images, question, answers, answers_description,
            show_preview=True, preload_images=True,
            assessment_method= Helper.IQA.DOUBLE_STIMULUS, test_image_side=Helper.Side.LEFT)
