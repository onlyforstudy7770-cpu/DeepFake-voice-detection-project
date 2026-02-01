import librosa
import librosa.display
import matplotlib.pyplot as plt
import os
import numpy as np


folder = "/home/adarsh/2025uee1036/images_ray/archive/LA/LA/ASVspoof2019_LA_train/flac"
file = os.listdir(folder)
i = 0
for fil in file:
    y , src = librosa.load("/home/adarsh/2025uee1036/images_ray/archive/LA/LA/ASVspoof2019_LA_train/flac/" + fil , sr = 22000)
    mfcc = librosa.feature.mfcc( y = y , sr = src , n_mfcc= 13)
    np.save("temp_data/" + fil , mfcc)
    i += 1

print( i )

