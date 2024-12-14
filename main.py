import tkinter as tk
from tkinter import messagebox
import yt_dlp

def download_video():
    url = entry_url.get()
    if not url:
        messagebox.showerror("Error", "Please enter a valid video URL")
        return

    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': '%(title)s.%(ext)s',  
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            messagebox.showinfo("Downloading", f"Downloading video: {url}")
            ydl.download([url])  
        messagebox.showinfo("Success", "The video has been downloaded successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def clear_entry():
    entry_url.delete(0, tk.END)

def close_app():
    root.quit()

root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("400x250") 
root.resizable(False, False)  

label_title = tk.Label(root, text="Enter YouTube Video URL", font=("Arial", 12))
label_title.pack(pady=10)

entry_url = tk.Entry(root, width=50)
entry_url.pack(pady=5)

btn_download = tk.Button(root, text="Download Video", command=download_video, bg="green", fg="white", width=20)
btn_download.pack(pady=10)

btn_clear = tk.Button(root, text="Clear URL", command=clear_entry, bg="orange", fg="white", width=20)
btn_clear.pack(pady=5)

btn_exit = tk.Button(root, text="Exit", command=close_app, bg="red", fg="white", width=20)
btn_exit.pack(pady=5)


root.mainloop()