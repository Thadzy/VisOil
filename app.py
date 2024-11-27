import cv2

# Set up the RTSP URL
rtsp_url = "rtsp://admin:taspol0812@192.168.2.34/Streaming/Channels/101"

# Open the video stream
cap = cv2.VideoCapture(rtsp_url)

if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

while True:
    # Capture frame-by-frame  
    ret, frame = cap.read()
    
    # Check if frame is received
    if not ret:
        print("Error: Could not read frame.")
        break

    # Display the resulting frame
    cv2.imshow('RTSP Stream', frame)

    # Press 'q' on the keyboard to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When done, release the capture
cap.release()
cv2.destroyAllWindows()
