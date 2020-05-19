def setup():
    size(500, 500)
    global ball_x, ball_y, speed_x, speed_y
    ball_x = random(500)
    ball_y = random(15, 250)
    speed_x = 3
    speed_y = 3
    
    global brick1, brick2, brick3, brick4, brick5
    brick1 = True
    brick2 = True
    brick3 = True
    brick4 = True
    brick5 = True
    
    reset_powerup()

def reset_powerup():
    global frames_til_powerup, powerup_x, powerup_y
    global powerup_duration
    powerup_x = random(500)
    powerup_y = -10
    # 60 fps * seconds
    frames_til_powerup = 60 * int(random(15))
    powerup_duration = -1

def draw():
    global speed_x, powerup_duration
    global ball_x, ball_y, speed_y
    
    if powerup_duration > 0:
        background(0, 255, 0)
    else:
        background(0)
    
    global brick1, brick2, brick3, brick4, brick5
    
    if not (brick1 or brick2 or brick3 or brick4 or brick5):
        background(255, 255, 0)
        return
        
    # The bricks.
    global brick1, brick2, brick3, brick4, brick5
    fill(255)
    if brick1:
        rect(0, 0, 100, 10)
    if brick2:
        rect(100, 0, 100, 10)
    if brick3:
        rect(200, 0, 100, 10)
    if brick4:
        rect(300, 0, 100, 10)
    if brick5:
        rect(400, 0, 100, 10)
        
    # The paddle.
    fill(255)
    rect(mouseX - 25, 480, 50, 10)
    paddle_l = mouseX - 25
    paddle_r = paddle_l + 50
    paddle_top = 480
    paddle_bottom = 490

    # The powerups.
    global frames_til_powerup, powerup_x, powerup_y
    global powerup_duration
    if powerup_duration > 0:
        powerup_duration = powerup_duration - 1
        if powerup_duration <= 0:
            speed_x = speed_x * 2
            speed_y = speed_y * 2
            reset_powerup()
    else:
        if frames_til_powerup > 0:
            frames_til_powerup = frames_til_powerup - 1
        elif powerup_y >= 510:
            reset_powerup()
        else:
            if (
                powerup_x >= paddle_l and
                powerup_x <= paddle_r and
                powerup_y >= paddle_top and
                powerup_y <= paddle_bottom):
                powerup_duration = 1800 # 30s in frames
                speed_x = speed_x / 2
                speed_y = speed_y / 2
            else:
                fill(0, 0, 255)
                ellipse(powerup_x, powerup_y, 10, 10)
                powerup_y = powerup_y + 1

    # The ball.
    fill(255)
    ellipse(ball_x, ball_y, 10, 10)
    
    if ball_x <= 0 or ball_x >= 500:
        speed_x = -speed_x
    if ball_y <= 0:
        speed_y = -speed_y
    elif (
            ball_x >= paddle_l and
            ball_x <= paddle_r and
            ball_y >= paddle_top and
            ball_y <= paddle_bottom):
        paddle_speed = mouseX - pmouseX
        if paddle_speed != 0:
            if powerup_duration > 0:
                paddle_speed = paddle_speed / 2
            speed_x = paddle_speed
        speed_y = -speed_y
    elif brick1 and ball_y <= 10 and ball_x <= 100:
        brick1 = False
        speed_y = -speed_y
    elif brick2 and ball_y <= 10 and ball_x <= 200 and ball_x > 100:
        brick2 = False
        speed_y = -speed_y
    elif brick3 and ball_y <= 10 and ball_x <= 300 and ball_x > 200:
        brick3 = False
        speed_y = -speed_y
    elif brick4 and ball_y <= 10 and ball_x <= 400 and ball_x > 300:
        brick4 = False
        speed_y = -speed_y
    elif brick5 and ball_y <= 10 and ball_x > 400:
        brick5 = False
        speed_y = -speed_y

    ball_x = ball_x + speed_x
    ball_y = ball_y + speed_y
