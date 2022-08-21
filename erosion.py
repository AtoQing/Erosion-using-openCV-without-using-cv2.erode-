import cv2
import numpy as np

def erosion():

    img = cv2.imread("image.jpg")
    cv2.imshow("Original image", img)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (thresh, binary) = cv2.threshold(gray, 177, 255, cv2.THRESH_BINARY)

    kernel = np.ones((7, 7))

    image_shape = binary.shape
    kernel_shape = kernel.shape

    binary = binary / 255

    output_row = image_shape[0] + kernel_shape[0] - 1
    output_column = image_shape[1] + kernel_shape[1] - 1
    output_image = np.zeros((output_row, output_column))

    # padding image
    for i in range(image_shape[0]):
        for j in range(image_shape[1]):
            output_image[i + int((kernel_shape[0] - 1) / 2), j + int((kernel_shape[1] - 1) / 2)] = binary[i, j]

    for i in range(image_shape[0]):
        for j in range(image_shape[1]):
            window = output_image[i:i + kernel_shape[0], j:j + kernel_shape[1]]
            result = (window == kernel)
            new_value = np.all(result == True)

            if new_value:
                binary[i, j] = 1
            else:
                binary[i, j] = 0

    cv2.imshow("Erosion", binary)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

erosion()
