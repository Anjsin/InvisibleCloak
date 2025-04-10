import cv2
import numpy as np
import time

def create_invisibility_cloak():
    cap = cv2.VideoCapture(0)
    
    time.sleep(3)
    
    for i in range(30):
        ret, background = cap.read()
    
    background = np.flip(background, axis=1)
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
            
        frame = np.flip(frame, axis=1)
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        lower_red1 = np.array([0, 120, 70])
        upper_red1 = np.array([10, 255, 255])
        mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
        
        lower_red2 = np.array([170, 120, 70])
        upper_red2 = np.array([180, 255, 255])
        mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
        
        mask = mask1 + mask2
        
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
        mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))
        
        mask_inv = cv2.bitwise_not(mask)
        
        res1 = cv2.bitwise_and(frame, frame, mask=mask_inv)
        
        res2 = cv2.bitwise_and(background, background, mask=mask)
        
        final_output = cv2.addWeighted(res1, 1, res2, 1, 0)
        
        cv2.imshow("Invisibility Cloak", final_output)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    create_invisibility_cloak() 