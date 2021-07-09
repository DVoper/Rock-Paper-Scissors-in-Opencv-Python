import cv2
import time
import numpy as np
import math
import HandTrackingModule2 as htm
import os
import random
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import cvzone


wCam, hCam = 640,480

stage = 1
val = ''
result = ''

uScore = 0
cScore = 0

valList = [1,2,3]


cap = cv2.VideoCapture(0)
blue = (255,0,0)
green = (0,255,0)
red = (0,0,255)
purple = (255,0,255)
white = (255,255,255)
black = (0,0,0)

cap.set(3, wCam)
cap.set(4, hCam)


pTime = 0
detector = htm.handDetector(detectionCon=0.85,maxHands = 1)


folderPath = "RPS"
myList = os.listdir(folderPath)

def find_cVal(cVal):
    valList = [1,2,3]
    
    random.shuffle(valList)
    
    cVal = valList[1]
    return cVal

cVal = 0

cVal = find_cVal(cVal)

def change_cVal(cVal):
    oricVal = cVal 
    valList = [1,2,3]
    
    random.shuffle(valList)
    if valList[1]==oricVal:
        random.shuffle(valList)
    
    cVal = valList[1]
        
    return cVal

overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)

while True:
    success,img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img,draw = True)
    if len(lmList) !=0:
        fingers = detector.fingersUp()
        totalFingers = fingers.count(1)
                          #X  Y
        if uScore != 0:
            cv2.putText(img,str(uScore),(290,465),cv2.FONT_HERSHEY_PLAIN,
                            2.75,white,3)
        elif uScore == 0:
            cv2.putText(img,"0",(290,465),cv2.FONT_HERSHEY_PLAIN,
                            2.75,white,3)
        if cScore != 0:
            cv2.putText(img,str(cScore),(340,465),cv2.FONT_HERSHEY_PLAIN,
                            2.75,white,3)
        else:
            cv2.putText(img,"0",(340,465),cv2.FONT_HERSHEY_PLAIN,
                            2.75,white,3)
            
        cv2.putText(img,":",(320,465),cv2.FONT_HERSHEY_PLAIN,
                            2.75,white,3)
            
            
        if stage==1:
            cv2.circle(img, (280,100), 75, blue,cv2.FILLED)
            cv2.putText(img,str("PLAY"),(230,125),cv2.FONT_HERSHEY_PLAIN,
                            2.75,white,3)
        if stage==2:
            timenow = (currentTime - time.time()) * -1
            if int(6-timenow) >= 1:        
                print(int(6-timenow))
                if int(6-timenow)==5:
                    cv2.circle(img, (280,100), 75, red,cv2.FILLED)
                    cv2.putText(img,str("5"),(265,135),cv2.FONT_HERSHEY_PLAIN,
                            4,white,3)
                if int(6-timenow)==4:
                    cv2.circle(img, (280,100), 75, red,cv2.FILLED)
                    cv2.putText(img,str("4"),(265,135),cv2.FONT_HERSHEY_PLAIN,
                            4,white,3)
                if int(6-timenow)==3:
                    cv2.circle(img, (280,100), 75, red,cv2.FILLED)
                    cv2.putText(img,str("3"),(265,135),cv2.FONT_HERSHEY_PLAIN,
                            4,white,3)
                if int(6-timenow)==2:
                    cv2.circle(img, (280,100), 75, red,cv2.FILLED)
                    cv2.putText(img,str("2"),(265,135),cv2.FONT_HERSHEY_PLAIN,
                            4,white,3)
                if int(6-timenow)==1:
                    cv2.circle(img, (280,100), 75, red,cv2.FILLED)
                    cv2.putText(img,str("1"),(265,135),cv2.FONT_HERSHEY_PLAIN,
                            4,white,3)
            else:
                if fingers[1] and fingers[2] and fingers[3] and fingers[4] and fingers[0] == True or totalFingers == 5 or fingers[1]== True and fingers[2] == True and fingers[3]== True and fingers[4]== False and fingers[0] == True:
                    sVar = ''
                    val = 'Paper'
                    cv2.putText(img, val, (bbox[0], bbox[1] - 30),
                            cv2.FONT_HERSHEY_PLAIN, 2, black, 2)
                elif fingers[0]== False and fingers[1]== False and fingers[2]== False and fingers[3]== False and fingers[4] == False or fingers[0]== True and fingers[1]== False and fingers[2]== False and fingers[3]== False and fingers[4] == False or fingers[0]== False and fingers[1]== False and fingers[2]== False and fingers[3]== False and fingers[4] == True or fingers[0]== True and fingers[1]== False and fingers[2]== False and fingers[3]== False and fingers[4] == True:             
                    sVar = ''
                    val = 'Rock'
                    cv2.putText(img, val, (bbox[0], bbox[1] - 30),
                            cv2.FONT_HERSHEY_PLAIN, 2, black, 2)
                elif fingers[0]== False and fingers[1]== True and fingers[2]== True and fingers[3]== False and fingers[4] == False or fingers[0]== True and fingers[1]== True and fingers[2]== True and fingers[3]== False and fingers[4] == False or fingers[0]== False and fingers[1]== True and fingers[2]== True and fingers[3]== True and fingers[4] == False or fingers[0]== True and fingers[1]== True and fingers[2]== True and fingers[3]== True and fingers[4] == False or fingers[0]== True and fingers[1]== True and fingers[2]== True and fingers[3]== False and fingers[4] == True or fingers[0]== False and fingers[1]== True and fingers[2]== True and fingers[3]== False and fingers[4] == True:
                    sVar = ''
                    val = 'Scissors'
                    cv2.putText(img, val, (bbox[0] - 20, bbox[1] - 30),
                            cv2.FONT_HERSHEY_PLAIN, 2, black, 2)
                else:
                    val = ''
                    stage = 1
                    
                crrentTime = time.time()
                stage = 3
        if stage==3:
            timnow = (crrentTime - time.time()) * -1
            if int(6-timnow) >= 3:        
                print(int(6-timnow))
                if val == "Rock":
                    h,w,c = overlayList[1].shape
                    cv2.putText(img,str("You"),(20,40),cv2.FONT_HERSHEY_PLAIN,
                                2.75,green,3)
                    cv2.putText(img,str("Computer"),(420,40),cv2.FONT_HERSHEY_PLAIN,
                                2.75,green,3)
                    img[50:h+50,0:w] = overlayList[1]
                    img[50:h+50,440:w+440] = overlayList[cVal]
                    if cVal == 1:
                        result = 'You Tie'
                    elif cVal == 2:
                        result = 'You Lose'
                        #cScore += 1
                    elif cVal == 3:
                        result = 'You Win'
                        #uScore += 1
                elif val == "Paper":
                    h,w,c = overlayList[2].shape
                    cv2.putText(img,str("You"),(20,40),cv2.FONT_HERSHEY_PLAIN,
                                2.75,green,3)
                    cv2.putText(img,str("Computer"),(420,40),cv2.FONT_HERSHEY_PLAIN,
                                2.75,green,3)
                    img[50:h+50,0:w] = overlayList[2]
                    img[50:h+50,440:w+440] = overlayList[cVal]
                    if cVal == 2:
                        result = 'You Tie'
                    elif cVal == 3:
                        result = 'You Lose'
                        #cScore += 1
                    elif cVal == 1:
                        result = 'You Win'
                        #uScore += 1
                elif val == "Scissors":
                    h,w,c = overlayList[3].shape
                    cv2.putText(img,str("You"),(20,40),cv2.FONT_HERSHEY_PLAIN,
                                2.75,green,3)
                    cv2.putText(img,str("Computer"),(420,40),cv2.FONT_HERSHEY_PLAIN,
                                2.75,green,3)
                    img[50:h+50,0:w] = overlayList[3]
                    img[50:h+50,440:w+440] = overlayList[cVal]
                    if cVal == 3:
                        result = 'You Tie'
                    elif cVal == 1:
                        result = 'You Lose'
                        #cScore += 1
                    elif cVal == 2:
                        result = 'You Win'
                        #uScore += 1
            elif int(6-timnow) >= 1:
                cv2.putText(img,result,(260,260),cv2.FONT_HERSHEY_PLAIN,3,blue,3)                        
            else:
                #print("Changing stage")
                if result == 'You Lose':
                    cScore += 1
                elif result == 'You Win':
                    uScore += 1
                cVal = change_cVal(cVal)
                #print(cVal)
                stage=1

        
        elif fingers[1]==True and fingers[2]== False and fingers[3]== False and fingers[4] == False and fingers[0] == False:
            x1, y1 = lmList[8][1:]
            #print(y1,",",x1)
            if stage == 1:
                if 60 < y1 < 175:
                    #print("TEST 1 PASSED")
                    if 215 < x1 < 350:
                        currentTime = time.time()
                        stage = 2
            #stage = 1
            val = ''
            sVar = 'Click on PLAY'
            cv2.putText(img,sVar , (bbox[0] - 20, bbox[1] - 30),
                    cv2.FONT_HERSHEY_PLAIN, 2, black, 2)
            
    #####__init__

    cv2.imshow("WebCam",img)
    key = cv2.waitKey(1)

    if key == ord('r'):
        uScore,cScore = 0,0
    elif key == ord('q'):
        cv2.destroyAllWindows()
        break
    
