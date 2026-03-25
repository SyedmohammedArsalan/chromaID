import cv2
import numpy as np
from sklearn.cluster import KMeans

def get_dominant_color(image_bytes: bytes) -> np.ndarray:
    """Extracts the dominant color from the center of the image."""
    # 1. Convert the uploaded bytes into an OpenCV image array
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Convert BGR (OpenCV default) to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # 2. Crop the center of the image (assuming the user's face is in the middle)
    h, w, _ = img.shape
    center_crop = img[h//3 : 2*h//3, w//3 : 2*w//3]
    
    # 3. Reshape the image data to a list of pixels
    pixels = center_crop.reshape(-1, 3)
    
    # 4. Use K-Means to find the 1 most dominant color in that cropped area
    kmeans = KMeans(n_clusters=1, n_init=10, random_state=42)
    kmeans.fit(pixels)
    
    dominant_color = kmeans.cluster_centers_[0]
    return dominant_color

def determine_season(image_bytes: bytes) -> str:
    """Analyzes the image and returns a seasonal color palette."""
    dominant_rgb = get_dominant_color(image_bytes)
    
    # Convert RGB to a format OpenCV can translate to HSV
    rgb_pixel = np.uint8([[dominant_rgb]])
    hsv_pixel = cv2.cvtColor(rgb_pixel, cv2.COLOR_RGB2HSV)[0][0]
    
    hue, sat, val = hsv_pixel
    
    # --- Basic ML Decision Tree for Seasons ---
    # Hue determines Warm vs Cool. Value determines Dark vs Light.
    
    # If the color is very dark (Low Value) and Warm (Hue in the orange/yellow range)
    if val < 150 and (hue < 30 or hue > 160):
        return "Dark Autumn"
    # Fallback/Example logic for other seasons
    elif val > 150 and (hue < 30 or hue > 160):
        return "Spring"
    elif val < 150 and (30 <= hue <= 160):
        return "Winter"
    else:
        return "Summer"