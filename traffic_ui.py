# import cv2
# import time
# from ultralytics import YOLO

# # Load YOLOv8 model
# model = YOLO("yolov8n.pt")

# # Define vehicle classes to count
# vehicle_classes = ['car', 'bus', 'truck', 'motorbike']

# # 4 directions with video sources (replace with your actual sources)
# directions = {
#     "North": 0,
#     "East": 1,
#     "South": 2,
#     "West": 3
# }

# # Timer calculation function based on vehicle count
# def calculate_signal_time(vehicle_count, min_time=10, max_time=60):
#     # You can adjust the logic/formula here as per real need
#     return min(max(min_time, vehicle_count * 2), max_time)

# # Function to process one direction at a time
# def process_direction(direction_name, source):
#     cap = cv2.VideoCapture(source)
#     print(f"\n Now processing {direction_name} traffic...")

#     time.sleep(1)  # Little pause to allow camera to warm up

#     ret, frame = cap.read()
#     if not ret:
#         print(f"[ERROR] Couldn't read from {direction_name} camera")
#         return

#     # YOLO detection
#     results = model(frame)[0]

#     # Count vehicles
#     vehicle_count = 0
#     for cls in results.boxes.cls:
#         if model.names[int(cls)] in vehicle_classes:
#             vehicle_count += 1

#     # Calculate signal time
#     green_time = calculate_signal_time(vehicle_count)
#     print(f"{direction_name} vehicles: {vehicle_count} | Green signal: {green_time} sec")

#     # Show result
#     annotated_frame = results.plot()
#     cv2.putText(annotated_frame, f'{direction_name} Vehicles: {vehicle_count}', (10, 30),
#                 cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#     cv2.putText(annotated_frame, f'Green Signal: {green_time} sec', (10, 70),
#                 cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 200, 200), 2)
    
#     cv2.imshow(f"{direction_name} View", annotated_frame)
#     cv2.waitKey(3000)  # Show for 3 seconds
#     cap.release()
#     cv2.destroyAllWindows()

#     # Simulate green signal time
#     for i in range(green_time, 0, -1):
#         print(f"[{direction_name}] GREEN for {i} sec", end='\r')
#         time.sleep(1)

# Main loop
# while True:
#     for direction, cam_source in directions.items():
#         process_direction(direction, cam_source)

#     print("\n One full cycle complete. Repeating...\n")
# import cv2
# import time
# import streamlit as st
# from ultralytics import YOLO
# from PIL import Image

# # Load YOLOv8 model
# model = YOLO("yolov8n.pt")
# vehicle_classes = ['car', 'bus', 'truck', 'motorbike']

# # Streamlit page config
# st.set_page_config(page_title="Smart Traffic Signal", layout="wide")
# st.title(" Smart Traffic Signal Controller with YOLOv8")
# st.markdown("---")

# # Video sources for directions
# directions = {
#     "North": 0,
#     "East": 1,
#     "South": 2,
#     "West": 3
# }

# # Function to calculate signal time
# def calculate_signal_time(vehicle_count, min_time=10, max_time=60):
#     return min(max(min_time, vehicle_count * 2), max_time)

# # Placeholder for each direction
# placeholders = {}
# for direction in directions:
#     col = st.columns(2)[0]
#     with st.container():
#         st.subheader(f"Direction: {direction}")
#         placeholders[direction] = {
#             "image": st.empty(),
#             "count": st.empty(),
#             "timer": st.empty()
#         }

# # Process each direction
# def process_direction(direction, source):
#     cap = cv2.VideoCapture(source)
#     time.sleep(1)
#     ret, frame = cap.read()
#     cap.release()

#     if not ret:
#         placeholders[direction]["count"].error(" Camera read error.")
#         return

#     results = model(frame)[0]
#     vehicle_count = sum(1 for cls in results.boxes.cls if model.names[int(cls)] in vehicle_classes)
#     green_time = calculate_signal_time(vehicle_count)

#     # Annotated frame
#     annotated_frame = results.plot()
#     annotated_pil = Image.fromarray(annotated_frame)

#     # Update UI
#     placeholders[direction]["image"].image(annotated_pil, caption=f"{direction} Camera View")
#     placeholders[direction]["count"].success(f" Vehicles Detected: {vehicle_count}")
#     placeholders[direction]["timer"].info(f" Green Signal for {green_time} seconds")

#     # Simulate signal timer
#     for i in range(green_time, 0, -1):
#         placeholders[direction]["timer"].info(f" Green Signal for {i} seconds")
#         time.sleep(1)

# # Main loop
# for direction, cam_source in directions.items():
#     process_direction(direction, cam_source)

# st.success(" All directions processed. Cycle complete.")
import cv2
import time
import streamlit as st
from ultralytics import YOLO
from PIL import Image

# Load YOLOv8 model
model = YOLO("yolov8n.pt")
vehicle_classes = ['car', 'bus', 'truck', 'motorbike']

# Streamlit config
st.set_page_config(page_title="Smart Traffic Signal", layout="wide")
st.title("🚦 Smart Traffic Signal Controller with YOLOv8")
st.markdown("---")

# Directions with camera index (change to same if you have only one camera)
directions = {
    "North": 0,
    "East": 0,
    "South": 0,
    "West": 0
}

# Signal timing logic
def calculate_signal_time(vehicle_count, min_time=5, max_time=50):
    return min(max(min_time, vehicle_count * 2), max_time)

# UI placeholders
placeholders = {}
for direction in directions:
    with st.container():
        st.subheader(f"Direction: {direction}")
        placeholders[direction] = {
            "image": st.empty(),
            "count": st.empty(),
            "timer": st.empty()
        }

# Function to process a direction
def process_direction(direction, cam_source):
    cap = cv2.VideoCapture(cam_source)
    time.sleep(1)  # allow camera to warm up
    ret, frame = cap.read()
    cap.release()

    if not ret:
        placeholders[direction]["count"].error(" Camera read error.")
        return

    results = model(frame)[0]
    vehicle_count = sum(1 for cls in results.boxes.cls if model.names[int(cls)] in vehicle_classes)
    green_time = calculate_signal_time(vehicle_count)

    annotated_frame = results.plot()
    annotated_pil = Image.fromarray(annotated_frame)

    # Update UI
    placeholders[direction]["image"].image(annotated_pil, caption=f"{direction} Camera View")
    placeholders[direction]["count"].success(f"Vehicles Detected: {vehicle_count}")
    
    # Green signal timer countdown
    for i in range(green_time, 0, -1):
        placeholders[direction]["timer"].info(f" Green Signal for {i} seconds")
        time.sleep(1)

    placeholders[direction]["timer"].info(" Red Signal")

#  Main Loop (Auto Refresh via Streamlit)
while True:
    for direction, cam_source in directions.items():
        process_direction(direction, cam_source)
    st.rerun()  # Streamlit auto-refresh to repeat cycle

