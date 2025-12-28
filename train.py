from ultralytics import YOLO

# Load a YOLOv8 model (small)
model = YOLO("yolov8s.pt")

# Train the model
model.train(
    data="data.yaml",    # path to dataset YAML
    epochs=50,           # number of training epochs
    imgsz=640,           # image size
    batch=16,            # batch size (adjust based on your GPU)
    project="yolov8_results",  # output folder
    name="pechey_model",   # subfolder for this run
    exist_ok=True
)
