"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'

def main():
    final_image = SimpleImage.blank(WIDTH, HEIGHT)

    # TODO: your code here
    # This is an example which should generate a pinkish patch
    patch = make_recolored_patch(1.5, 0, 1.5)
    for y in range(patch.height):
        for x in range(patch.width):
            pixel = patch.get_pixel(x, y)
            final_image.set_pixel(x, y, pixel)
            final_image.set_pixel(x+222, y, pixel)
            final_image.set_pixel(x+444, y, pixel)
            final_image.set_pixel(x, y+222, pixel)
            patch2 = make_recolored_patch(1, 1, 1)
            pixel2 = patch2.get_pixel(x, y)
            final_image.set_pixel(x+222, y+222, pixel2)
            final_image.set_pixel(x+444, y+222, pixel)

    final_image.show()


def make_recolored_patch(red_scale, green_scale, blue_scale):
    '''
    Implement this function to make a patch for the Warhol Filter.
    It loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixel's red component by
    :param green_scale: A number to multiply each pixel's green component by
    :param blue_scale: A number to multiply each pixel's blue component by
    Returns the newly generated patch.
    '''
    patch = SimpleImage(PATCH_NAME)
    # TODO: your code here
    for pixel in patch:
        pixel.red = pixel.red * red_scale
        pixel.green = pixel.green * green_scale
        pixel.blue = pixel.blue * blue_scale
    return patch


if __name__ == '__main__':
    main()
