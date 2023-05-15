import wave

wav = wave.open('ChinaFM.wav', 'r')
num_channels = wav.getnchannels()
print(num_channels)
