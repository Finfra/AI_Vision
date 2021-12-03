from __future__ import print_function, division

import numpy as np
from skimage import data
import cv2

import imgaug as ia
from imgaug import augmenters as iaa

TIME_PER_STEP = 5000
NB_AUGS_PER_IMAGE = 10


def main():
    image = data.astronaut()
    image = ia.imresize_single_image(image, (64, 64))
    print("image shape:", image.shape)
    print("Press any key or wait %d ms to proceed to the next image." % (TIME_PER_STEP,))

    k = [
        1,
        2,
        4,
        8,
        16,
        (8, 8),
        (1, 8),
        ((1, 1), (8, 8)),
        ((1, 16), (1, 16)),
        ((1, 16), 1)
    ]

    cv2.namedWindow("aug", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("aug", 64*NB_AUGS_PER_IMAGE, 64)

    for ki in k:
        aug = iaa.AverageBlur(k=ki)
        img_aug = [aug.augment_image(image) for _ in range(NB_AUGS_PER_IMAGE)]
        img_aug = np.hstack(img_aug)
        print("dtype", img_aug.dtype, "averages", np.average(img_aug, axis=tuple(range(0, img_aug.ndim-1))))

        title = "k=%s" % (str(ki),)
        img_aug = ia.draw_text(img_aug, x=5, y=5, text=title)

        cv2.imshow("aug", img_aug[..., ::-1])  # here with rgb2bgr
        cv2.waitKey(TIME_PER_STEP)


if __name__ == "__main__":
    main()
