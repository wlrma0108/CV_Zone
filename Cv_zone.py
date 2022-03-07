from cvzone.HandTrackingModule import HandDetector
import cv2

detector=HandDetector(maxHands=1)

cap_cam= cv2.VideoCapture(0)
cap_video =cv2.VideoCapture('video.mp4')


w=cap_cam.get(cv2.CAP_PROP_FRAME_WIDTH)
total_frames=int(cap_video.get(cv2.CAP_PROP_FRAME_COUNT))


while cap_cam.isOpened():
    ret,cam_img=cap_cam.read()
    ret2,video_img=cap_video.read()
    if not ret:
        break
    
    hands,cam_img=detector.findHands(cam_img)
    cv2.imshow('cam',cam_img)
    
    if hands:
        lm_list = hands[0]['lmList']
        length, info, cam_img = detector.findDistance(lm_list[4], lm_list[8], cam_img) 
        print(length)
        
        if length <50:
            rel_x=lm_list[4][0]/w
            frame_idx=int(rel_x * total_frames)
            if frame_idx<0:
                 frame_idx=0
                
            elif frame_idx>total_frame:
                frame_idx=total_frames
                
                                
            cv2.putText(cam_img, text='Navigation', org=(10,50), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=2, color=(255,255,255))
        else:
            pass

    if cv2.waitKey(1)==ord('q'):
        break
    