# Import necessary modules
from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

# Function to handle video download from YouTube
def download_video(url, save_path):
    """
    Download a YouTube video to the specified folder.

    Parameters:
    - url (str): The URL of the YouTube video.
    - save_path (str): The path where the video will be saved.
    
    Returns:
    - None
    """
    try:
        yt = YouTube(url)  # Create a YouTube object with the provided URL

        # Filter for progressive streams (with both video and audio) and .mp4 format
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()  # Get the highest resolution available

        # Check if the stream exists, then download
        if highest_res_stream:
            highest_res_stream.download(output_path=save_path)
            print("Video downloaded successfully!")
        else:
            print("No valid stream found.")

    # Handle any exceptions that occur during the download
    except Exception as e:
        print(f"Error: {e}")

# Function to open the file dialog to select the download location
def open_file_dialog():
    """
    Open a file dialog to allow the user to select a folder.

    Returns:
    - str: The path to the selected folder or None if no folder is selected.
    """
    folder = filedialog.askdirectory()  # Open the directory selection dialog
    if folder:
        print(f"Selected folder: {folder}")  # Print the selected folder
        return folder
    return None  # Return None if no folder is selected

# Main block of code to run the program
if __name__ == "__main__":
    # Initialize Tkinter root window and hide it
    root = tk.Tk()
    root.withdraw()  # Hide the Tkinter root window as we don't need it visible

    # Get the video URL from the user
    video_url = input("Please enter your URL: ").strip()  # Strip any extra spaces

    # Validate the URL input
    if not video_url:
        print("Invalid URL")  # Error message for invalid or empty URL
    else:
        save_dir = open_file_dialog()  # Ask the user to select a folder

        # Check if a valid save directory was selected
        if save_dir:
            print("Started download...")  # Inform the user that download is starting
            download_video(video_url, save_dir)  # Download the video
        else:
            print("Invalid save location...")  # Error message for invalid directory selection
