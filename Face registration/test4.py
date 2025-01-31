import cv2
import os
import time

def capture_face_images(user_id, save_path='/home/mona/Face recognition/database', num_images=5):
    os.makedirs(save_path, exist_ok=True)
    user_folder = os.path.join(save_path, str(user_id))
    os.makedirs(user_folder, exist_ok=True)
    
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    
    instructions = [
        "Look straight at the camera",
        "Turn your head slightly to the left",
        "Turn your head slightly to the right",
        "Look up slightly",
        "Look down slightly"
    ]
    
    count = 0
    while count < num_images:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image. Exiting...")
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))
        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            face = frame[y:y + h, x:x + w]
            
            if count < len(instructions):
                text = instructions[count]
                cv2.putText(frame, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                cv2.putText(frame, "Adjust your position", (50, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            
            cv2.imshow("Face Registration", frame)
            
            # Automatically capture the image when the face is in the correct position
            if count == 0:  # Look straight
                # Check if the face is roughly centered (you can adjust these thresholds)
                if abs(x + w/2 - frame.shape[1]/2) < 50 and abs(y + h/2 - frame.shape[0]/2) < 50:
                    img_path = os.path.join(user_folder, f"face_{count}.jpg")
                    cv2.imwrite(img_path, face)
                    print(f"Image {count + 1}/{num_images} captured: {img_path}")
                    count += 1
                    time.sleep(1)  # Pause to allow the user to adjust
            elif count == 1:  # Turn head slightly to the left
                # Check if the face is shifted to the left (you can adjust these thresholds)
                if x + w/2 < frame.shape[1]/2 - 50:
                    img_path = os.path.join(user_folder, f"face_{count}.jpg")
                    cv2.imwrite(img_path, face)
                    print(f"Image {count + 1}/{num_images} captured: {img_path}")
                    count += 1
                    time.sleep(1)  # Pause to allow the user to adjust
            elif count == 2:  # Turn head slightly to the right
                # Check if the face is shifted to the right (you can adjust these thresholds)
                if x + w/2 > frame.shape[1]/2 + 50:
                    img_path = os.path.join(user_folder, f"face_{count}.jpg")
                    cv2.imwrite(img_path, face)
                    print(f"Image {count + 1}/{num_images} captured: {img_path}")
                    count += 1
                    time.sleep(1)  # Pause to allow the user to adjust
            elif count == 3:  # Look up slightly
                # Check if the face is shifted upward (you can adjust these thresholds)
                if y + h/2 < frame.shape[0]/2 - 50:
                    img_path = os.path.join(user_folder, f"face_{count}.jpg")
                    cv2.imwrite(img_path, face)
                    print(f"Image {count + 1}/{num_images} captured: {img_path}")
                    count += 1
                    time.sleep(1)  # Pause to allow the user to adjust
            elif count == 4:  # Look down slightly
                # Check if the face is shifted downward (you can adjust these thresholds)
                if y + h/2 > frame.shape[0]/2 + 50:
                    img_path = os.path.join(user_folder, f"face_{count}.jpg")
                    cv2.imwrite(img_path, face)
                    print(f"Image {count + 1}/{num_images} captured: {img_path}")
                    count += 1
                    time.sleep(1)  # Pause to allow the user to adjust
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    print("Face registration complete!")

# Example usage
user_id = input("Enter user ID: ")
capture_face_images(user_id)