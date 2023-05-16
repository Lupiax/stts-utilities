import pyaudio

def main():
    print("Above you can see all of your audio devices:")
    print("")
    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
        print(p.get_device_info_by_index(i).get('name'))

if __name__ == "__main__":
    main()