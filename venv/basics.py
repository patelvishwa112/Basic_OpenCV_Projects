
import cv2


img = cv2.imread("Path to picture", 1)

print(img.shape)

#reshape_img = cv2.resize(img, (650, 500))

#This line is for dividing original photo into half picture

reshape_img = cv2.resize(img, (int(img.shape[1]/2), int (img.shape[0]/2)))

cv2.imshow("Buildings", reshape_img)
cv2.waitKey(0)

cv2.destroyAllWindows()

