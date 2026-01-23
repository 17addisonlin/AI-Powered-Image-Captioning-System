# AI-Powered-Image-Captioning-System

An AI-powered web app that generates image descriptions and social-ready captions from uploaded images. Built with FastAPI and modern vision-language models.

![Screenshot][product-screenshot]

## Built With

- FastAPI
- Transformers (Hugging Face)
- PyTorch
- Pillow
- HTML/CSS/JavaScript

## Getting Started

### Prerequisites

- Python 3.11 (recommended)
- Conda or venv

### Installation

1) Clone the repo
```bash
git clone https://github.com/17addisonlin/AI-Powered-Image-Captioning-System.git
cd AI-Powered-Image-Captioning-System
```

2) Create and activate an environment
```bash
conda create -n captioning python=3.11 -y
conda activate captioning
```

3) Install dependencies
```bash
pip install -r requirements.txt
```

4) Run the server
```bash
uvicorn backend.main:app --reload
```

5) Open `http://127.0.0.1:8000`

## Usage

- Upload an image to generate a caption.
- Switch to Social mode to generate a social caption with optional tone, emojis, and hashtags.

## Roadmap

- [ ] Enhance UI
- [ ] Add features
- [ ] Add dark/white toggle background

## License

MIT License. See `LICENSE`.

## Contact

Addison Lin  
LinkedIn: https://www.linkedin.com/in/addison-lin-227

## Links

- Repo: https://github.com/17addisonlin/AI-Powered-Image-Captioning-System

[product-screenshot]: images/screenshot.png
