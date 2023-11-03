import tkinter as tk
import pyshorteners
import tkinter.messagebox
import pyperclip  # This library is needed for clipboard operations


def shorten_url():
    long_url = entry.get()
    type_bitly = pyshorteners.Shortener(api_key='adc8bf63a6643f1a40d8e046ef419cd658f98f97')
    short_url = type_bitly.bitly.short(long_url)

    # Copy the shortened URL to the clipboard
    pyperclip.copy(short_url)

    # Show a message box
    message = f'Short URL is: {short_url}\n\nLink copied to clipboard!'
    tkinter.messagebox.showinfo("URL Shortened", message)


# Create the main window
window = tk.Tk()
window.title("URL Shortener")

# Create a label
label = tk.Label(window, text="Enter the URL:")
label.pack()

# Create an entry widget for input
entry = tk.Entry(window)
entry.pack()

# Create a button to trigger URL shortening
shorten_button = tk.Button(window, text="Shorten URL", command=shorten_url)
shorten_button.pack()

# Start the GUI main loop
window.mainloop()
