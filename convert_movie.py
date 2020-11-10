import imageio
import numpy as np
from pathlib import Path
from PIL import Image

filename = Path('//Users/arminbahl/Desktop/Basler acA2040-90um (22778061)_20201106_171319879.m4v')
vid = imageio.get_reader(filename,  'ffmpeg')
input_fps = vid.get_meta_data()['fps']
print(input_fps)

writer = imageio.get_writer(str(filename.parent / filename.stem) + "_size_reduced.mp4", fps=input_fps, ffmpeg_params=["-b:v", "4M"])

for i, frame in enumerate(vid):
    frame = np.array(Image.fromarray(frame[:,:,0]).resize((512, 512)))
    print(frame.shape)
    writer.append_data(frame)

writer.close()