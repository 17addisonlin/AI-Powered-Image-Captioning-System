from transformers import GitProcessor, GitForCausalLM
from PIL import Image
import torch

class ImageCaptioner:
    def __init__(self, device: str = None):
        # Set device to GPU if available, otherwise CPU
        if device is None:
            device = "cuda" if torch.cuda.is_available() else "cpu"
        
        self.device = device
        
        # Initialize GIT model and processor
        self.processor = GitProcessor.from_pretrained("microsoft/git-base-coco")
        self.model = GitForCausalLM.from_pretrained("microsoft/git-base-coco").to(self.device)

    def caption(self, image: Image.Image, max_new_tokens: int = 30) -> str:
        # Process the image into the format expected by the model
        inputs = self.processor(images=image, return_tensors="pt").to(self.device)

        # Generate caption using the model
        with torch.no_grad():
            output_ids = self.model.generate(**inputs, max_new_tokens=max_new_tokens)

        # Decode and return the generated caption
        caption = self.processor.batch_decode(output_ids, skip_special_tokens=True)[0]
        return caption
