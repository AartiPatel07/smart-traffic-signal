# smart-traffic-signal
Smart traffic controller using YOLOv8 and Streamlit


This project is a real-time AI-based traffic management system. It uses the **YOLOv8 object detection model** to count vehicles from a webcam feed and dynamically adjust the traffic light timer. Built using Python and Streamlit by a 3rd year BTech AIML student.

---

## Main File

**File to run:** `traffic_ui.py`

---

## Features

- Detects vehicles (car, bus, truck, bike)
- Counts vehicles in each direction
- Dynamically calculates green signal timing
- Shows live camera feed, vehicle count, and signal timer using a Streamlit dashboard

---

##  How to Run this Project

### Step 1: Open Command Prompt or Terminal

Go to the folder where your file `traffic_ui.py` is saved.

cd path_to_your_folder

### Step 02 Create virtual Environment 
python -m venv yolov8_env

Activate the environment:
yolov8_env\Scripts\activate  // for windows 
source yolov8_env/bin/activate //for Mac/Linux

### Step 3: Install Required Python Libraries
pip install streamlit opencv-python-headless ultralytics pillow

### Step 4: Run the Streamlit App
Use this command to run 

streamlit run traffic_ui.py

Your default browser will open and show the app at:
http://localhost:8501

Developed By
Aarti Patel
3rd Year BTech Student
Artificial Intelligence & Machine Learning (AIML)
Smart Traffic Management 3rd Year Project
