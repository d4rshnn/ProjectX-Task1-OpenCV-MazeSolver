import cv2

image = cv2.imread("X task 1 Windows/mazes/maze_01.png")

print("Image loaded successfully:", image is not None)

print("Shape:", image.shape)    

print("Top-left pixel value:", image[0, 0])

print("Center pixel value:", image[400, 400])

print("Pixel at 100,100:", image[100,100])
print("Pixel at 200,200:", image[200,200])
print("Pixel at 300,300:", image[300,300])
print("Pixel at 50,50:", image[50,50])
print("Pixel at 51,51:", image[51,51])
print("Pixel at 52,52:", image[52,52])
print("Pixel at 53,53:", image[53,53])