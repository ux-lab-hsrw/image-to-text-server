from ultralytics import YOLO

model = None
confidence_threshold = None

def init(conf_threshold=0.4):
    global model, confidence_threshold
    model = YOLO("yolov8n.pt")
    confidence_threshold = conf_threshold

def handle_image(image):
    if model is None:
        raise Exception("the model is not initialized")
    
    results = model(image)#,conf=confidence_threshold)

    if len(results) == 0:
        return
    
    output = []
    for box in results[0].boxes:
        if round(box.conf[0].item(), 2) >= confidence_threshold:
            output.append(results[0].names[box.cls[0].item()])
   
    return output