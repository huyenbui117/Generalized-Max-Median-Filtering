import numpy as np
from numpy import ndarray
from numpy import random
from matplotlib import pyplot as plt
MAX_COLOR_SCALE = 255
NOISE_PERCENTAGE = 0.005

def get_image_scale(im: ndarray, c: int) -> ndarray:
    assert len(im.shape) == 3 and im.shape[-1] == 3
    return im[:,:,c]

def set_image_scale(im: ndarray, c: int, to: ndarray):
    assert len(im.shape) == 3 and im.shape[-1] == 3
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            im[i][j][c] = to[i][j]

def generate_noise(im: ndarray) -> ndarray:
    result: ndarray = MAX_COLOR_SCALE * np.ones(im.shape, dtype=im.dtype)
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            if random.random() > NOISE_PERCENTAGE:
                result[i][j] = im[i][j]
    return result

def generate_noise_rgb(im: ndarray) -> ndarray:
    result: ndarray = np.zeros(im.shape, dtype=im.dtype)
    for i in range(3):
        set_image_scale(result, i, generate_noise(get_image_scale(im, i)))
    return result

def get_converted_image(im: ndarray) -> ndarray:
    assert len(im.shape) == 3 and im.shape[-1] == 3
    b, g, r = cv2.split(im)
    return cv2.merge([r, g, b])

def plt_show(im: ndarray) -> ndarray:
    plt.imshow(get_converted_image(im))
    plt.show()