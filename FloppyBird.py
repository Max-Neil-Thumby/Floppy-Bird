import thumby
import time

#while loops
over = 0
start = 0
other = 0

#start screen
def startScreen():
    global start, other
    other = 0
    time.sleep_ms(50)
    thumby.display.fill(0)
    thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
    thumby.display.drawText("PLAY FLOPPY BIRD?", 2, 5, 1)
    thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
    thumby.display.drawText("PRESS A TO PLAY", 2, 20, 1)
    thumby.display.drawText("PRESS B TO EXIT", 2, 30, 1)
    thumby.display.update()
    
    while other == 0:
        if thumby.buttonA.pressed():
            start = 1
            other = 1
            
        if thumby.buttonB.pressed():
            thumby.exit()

startScreen()

def restart():
    start = 1
    other = 1

#bitmaps
while start == 1:
    birdbyte = bytearray([48,204,210,162,138,130,76,48])
    birdbyte2 = bytearray([48,220,210,162,138,130,76,48])
    birdbyte3 = bytearray([48,204,202,178,138,130,76,48])
    birdbyte4 = bytearray([48,204,234,146,138,130,76,48])

    bird = thumby.Sprite(8,8, birdbyte +  birdbyte + birdbyte + birdbyte + birdbyte2 + birdbyte2 + birdbyte2 + birdbyte2 + birdbyte3 + birdbyte3 + birdbyte3 + birdbyte3 + birdbyte4 + birdbyte4 + birdbyte4 + birdbyte4, 0, 0)
    birdFrame = 0
    p1byte = bytearray([0,255,255,255,255,0,
               3,3,3,3,3,3,
               0,0,0,0,0,0,
               192,192,192,192,192,192,
               0,255,255,255,255,0])
               
    p2byte = bytearray([48,63,63,63,63,48,
               0,0,0,0,0,0,
               0,0,0,0,0,0,
               12,252,252,252,252,12,
               0,255,255,255,255,0])
               
    p3byte = bytearray([0,255,255,255,255,0,
               48,63,63,63,63,48,
               0,0,0,0,0,0,
               0,0,0,0,0,0,
               12,252,252,252,252,12])
               
    pillar1 = thumby.Sprite(6, 40, p1byte)
    pillar2 = thumby.Sprite(6, 40, p2byte)
    pillar3 = thumby.Sprite(6, 40, p3byte)
    
    #setting variables
    score = 0
    over = 1
    bird.x = 0
    bird.y = 0
    pillar1.x = 80
    pillar1.y = 0
    pillar2.x = 116
    pillar2.y = 0
    pillar3.x = 152
    pillar3.y = 0
    
    bird.xVel = 0
    bird.yVel = 0
    
    pillar1.passed = False
    pillar2.passed = False
    pillar3.passed = False
    
    def checkScore(pillar):
        global score
        if bird.x > pillar.x + 6 and not pillar.passed:
            pillar.passed = True
            score += 1
            pillar.passed = False
    
    #end screen
    def endscreen():
        global over
        global score
        thumby.display.fill(0)
        thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
        thumby.display.drawText("GAME OVER!", 7, 16, 1)
        thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
        thumby.display.drawText("PRESS A TO PLAY", 6, 27, 1)
        thumby.display.drawText("AGAIN.", 25, 34, 1)

        thumby.display.drawText("SCORE: " + str(score), 40, 2, 1)
        thumby.display.update()
        
        while over == 0:
            if thumby.buttonA.pressed():
                score = 0
                over = 1
                bird.x = 0
                bird.y = 0
                pillar1.x = 80
                pillar1.y = 0
                pillar2.x = 116
                pillar2.y = 0
                pillar3.x = 152
                pillar3.y = 0
                bird.xVel = 0
                bird.yVel = 0
                
                pillar1.passed = False
                pillar2.passed = False
                pillar3.passed = False
        
        while 1:
            if thumby.buttonA.pressed():
                restart()
                break
        
        #3, 2, 1, countdown back to start screen
        # thumby.display.fill(0)
        # thumby.display.drawText("GAME OVER!", 7, 16, 1)
        # thumby.display.drawText("Score: " + str(score), 23, 2, 1)
        # thumby.display.drawText("3", 65, 30, 1)
        # thumby.display.update()
        # time.sleep(1)
        # thumby.display.fill(0)
        # thumby.display.drawText("GAME OVER!", 7, 16, 1)
        # thumby.display.drawText("Score: " + str(score), 23, 2, 1)
        # thumby.display.drawText("2", 65, 30, 1)
        # thumby.display.update()
        # time.sleep(1)
        # thumby.display.fill(0)
        # thumby.display.drawText("GAME OVER!", 7, 16, 1)
        # thumby.display.drawText("Score: " + str(score), 23, 2, 1)
        # thumby.display.drawText("1", 65, 30, 1)
        # thumby.display.update()
        # time.sleep(1)
        
    
    #font
    thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
    
    #main loop
    while over == 1:
        
        #drawing sprites
        thumby.display.fill(0)
        thumby.display.drawSprite(pillar1)
        thumby.display.drawSprite(pillar2)
        thumby.display.drawSprite(pillar3)
        bird.setFrame(birdFrame)
        thumby.display.drawSprite(bird)
        birdFrame += 1
        thumby.display.setFPS(60)
        
        thumby.display.drawText(str(score), 68, 2, 1)
        
        thumby.display.update()
        
    
    
        #setting jump velocity
        if thumby.buttonA.pressed():
            bird.yVel = 0.55
            bird.setFrame(1)
    
        #making the y actually go down with this new velocity variable
        bird.y -= bird.yVel
    
        #making sure the down velocity is set
        if bird.yVel != 0:
            bird.yVel -= 0.055
    
    
        #bird cannot go off the top of the screen
        if bird.y < 0:
            bird.y = 0
            
        #make the pillars move
        pillar1.x -= 0.25
        pillar2.x -= 0.25
        pillar3.x -= 0.25
        
        
        if pillar1.x < 80:
            checkScore(pillar1)
        if pillar2.x < 80:
            checkScore(pillar2)
        if pillar3.x < 80:
            checkScore(pillar3)
        
        #kill the bird if it goes to the bottom
        if bird.y > 33:
            endscreen()
            over = 0
                
                
        #pillar 1 hitboxes
        if bird.x+8 > pillar1.x:
            if bird.x+8 < pillar1.x+7:
                if bird.y < pillar1.y+10:
                    endscreen()
                    over = 0
                    
        if bird.x+8 > pillar1.x:
            if bird.x+8 < pillar1.x+7:
                if bird.y+8 > pillar1.y+30:
                    endscreen()
                    over = 0
                    
        if bird.x > pillar1.x:
            if bird.x < pillar1.x+7:
                if bird.y < pillar1.y+10:
                    endscreen()
                    over = 0
                    
        if bird.x > pillar1.x:
            if bird.x < pillar1.x+7:
                if bird.y+8 > pillar1.y+30:
                    endscreen()
                    over = 0
        
        #pillar 2 hitboxes
        if bird.x+8 > pillar2.x:
            if bird.x+8 < pillar2.x+7:
                if bird.y < pillar2.y+6:
                    endscreen()
                    over = 0
                    
        if bird.x+8 > pillar2.x:
            if bird.x+8 < pillar2.x+7:
                if bird.y+8 > pillar2.y+26:
                    endscreen()
                    over = 0
                    
        if bird.x > pillar2.x:
            if bird.x < pillar2.x+7:
                if bird.y < pillar2.y+6:
                    endscreen()
                    over = 0
                    
        if bird.x > pillar2.x:
            if bird.x < pillar2.x+7:
                if bird.y+8 > pillar2.y+26:
                    endscreen()
                    over = 0
        
        #pillar 3 hitboxes
        if bird.x+8 > pillar3.x:
            if bird.x+8 < pillar3.x+7:
                if bird.y < pillar3.y+14:
                    endscreen()
                    over = 0
                    
        if bird.x+8 > pillar3.x:
            if bird.x+8 < pillar3.x+7:
                if bird.y+8 > pillar3.y+34:
                    endscreen()
                    over = 0
                    
        if bird.x > pillar3.x:
            if bird.x < pillar3.x+7:
                if bird.y < pillar3.y+14:
                    endscreen()
                    over = 0
                    
        if bird.x > pillar3.x:
            if bird.x < pillar3.x+7:
                if bird.y+8 > pillar3.y+34:
                    endscreen()
                    over = 0
                    
        #make the pillars keep repeating
        if pillar1.x < -6:
            pillar1.x = pillar3.x + 36

        if pillar2.x < -6:
            pillar2.x = pillar1.x + 36
    
        if pillar3.x < -6:
            pillar3.x = pillar2.x + 36





