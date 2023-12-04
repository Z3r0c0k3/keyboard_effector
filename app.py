# python 3.11
import os
import random
import tkinter as tk
from tkinter import filedialog
from playsound import playsound
import threading
import keyboard

class AudioPlayerApp:
    def __init__(self, root):
        self.root = root
        root.title("Random Audio Player")

        self.label = tk.Label(root, text="Select an audio folder")
        self.label.pack()

        self.select_folder_button = tk.Button(root, text="Select Folder", command=self.select_folder)
        self.select_folder_button.pack()

        self.play_audio_button = tk.Button(root, text="Play Random Audio", command=self.play_random_audio, state=tk.DISABLED)
        self.play_audio_button.pack()

        self.audio_folder = ""

    def select_folder(self):
        self.audio_folder = filedialog.askdirectory()
        if self.audio_folder:
            self.play_audio_button['state'] = tk.NORMAL
            self.label.config(text=f"Selected Folder: {self.audio_folder}")

    def play_random_audio(self):
        if self.audio_folder:
            audio_files = [f for f in os.listdir(self.audio_folder) if f.endswith('.mp3')]
            if audio_files:
                audio_file = random.choice(audio_files)
                threading.Thread(target=playsound, args=(os.path.join(self.audio_folder, audio_file),), daemon=True).start()

# GUI 생성
root = tk.Tk()
app = AudioPlayerApp(root)

# 키보드 이벤트 설정
def on_space_key():
    if app.audio_folder:
        app.play_random_audio()

keyboard.add_hotkey('space', on_space_key)

# GUI 실행
root.mainloop()
