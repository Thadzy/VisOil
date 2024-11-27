import cv2
import os

def video_to_frames(video_path, output_folder, target_frames=600):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Load the video
    cap = cv2.VideoCapture(video_path)

    # Get the total frames and frames per second (fps)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Calculate interval to save approximately the desired number of frames
    frame_interval = max(int(total_frames / target_frames), 1)

    frame_count = 0
    saved_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break  # Exit the loop if the video ends

        # Save frames at the calculated interval
        if frame_count % frame_interval == 0:
            frame_filename = os.path.join(output_folder, f"frame_{saved_count:04d}.jpg")
            cv2.imwrite(frame_filename, frame)
            saved_count += 1

            if saved_count >= target_frames:  # Stop once the target number of frames is saved
                break

        frame_count += 1

    cap.release()
    print(f"Extraction completed! {saved_count} frames saved in {output_folder}")

# Path to your video and output folder
video_path = r"D:\Thadzy\Innovation\Dataset\Oilspill271124dataset.mp4"
output_folder = r"D:\Thadzy\Innovation\Dataset\Extracted_Frames"

# Extract approximately 600 frames
video_to_frames(video_path, output_folder, target_frames=600)
