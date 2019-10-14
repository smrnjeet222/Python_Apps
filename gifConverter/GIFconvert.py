import imageio
import os

clip = os.path.abspath('ForGIF.mp4')

def ToGIF(inputPath , targetFormat):
    
    outputPath = os.path.splitext(inputPath)[0] + targetFormat
    print(f'Converting {inputPath} to {outputPath}')

    reader = imageio.get_reader(inputPath)
    fps = reader.get_meta_data()['fps']

    writer = imageio.get_writer(outputPath , fps=fps)

    for frames in reader:
        writer.append_data(frames)
        print (f'Frame{frames}')

    print('DONE!')

    writer.close()



ToGIF(clip , '.gif')

