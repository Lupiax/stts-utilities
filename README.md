# STTS Utilities

This repository contains STTS utilities which I use for VRChat primarily,
by using the scripts available in this repo you can use your own microphone to speak,
but you will have AI generated voice rather than your own voice as Output.

# Prerequisites

- You must have [VB-Audio CABLE](https://vb-audio.com/Cable/) Installed it is required to forward the audio properly to your games.

- You must have [Docker](https://www.docker.com/products/docker-desktop/) installed, it is required for voicevox engine.

- You should have at least [python 3.10.6](https://www.python.org/downloads/release/python-3106/) installed.

# How to use?


1. If you are planning on using the Japanese STTS, install voicevox through `start.bat`, if you are not going to use skip this step.

2. Now we must install our python dependencies we can do that by running `install_dependencies.bat`

3. Now if you are going to use the Japanese voice, start voicevox engine from `start.bat`, if you are not going to use it, skip this step.

5. Next you should configure your API keys and audio devices by modifying `.env.sample` and renaming it to `.env` afterwards.

4. Now start your preferred STTS script, English or Japanese.

5. Now you can record yourself by talking `V` after you let it go it will transcribe the Audio and turn it into AI voice and play it through your virtual microphone.

# Notes

- You must set the VB-Audio CABLE as your microphone in games so people can hear you.

# License

This repository is licensed under the MIT license.