import librosa
import librosa.display
import matplotlib.pyplot as plt

y , src =  librosa.load("LA_D_1000265.flac" , sr = 16000)

mfcc = librosa.feature.mfcc( y = y , sr = src , n_mfcc= 13)

print(type(y))
print(type(src))
print(type(mfcc))

plt.figure(figsize = (10 , 4))
librosa.display.specshow( mfcc , x_axis= 'time')
plt.colorbar()
plt.title("mfsfhiuf")
plt.tight_layout()
plt.show()
