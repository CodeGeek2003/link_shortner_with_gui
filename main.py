import tkinter as tk
import pyshorteners
import tkinter.messagebox
import pyperclip
def shorten_url():
    long_url = entry.get()
    type_bitly = pyshorteners.Shortener(api_key='adc8bf63a6643f1a40d8e046ef419cd658f98f97')
    short_url = type_bitly.bitly.short(long_url)
    pyperclip.copy(short_url)
    message = f'Short URL is: {short_url}\n\nLink copied to clipboard!'
    tkinter.messagebox.showinfo("URL Shortened", message)
window = tk.Tk()
window.title("URL Shortener")
label = tk.Label(window, text="Enter the URL:")
label.pack()
entry = tk.Entry(window)
entry.pack()
shorten_button = tk.Button(window, text="Shorten URL", command=shorten_url)
shorten_button.pack()
window.mainloop()
