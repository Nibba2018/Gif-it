import imageio, os

def gif_it(inputPath, targetFormat):

    outputPath = os.path.splitext(inputPath)[0] + targetFormat

    reader = imageio.get_reader(inputPath)
    fps = reader.get_meta_data()['fps']

    writer = imageio.get_writer(outputPath, fps=fps)

    for frames in reader:
        writer.append_data(frames)

    writer.close()

if __name__ == "__main__":
    clip = os.path.abspath('clip.mp4')
    gif_it(clip, ".gif")