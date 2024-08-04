import argparse
import tkinter as tk
from tkinter import messagebox
from module import video_detection, image_upload_detection

def show_interface():
    def run_video_detection():
        root.destroy()
        video_detection.main()

    def run_image_upload_detection():
        root.destroy()
        image_upload_detection.upload_image()

    root = tk.Tk()
    root.title("Number Plate Detection")

    label = tk.Label(root, text="Choose an option to run:")
    label.pack(pady=10)

    btn_video = tk.Button(root, text="Video Detection", command=run_video_detection)
    btn_video.pack(pady=5)

    btn_image_upload = tk.Button(root, text="Image Upload Detection", command=run_image_upload_detection)
    btn_image_upload.pack(pady=5)

    root.mainloop()

def main():
    parser = argparse.ArgumentParser(description="Number Plate Detection System")
    parser.add_argument('-v', '--video', action='store_true', help="Run video detection")
    parser.add_argument('-u', '--upload', action='store_true', help="Run image upload detection")
    args = parser.parse_args()

    if args.video:
        video_detection.main()
    elif args.upload:
        image_upload_detection.upload_image()
    else:
        show_interface()

if __name__ == "__main__":
    main()
