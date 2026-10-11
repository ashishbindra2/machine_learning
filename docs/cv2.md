# cv installtions

- Update pip
- update steptool
- user numpy version less thrn 2
- or install visuall c++ developer

OpenCV stitcher returns:

- 0 → OK
- 1 → ERR_NEED_MORE_IMGS
- 2 → ERR_HOMOGRAPHY_EST_FAIL
- 3 → ERR_CAMERA_PARAMS_ADJUST_FAIL

# CV2

Save image using cv2

To save an image using OpenCV (cv2) in Python, the cv2.imwrite() function is used.
This function writes an image (represented as a NumPy array) to a specified file.

```py
cv2.imwrite(filename, img, params=None)
```

Parameters:

- filename: A string representing the name and path where the image will be saved. The filename must include the desired image format extension (e.g., .jpg, .png, .bmp).
- img: The image data to be saved, typically a NumPy array (the image object loaded or processed by OpenCV).
- params (Optional): A list of format-specific parameters encoded as pairs. This is used for advanced settings like compression quality for JPEG images
