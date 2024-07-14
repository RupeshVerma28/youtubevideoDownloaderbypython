import tkinter as tk
import pytube
from tkinter import filedialog, messagebox
from pytube import YouTube

class YouTubeDownloader(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("YouTube Video Downloader")
        self.geometry("400x200")
        self.create_widgets()

    def create_widgets(self):
        # URL Label and Entry
        self.url_label = tk.Label(self, text="YouTube URL:")
        self.url_label.pack(pady=10)
        self.url_entry = tk.Entry(self, width=50)
        self.url_entry.pack(pady=5)

        # Path Label and Button
        self.path_label = tk.Label(self, text="Save Location:")
        self.path_label.pack(pady=10)
        self.path_button = tk.Button(self, text="Browse", command=self.browse_path)
        self.path_button.pack(pady=5)
        self.path_display = tk.Label(self, text="", fg="blue")
        self.path_display.pack(pady=5)

        # Download Button
        self.download_button = tk.Button(self, text="Download", command=self.download_video)
        self.download_button.pack(pady=20)

    def browse_path(self):
        self.download_path = filedialog.askdirectory()
        self.path_display.config(text=self.download_path)

    def download_video(self):
        url = self.url_entry.get()
        path = self.download_path
        if not url:
            messagebox.showerror("Error", "Please enter a YouTube URL")
            return
        if not path:
            messagebox.showerror("Error", "Please select a save location")
            return
        try:
            yt = YouTube(url)
            ys = yt.streams.get_highest_resolution()
            ys.download(path)
            messagebox.showinfo("Success", f"Downloaded: {yt.title}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to download video: {e}")

if __name__ == "__main__":
    app = YouTubeDownloader()
    app.mainloop()
