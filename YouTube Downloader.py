import tkinter
import customtkinter
import yt_dlp


def startDownload():
    try:
        ytLink = link.get()  # Get the URL from the input
        ydl_opts = {
            'quiet': False,  # Show detailed logs
            'format': 'best',  # Choose the best available format
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([ytLink])  # Download the video
        print("Download complete!")
    except Exception as e:
        print("The YouTube link is invalid")
        print("Error:", e)


# System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Define app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# Add UI elements
title = customtkinter.CTkLabel(app, text="Insert a YouTube URL")
title.pack(padx=10, pady=10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Download Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

# Run app
app.mainloop()
