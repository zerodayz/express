import logging
import random
import time


def test_recaptcha_v2(actions):
    actions.set_user_agent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36")
    actions.go("https://patrickhlauke.github.io/recaptcha/")
    # First try (Directly)
    # actions.switch_to_iframe("css=.g-recaptcha iframe")
    # actions.mouse_click("css=.recaptcha-checkbox-border")
    # actions.wait_for_presence_of_element("class=recaptcha-checkbox-checked")
    # actions.switch_to_default_content()
    # actions.take_screenshot("recaptcha_v2.png")

    # Second try (Keyboard only)
    # actions.keyboard_press("tab")
    # actions.keyboard_press("tab")
    # actions.keyboard_press("enter")

    # Third try (Audio only)
    actions.switch_to_iframe("css=.g-recaptcha iframe")
    actions.mouse_hover("css=.recaptcha-checkbox-border")
    actions.mouse_click("css=.recaptcha-checkbox-border")
    actions.switch_to_default_content()
    actions.switch_to_frame(2)
    time.sleep(random.randint(1, 3))
    actions.mouse_hover("id=recaptcha-audio-button")
    actions.mouse_click("id=recaptcha-audio-button")
    audio = actions.get_href("css=.rc-audiochallenge-tdownload-link")

    # Download audio file
    import requests
    r = requests.get(audio)
    with open("audio.mp3", "wb") as f:
        f.write(r.content)

    # Remove the wav file
    import os
    os.remove("audio.wav")

    # Convert mp3 to wav
    import subprocess
    subprocess.call(["ffmpeg", "-i", "audio.mp3", "audio.wav"])

    text = ""
    import speech_recognition as sr
    r = sr.Recognizer()
    try:
        # Create audio file instance from the original file
        audio_ex = sr.AudioFile("audio.wav")
        type(audio_ex)

        # Create audio data
        with audio_ex as source:
            audio_data = r.record(audio_ex)
        type(audio_data)

        s = r.recognize_google(audio_data)
        text = s
    except Exception as e:
        print("Exception: "+str(e))

    time.sleep(random.randint(1, 3))
    actions.mouse_hover("id=audio-response")
    actions.mouse_click("id=audio-response")
    logging.getLogger().info(f'Recognized text: {text}')

    time.sleep(random.randint(1, 3))
    actions.keyboard_type("id=audio-response", text)

    time.sleep(random.randint(1, 3))
    actions.mouse_hover("id=recaptcha-verify-button")
    actions.mouse_click("id=recaptcha-verify-button")
    time.sleep(5)
    actions.take_screenshot("recaptcha_v2.png")
