# AI Video Generation Project 

A simple AI-powered video generation project that automatically creates a short narrated video about a given topic.

For this project, the script generates a short video tribute to **Bhagat Singh** by:

* Generating a narration using **Google Gemini**
* Generating relevant images using **Pollinations AI**
* Converting the narration into speech using **gTTS**
* Combining images, audio, and subtitles into a final video using **MoviePy**

## Features

* AI-generated narration
* Automatic image generation
* Text-to-speech voiceover
* Automatic video creation
* Subtitle overlay
* Fully automated pipeline

## Tech Stack

* Python
* Google Gemini API
* Pollinations AI
* gTTS (Google Text-to-Speech)
* MoviePy
* Requests

## Project Workflow

1. Generate narration using Gemini API
2. Generate images based on predefined prompts
3. Convert narration into audio using gTTS
4. Create video scenes from generated images
5. Add subtitles and voiceover
6. Export final video as MP4

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/video-generation-project.git
cd video-generation-project
```

Install dependencies:

```bash
pip install google-generativeai gtts moviepy pillow requests numpy
```

## Configuration

Add your Gemini API key inside the script:

```python
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

## Run the Project

```bash
python python2.py
```

## Output

The project generates:

* `scene_0.jpg` to `scene_4.jpg`
* `narration.mp3`
* `bhagat_singh_intro.mp4`

## Sample Screenshots

### Generated Images

(Add screenshots here)

### Video Frames

(Add screenshots here)

### Final Output Video

(Add GIF or video preview here)

## Future Improvements

* Dynamic topic selection
* Better subtitle synchronization
* Background music support
* Image transitions and effects
* Multiple voice options
* Web interface using Streamlit

## Project Structure

```text
.
├── python2.py
├── requirements.txt
├── README.md
├── scene_0.jpg
├── scene_1.jpg
├── scene_2.jpg
├── scene_3.jpg
├── scene_4.jpg
├── narration.mp3
└── bhagat_singh_intro.mp4
```

## Disclaimer

This project is built for learning purposes to demonstrate how multiple AI services can be combined to automate video creation using Python.
