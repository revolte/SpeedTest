import speedtest
import tkinter as tk
from tkinter import ttk
import threading
import time


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Internet Speed Test')
        self.root.geometry('300x130')
        # self.root.iconbitmap('download.ico')

        self.progressbar = ttk.Progressbar(self.root, orient="horizontal", length=250, mode="indeterminate")
        self.progressbar.pack()
        self.start_button = tk.Button(self.root, text="Start", bg='Green', font=('Arial', 15), command=self.start)
        self.start_button.pack()
        self.download_label = tk.Label(self.root, text="", font=('Arial', 10), fg='Blue')
        self.download_label.pack()

        self.upload_label = tk.Label(self.root, text="", font=('Arial', 10), fg='Green')
        self.upload_label.pack()

        self.ping_label = tk.Label(self.root, text="", fg='Red')
        self.ping_label.pack()
        self.thread1 = None
        self.thread2 = None
        self.progress = 0
        self.running = False

    def start(self):
        self.running = True
        self.thread1 = threading.Thread(target=self.run)
        self.thread1.start()
        self.thread2 = threading.Thread(target=self.internet_speed)
        self.thread2.start()

    def stop(self):
        self.running = False

    def run(self):
        while self.progress < 100000 and self.running:
            self.progress += 1
            time.sleep(0.01)  # simulate doing some work
            self.root.after(10, self.update_progressbar)  # update progress bar from main thread

    def internet_speed(self):
        st = speedtest.Speedtest()
        download_speed = st.download() / 1_000_000
        upload_speed = st.upload() / 1_000_000
        ping_speed = st.results.ping
        self.download_label.config(text=f"Download speed: {download_speed:.2f} Mbps")
        self.upload_label.config(text=f"Upload speed: {upload_speed:.2f} Mbps")
        self.ping_label.config(text=f"Ping: {ping_speed:.2f} ms")
        self.stop()

    def update_progressbar(self):
        self.progressbar["value"] = self.progress

    def start_gui(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = App()
    app.start_gui()
