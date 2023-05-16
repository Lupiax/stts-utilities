from dotenv import load_dotenv
import os
import sounddevice as sd
import soundfile as sf
import keyboard
import threading
import numpy as np
import time
import openai
import deepl

from fairseq.checkpoint_utils import load_model_ensemble_and_task_from_hf_hub
from fairseq.models.text_to_speech.hub_interface import TTSHubInterface

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')
translator = deepl.Translator(os.getenv('DEEPL_API_KEY'))
input_device = os.getenv('AUDIO_INPUT_DEVICE')
sd.default.device = os.getenv('AUDIO_OUTPUT_DEVICE')
temp_dir = os.getenv('TEMPORARY_DIRECTORY')

# TODO: use some other voice model.
models, cfg, task = load_model_ensemble_and_task_from_hf_hub(
    "facebook/fastspeech2-en-ljspeech",
    arg_overrides={"vocoder": "hifigan", "fp16": False}
)

model = models[0]
TTSHubInterface.update_cfg_with_data_cfg(cfg, task.data_cfg)
generator = task.build_generator([model], cfg)

def record_audio():
    print('[Audio] started recording.')

    sample_rate = 44100
    samples = []

    def callback(data, frames_count, time, status):
        samples.extend(np.copy(data))

    stream = sd.InputStream(callback=callback, channels=1, samplerate=sample_rate, device=input_device)
    stream.start()

    global recording
    while recording:
        time.sleep(0.1) # Let's prevent the application from eating up our CPU usage.

    stream.stop()
    print('[Audio] stopped recording.')
    sf.write(temp_dir + 'recorded_voice.wav', samples, sample_rate)

    threading.Thread(target=transcribe_speech).start()

def transcribe_speech():
    print('[Transcribe] transcribing recording.')
    file = open(temp_dir + "recorded_voice.wav", "rb")
    transcript = openai.Audio.translate("whisper-1", file)
    print('[Transcribe] transcribed recording.')
    threading.Thread(target=generate_audio, args=(transcript.text,)).start()

def generate_audio(transcript):
    print('[Audio] generating AI voice.')
    sample = TTSHubInterface.get_model_input(task, transcript)
    wav, rate = TTSHubInterface.get_prediction(task, model, generator, sample)
    sf.write(temp_dir + 'ai_voice.wav', wav, rate)
    print('[Audio] generated AI voice.')
    threading.Thread(target=play_audio).start()

def play_audio():
    data, sample_rate = sf.read(temp_dir + 'ai_voice.wav', dtype='float32')
    print('[Audio] playing AI voice.')
    sd.play(data, sample_rate)
    sd.wait()
    print('[Audio] played AI voice.')

def main():
    global recording
    recording = False

    def start_recording():
        global recording
        if not recording:
            recording = True
            threading.Thread(target=record_audio).start()

    def stop_recording():
        global recording
        if recording:
            recording = False

    keyboard.on_press_key('v', lambda event: start_recording())
    keyboard.on_release_key('v', lambda event: stop_recording())

    print("SpeechToText/TextToSpeech utility by Lupiax")
    print("==========================================================")
    print(f"Audio Input: {os.getenv('AUDIO_INPUT_DEVICE')}")
    print(f"Audio Output: {os.getenv('AUDIO_OUTPUT_DEVICE')}")
    print("==========================================================")
    print("Press and hold the 'V' key to start recording audio.")
    print("Release the 'V' key to stop recording and play AI voice.")

    keyboard.wait()

if __name__ == "__main__":
    main()
