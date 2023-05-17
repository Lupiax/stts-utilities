# STTS Utilities

This repository contains STTS utilities which I use primarily for VRChat. By using the scripts available in this repository, you can use your own microphone to speak, but the output will be an AI-generated voice instead of your own voice.

# Prerequisites

Before using the STTS utilities, make sure you have the following prerequisites installed and set up:

- VB-Audio CABLE: Install [VB-Audio CABLE](https://vb-audio.com/Cable/), as it is required to forward the audio properly to your games.

- Docker: Install [Docker](https://www.docker.com/products/docker-desktop/), as it is required for the Voicevox engine.

- Python: Ensure you have at least Python 3.10.6 installed. You can download it from the [Python website](https://www.python.org/downloads/release/python-3106/).

- **API Access**: Obtain API access to DeepL and OpenAI. You will need the API keys for these services.

# How to Use

Follow the steps below to use the STTS utilities:

1. If you intend to use the Japanese STTS, install Voicevox by running `start.bat`. If you're not planning to use it, you can skip this step.

2. Install the Python dependencies by running `install_dependencies.bat`.

3. If you're using the Japanese voice, start the Voicevox engine by running `start.bat`. If you're not using it, you can skip this step.

4. Configure your API keys and audio devices by modifying the `.env.sample` file. Save the changes and rename the file to `.env`.

5. Start your preferred STTS script, either the English or Japanese version.

6. To record yourself, press the 'V' key while speaking. Release the key when you're done speaking. The audio will be transcribed, converted into an AI voice, and played through your virtual microphone.

**Note**: In your game settings, make sure to set VB-Audio CABLE as your microphone so that others can hear you.
License

# License

This repository is licensed under the MIT license.

# Contributions

Contributions are always welcome, if you got anything to improve, feel free to make a PR.
