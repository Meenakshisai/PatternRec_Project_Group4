import gradio as gr
import torch
from torchvision import models, transforms
from PIL import Image
import torch.nn as nn

device = "cuda" if torch.cuda.is_available() else "cpu"

produce_model = models.resnet18(weights=None)
produce_model.fc = nn.Linear(produce_model.fc.in_features, 2)
produce_model.load_state_dict(torch.load("produce_classifier.pth", map_location=device))
produce_model.eval().to(device)

variation_model = models.resnet18(weights=None)
variation_model.fc = nn.Linear(variation_model.fc.in_features, 6)
variation_model.load_state_dict(
    torch.load("variation_classifier.pth", map_location=device)
)
variation_model.eval().to(device)

produce_classes = ["blackberry", "lime"]
variation_classes = [
    "Halved",
    "In Context",
    "In a Container",
    "Single Berry",
    "Small Group",
    "Whole",
]

transform = transforms.Compose(
    [
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
    ]
)


def classify(image):
    image = Image.fromarray(image).convert("RGB")
    img_tensor = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        pred1 = produce_model(img_tensor)
        pred2 = variation_model(img_tensor)

    prod_label = produce_classes[torch.argmax(pred1).item()]
    var_label = variation_classes[torch.argmax(pred2).item()]
    return f"Produce: {prod_label}", f"Variation: {var_label}"


demo = gr.Interface(
    fn=classify,
    inputs=gr.Image(type="numpy"),
    outputs=["text", "text"],
    title="Blackberry & Lime Classifier",
    description="Upload a produce image to get predictions for type and variation.",
)

demo.launch()
