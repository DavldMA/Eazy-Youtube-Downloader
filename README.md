# Eazy-Youtube-Downloader

This Python script provides a simple command-line interface for downloading YouTube videos and playlists as either audio, video, or both. The script utilizes the `pytube` library for interacting with YouTube, and it offers the following features:

- **Download Options:**
  - Download videos as audio-only.
  - Download videos as video.
  - Download both audio and video simultaneously.
  - Close the program.

- **User Interface:**
  - Interactive menu with colorful console output using the `colorama` library.
  - Clear screen functionality for a clean display.

- **Features:**
  - Supports both single YouTube video and playlist links.
  - Displays information about the video, such as title, views, and duration.
  - Progress bar with download status using `tqdm`.
  - Handles special characters in video titles for safe filenames.
  - Zips downloaded files into separate audio and video archives.

**Installation:**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. Install the required dependencies using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

**How to Use:**
1. Run the script:
   ```bash
   python main.py
   ```

2. Choose the desired download option by entering the corresponding number (0-3).
3. Paste the YouTube video or playlist link.
4. Enjoy the downloaded content in the 'download' folder :).

**Note:**
- This script assumes that you have the necessary rights to download and use the content as per YouTube's terms of service.
