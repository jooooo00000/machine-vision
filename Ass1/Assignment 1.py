import cv2
import matplotlib.pyplot as plt
import numpy as np

# === 1. Create canvas and draw rectangles ===
canvas = np.ones((500, 500, 3), dtype=np.uint8) * 255

# Draw 3 rectangles
cv2.rectangle(canvas, (100, 100), (150, 200), (255, 0, 0), 2)   # Blue
cv2.rectangle(canvas, (200, 200), (300, 300), (0, 255, 0), 2)   # Green
cv2.rectangle(canvas, (250, 320), (400, 400), (0, 0, 255), 2)   # Red

# Show the canvas with rectangles using Matplotlib
plt.figure(figsize=(5, 5))
plt.imshow(cv2.cvtColor(canvas, cv2.COLOR_BGR2RGB))
plt.title("Rectangles")
plt.axis('off')
plt.show()

# === 2. Capture ID photo from webcam ===
cap = cv2.VideoCapture(0)
print("D:\youssef\study\Semester (10)\Machine vision\lec3\WhatsApp Image 2025-04-05 at 10.51.42_c860368c.jpg")
while True:
    ret, frame = cap.read()
    cv2.imshow("Camera - Press SPACE to Capture", frame)
    key = cv2.waitKey(1)
    if key == 32:  # Spacebar
        id_photo = frame.copy()
        break
    elif key == 27:  # ESC to exit
        cap.release()
        cv2.destroyAllWindows()
        exit("❌ Capture canceled.")
cap.release()
cv2.destroyAllWindows()

# Resize for consistency
id_photo = cv2.resize(id_photo, (500, 300))

# === 3. Add name, line and corner circles ===
name = "Youssef Samy"
cv2.putText(id_photo, name, (20, 260), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
cv2.line(id_photo, (20, 270), (250, 270), (0, 0, 0), 2)

# Draw red circles at corners
corners = [(0, 0), (499, 0), (0, 299), (499, 299)]
for corner in corners:
    cv2.circle(id_photo, corner, 10, (0, 0, 255), -1)

# === 4. Show 4 subplots with different transparency ===
id_rgba = cv2.cvtColor(id_photo, cv2.COLOR_BGR2RGBA)  # Add alpha channel

fig, axs = plt.subplots(1, 4, figsize=(16, 4))
alphas = [1.0, 0.75, 0.5, 0.25]

for i in range(4):
    img = id_rgba.copy()
    img[:, :, 3] = int(255 * alphas[i])  # Set transparency
    axs[i].imshow(img)
    axs[i].set_title(f'Alpha = {alphas[i]}')
    axs[i].axis('off')

plt.tight_layout()
plt.show()
