# Requirements: google-generativeai gtts moviepy pillow requests numpy
# command : pip install google-generativeai gtts moviepy pillow requests numpy



import requests
import time
from gtts import gTTS
from moviepy import (
    ImageClip,
    AudioFileClip,
    TextClip,
    CompositeVideoClip,
    concatenate_videoclips
)




GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"  

FPS = 24


# SCRIPT GENERATION

def generate_narration():

    try:
        url = (
            "https://generativelanguage.googleapis.com/"
            f"v1beta/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"
        )

        prompt = """
        Write a 25-word emotional narration about Bhagat Singh.
        Mention:
        - Indian freedom fighter
        - hanged at age 23
        - sacrifice for freedom
        - inspiring ending

        Return narration only.
        """

        body = {
            "contents": [
                {
                    "parts": [
                        {"text": prompt}
                    ]
                }
            ]
        }

        response = requests.post(url, json=body)

        data = response.json()

        return data["candidates"][0]["content"]["parts"][0]["text"]

    except Exception:
        return (
            "Bhagat Singh was one of India's bravest freedom fighters. "
            "At just 23 years old, he gave his life fighting British rule. "
            "His sacrifice inspired generations and continues to remind us "
            "that courage can change the course of history."
        )


# IMAGE GENERATION


def generate_images():

    prompts = [
        "young Bhagat Singh portrait cinematic lighting ultra realistic",
        "Bhagat Singh reading revolutionary books historical India cinematic",
        "Indian freedom movement protest dramatic historical scene",
        "Bhagat Singh with Indian flag emotional patriotic artwork",
        "tribute to Bhagat Singh freedom sacrifice masterpiece"
    ]

    files = []

    for i, prompt in enumerate(prompts):

        print(f"Generating image {i+1}")

        url = f"https://image.pollinations.ai/prompt/{prompt}"

        img = requests.get(url).content

        filename = f"scene_{i}.jpg"

        with open(filename, "wb") as f:
            f.write(img)

        files.append(filename)

        time.sleep(2)

    return files


# AUDIO


def generate_audio(script):

    tts = gTTS(text=script)

    tts.save("narration.mp3")

    return "narration.mp3"


# VIDEO


def create_video(images, audio_path, narration):

    audio = AudioFileClip(audio_path)
    VIDEO_DURATION = audio.duration

    duration_per_scene = VIDEO_DURATION / len(images)

    clips = []

    for image in images:

        image_clip = (
            ImageClip(image)
            .resized(new_size=(1280,720))
            .with_duration(duration_per_scene)
        )

        subtitle = (
            TextClip(
                text="Bhagat Singh - Freedom Fighter",
                font_size=50,
                color="white",
                stroke_color="black",
                stroke_width=2,
                size=(1200, None),
                method="caption"
            )
            .with_position(("center", 620))
            .with_duration(duration_per_scene)
        )

        final_scene = CompositeVideoClip(
            [image_clip, subtitle],
            size=(1280, 720)
        )

        clips.append(final_scene)

    video = concatenate_videoclips(clips)

    final_video = video.with_audio(audio)

    final_video.write_videofile(
        "bhagat_singh_intro.mp4",
        fps=FPS,
        codec="libx264",
        audio_codec="aac"
    )


# MAIN


if __name__ == "__main__":

    print("Generating narration...")
    narration = generate_narration()

    print("\nNarration:")
    print(narration)

    print("\nGenerating images...")
    images = generate_images()

    print("\nGenerating voice...")
    audio = generate_audio(narration)

    print("\nCreating video...")
    create_video(images, audio, narration)

    print("\nDone!")
    print("Saved as bhagat_singh_intro.mp4")
    
    from moviepy import AudioFileClip

    audio = AudioFileClip("narration.mp3")
    print(audio.duration)