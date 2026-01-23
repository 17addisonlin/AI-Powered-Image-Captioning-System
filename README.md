<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![project_license][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/17addisonlin/AI-Powered-Image-Captioning-System">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">AI-Powered-Image-Captioning-System</h3>

  <p align="center">
    An AI-powered web app that generates image descriptions and social-ready captions from uploaded images.
    <br />
    <a href="https://github.com/17addisonlin/AI-Powered-Image-Captioning-System"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/17addisonlin/AI-Powered-Image-Captioning-System">View Demo</a>
    &middot;
    <a href="https://github.com/17addisonlin/AI-Powered-Image-Captioning-System/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/17addisonlin/AI-Powered-Image-Captioning-System/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://github.com/17addisonlin/AI-Powered-Image-Captioning-System)

AI-Powered-Image-Captioning-System lets users upload an image and receive a caption describing the scene. It also includes a Social mode for generating a short, shareable caption with optional tone, emojis, and hashtags.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [FastAPI](https://fastapi.tiangolo.com/)
* [Transformers](https://huggingface.co/docs/transformers/index)
* [PyTorch](https://pytorch.org/)
* [Pillow](https://python-pillow.org/)
* HTML/CSS/JavaScript

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these steps.

### Prerequisites

* Python 3.11 (recommended)
* Conda or venv

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/17addisonlin/AI-Powered-Image-Captioning-System.git
   cd AI-Powered-Image-Captioning-System
   ```
2. Create and activate an environment
   ```sh
   conda create -n captioning python=3.11 -y
   conda activate captioning
   ```
3. Install dependencies
   ```sh
   pip install -r requirements.txt
   ```
4. Run the server
   ```sh
   uvicorn backend.main:app --reload
   ```
5. Open `http://127.0.0.1:8000`

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

- Upload an image to generate a caption.
- Switch to Social mode to generate a social caption with optional tone, emojis, and hashtags.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [ ] Enhance UI
- [ ] Add features
- [ ] Add dark/white toggle background

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Addison Lin  
LinkedIn: https://www.linkedin.com/in/addison-lin-227

Project Link: https://github.com/17addisonlin/AI-Powered-Image-Captioning-System

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/17addisonlin/AI-Powered-Image-Captioning-System.svg?style=for-the-badge
[contributors-url]: https://github.com/17addisonlin/AI-Powered-Image-Captioning-System/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/17addisonlin/AI-Powered-Image-Captioning-System.svg?style=for-the-badge
[forks-url]: https://github.com/17addisonlin/AI-Powered-Image-Captioning-System/network/members
[stars-shield]: https://img.shields.io/github/stars/17addisonlin/AI-Powered-Image-Captioning-System.svg?style=for-the-badge
[stars-url]: https://github.com/17addisonlin/AI-Powered-Image-Captioning-System/stargazers
[issues-shield]: https://img.shields.io/github/issues/17addisonlin/AI-Powered-Image-Captioning-System.svg?style=for-the-badge
[issues-url]: https://github.com/17addisonlin/AI-Powered-Image-Captioning-System/issues
[license-shield]: https://img.shields.io/github/license/17addisonlin/AI-Powered-Image-Captioning-System.svg?style=for-the-badge
[license-url]: https://github.com/17addisonlin/AI-Powered-Image-Captioning-System/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/addison-lin-227
[product-screenshot]: images/screenshot.png
