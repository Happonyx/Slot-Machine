import random
canvas_length = get_height()
canvas_width = get_width()

slot_screen_body = Rectangle(255, 200)
slot_screen_body.set_position(canvas_width / 4 - 25, 140)
slot_screen_body.set_color(Color.orange)
add(slot_screen_body)

slot_screen_body2 = Rectangle(265, 200)
slot_screen_body2.set_position(canvas_width / 4 - 30, 330)
slot_screen_body2.set_color("#E0890B")
add(slot_screen_body2)

slot_screen_body3 = Rectangle(265, 100)
slot_screen_body3.set_position(canvas_width / 4 - 30, 60)
slot_screen_body3.set_color("#E0890B")
add(slot_screen_body3)

slot_screen_rim_gray = Rectangle(235, 110)
slot_screen_rim_gray.set_position(canvas_width / 4 - 15, 180)
slot_screen_rim_gray.set_color(Color.gray)
add(slot_screen_rim_gray)

slot_screen_white = Rectangle(225, 100)
slot_screen_white.set_position(canvas_width / 4 - 10, 185)
slot_screen_white.set_color(Color.white)
add(slot_screen_white)

number_1 = random.randint(0, 9)
start_text_1 = Text(number_1)
start_text_1.set_position(canvas_width / 4 + 20, 260)
start_text_1.set_font("60pt serif")
start_text_1.set_color(Color.black)
add(start_text_1)

number_2 = random.randint(0, 9)
start_text_2 = Text(number_2)
start_text_2.set_position(canvas_width / 2 - 20, 260)
start_text_2.set_font("60pt serif")
start_text_2.set_color(Color.black)
add(start_text_2)

number_3 = random.randint(0, 9)
start_text_3 = Text(number_3)
start_text_3.set_position(canvas_width / 2 + 40, 260)
start_text_3.set_font("60pt serif")
start_text_3.set_color(Color.black)
add(start_text_3)

lever_handle = Rectangle(25, 15)
lever_handle.set_position(330, canvas_length / 2)
lever_handle.set_color("#6D6D6D")
add(lever_handle)

lever_stick = Rectangle(15, 100)
lever_stick.set_position(345, canvas_length / 2 - 90)
lever_stick.set_color("#505050")
add(lever_stick)

ball = Circle(16)
ball.set_position(352.5, canvas_length / 2 - 75)
ball.set_color(Color.red)
add(ball)

jackpot_screen = Rectangle(240, 50)
jackpot_screen.set_position(84, 86)
jackpot_screen.set_color(Color.white)
add(jackpot_screen)

slot = Rectangle(50, 50)
slot.set_position(canvas_width / 2 - 25, canvas_length / 2 + 70)
slot.set_color(Color.gray)
add(slot)

number_of_tries = 0
blinking_text_switch = True
switch = True
def clicked(x, y):
    global number_of_tries, switch
    if x >= (canvas_width / 2 - 25) and x <= (canvas_width / 2 + 25) and y >= (canvas_length / 2 + 70) and y <= (canvas_length / 2 + 120):
        if switch == True:
            switch = False
            slot_coin = Circle(17)
            slot_coin.set_position(canvas_width / 2, canvas_length / 2 + 150)
            slot_coin.set_color(Color.yellow)
            add(slot_coin)
            
            def move_slot_coin():
                if slot_coin.get_y() != 330:
                    slot_coin.move(0, -10)
                remove(slot)
                add(slot)
            slot_coin_move_timer = timer.set_interval(move_slot_coin, 50)
            def stop_slot_coin_move_timer():
                global switch
                timer.clear_interval(slot_coin_move_timer)
                remove(slot_coin)
                switch = True
            timer.set_timeout(stop_slot_coin_move_timer, 700)
            number_of_tries += 1
    if x >= 337.5 and x <= 367.5 and y >= (canvas_length / 2 - 90) and y <= (canvas_length / 2 - 60):
        if number_of_tries > 0:
            if switch == True:
                number_of_tries -= 1
                triple_jackpot = Text("TRIPLE JACKPOT")
                triple_jackpot.set_position(canvas_width - 283, 120)
                triple_jackpot.set_color(Color.green)
                triple_jackpot.set_font("21pt Impact")
                six_jackpot = Text("DEVIL'S JACKPOT")
                six_jackpot.set_position(canvas_width - 286, 120)
                six_jackpot.set_color(Color.red)
                six_jackpot.set_font("21pt Impact")
                nine_jackpot = Text("GRAND JACKPOT")
                nine_jackpot.set_position(canvas_width - 285, 120)
                nine_jackpot.set_color("#c8c717")
                nine_jackpot.set_font("21pt Impact")
                regular_jackpot = Text("JACKPOT")
                regular_jackpot.set_position(canvas_width - 250, 122.5)
                regular_jackpot.set_color(Color.black)
                regular_jackpot.set_font("25pt Impact")
                switch = False
                numbers = []
                def new_text():
                    starter_number_1 = random.randint(0, 9)
                    starter_number_2 = random.randint(0, 9)
                    starter_number_3 = random.randint(0, 9)
                    start_text_1.set_text(starter_number_1)
                    start_text_2.set_text(starter_number_2)
                    start_text_3.set_text(starter_number_3)
                    numbers.append(starter_number_1)
                    numbers.append(starter_number_2)
                    numbers.append(starter_number_3)
                timer_id = timer.set_interval(new_text, 1)
                def clear_timer():
                    timer.clear_interval(timer_id)
                    def turn_on_switch():
                        global switch
                        switch = True
                    timer.set_timeout(turn_on_switch, 800)
                    starter_number_1 = numbers[-3]
                    starter_number_2 = numbers[-2]
                    starter_number_3 = numbers[-1]
                    if starter_number_1 == starter_number_2 and starter_number_1 == starter_number_3:
                        if starter_number_1 == 3 and starter_number_2 == 3 and starter_number_3 == 3:
                            def blinking_text():
                                global blinking_text_switch
                                if blinking_text_switch == True:
                                    add(triple_jackpot)
                                    blinking_text_switch = False
                                elif blinking_text_switch == False:
                                    remove(triple_jackpot)
                                    blinking_text_switch = True
                            jackpot_timer = timer.set_interval(blinking_text, 400)
                            def stop_jackpot_timer():
                                global blinking_text_switch
                                timer.clear_interval(jackpot_timer)
                                remove(triple_jackpot)
                                blinking_text_switch = True
                            timer.set_timeout(stop_jackpot_timer, 3500)
                            def generate_coin():
                                random_x_coordinate = random.randint(0, canvas_width)
                                random_y_coordinate = random.randint(-200, 0)
                                coin = Circle(10)
                                coin.set_position(random_x_coordinate, random_y_coordinate)
                                coin.set_color(Color.yellow)
                                add(coin)
                                def move_coin():
                                    coin.move(0, 10)
                                coin_timer = timer.set_interval(move_coin, 50)
                                
                                def stop_coin_timer():
                                    timer.clear_interval(coin_timer)
                                timer.set_timeout(stop_coin_timer, 10000)
                            generate_coin_timer = timer.set_interval(generate_coin, 150)
                            def stop_creating_coins():
                                timer.clear_interval(generate_coin_timer)
                            timer.set_timeout(stop_creating_coins, 3000)
                        elif starter_number_1 == 6 and starter_number_2 == 6 and starter_number_3 == 6:
                            def blinking_text():
                                global blinking_text_switch
                                if blinking_text_switch == True:
                                    add(six_jackpot)
                                    blinking_text_switch = False
                                elif blinking_text_switch == False:
                                    remove(six_jackpot)
                                    blinking_text_switch = True
                            jackpot_timer = timer.set_interval(blinking_text, 400)
                            def stop_jackpot_timer():
                                global blinking_text_switch
                                timer.clear_interval(jackpot_timer)
                                remove(six_jackpot)
                                blinking_text_switch = True
                            timer.set_timeout(stop_jackpot_timer, 3500)
                            def generate_coin():
                                random_x_coordinate = random.randint(0, canvas_width)
                                random_y_coordinate = random.randint(-200, 0)
                                coin = Circle(10)
                                coin.set_position(random_x_coordinate, random_y_coordinate)
                                coin.set_color(Color.yellow)
                                add(coin)
                                def move_coin():
                                    coin.move(0, 10)
                                coin_timer = timer.set_interval(move_coin, 50)
                                
                                def stop_coin_timer():
                                    timer.clear_interval(coin_timer)
                                timer.set_timeout(stop_coin_timer, 10000)
                            generate_coin_timer = timer.set_interval(generate_coin, 100)
                            def stop_creating_coins():
                                timer.clear_interval(generate_coin_timer)
                            timer.set_timeout(stop_creating_coins, 4500)
                        elif starter_number_1 == 9 and starter_number_2 == 9 and starter_number_3 == 9:
                            def blinking_text():
                                global blinking_text_switch
                                if blinking_text_switch == True:
                                    add(nine_jackpot)
                                    blinking_text_switch = False
                                elif blinking_text_switch == False:
                                    remove(nine_jackpot)
                                    blinking_text_switch = True
                            jackpot_timer = timer.set_interval(blinking_text, 400)
                            def stop_jackpot_timer():
                                global blinking_text_switch
                                timer.clear_interval(jackpot_timer)
                                remove(nine_jackpot)
                                blinking_text_switch = True
                            timer.set_timeout(stop_jackpot_timer, 3500)
                            def generate_coin():
                                random_x_coordinate = random.randint(0, canvas_width)
                                random_y_coordinate = random.randint(-200, 0)
                                coin = Circle(10)
                                coin.set_position(random_x_coordinate, random_y_coordinate)
                                coin.set_color(Color.yellow)
                                add(coin)
                                def move_coin():
                                    coin.move(0, 10)
                                coin_timer = timer.set_interval(move_coin, 50)
                                
                                def stop_coin_timer():
                                    timer.clear_interval(coin_timer)
                                timer.set_timeout(stop_coin_timer, 10000)
                            generate_coin_timer = timer.set_interval(generate_coin, 50)
                            def stop_creating_coins():
                                timer.clear_interval(generate_coin_timer)
                            timer.set_timeout(stop_creating_coins, 6000)
                        else:
                            def blinking_text():
                                global blinking_text_switch
                                if blinking_text_switch == True:
                                    add(regular_jackpot)
                                    blinking_text_switch = False
                                elif blinking_text_switch == False:
                                    remove(regular_jackpot)
                                    blinking_text_switch = True
                            jackpot_timer = timer.set_interval(blinking_text, 400)
                            def stop_jackpot_timer():
                                global blinking_text_switch
                                timer.clear_interval(jackpot_timer)
                                remove(regular_jackpot)
                                blinking_text_switch = True
                            timer.set_timeout(stop_jackpot_timer, 3500)
                            def generate_coin():
                                random_x_coordinate = random.randint(0, canvas_width)
                                random_y_coordinate = random.randint(-200, 0)
                                coin = Circle(10)
                                coin.set_position(random_x_coordinate, random_y_coordinate)
                                coin.set_color(Color.yellow)
                                add(coin)
                                def move_coin():
                                    coin.move(0, 10)
                                coin_timer = timer.set_interval(move_coin, 50)
                                
                                def stop_coin_timer():
                                    timer.clear_interval(coin_timer)
                                timer.set_timeout(stop_coin_timer, 10000)
                            generate_coin_timer = timer.set_interval(generate_coin, 200)
                            def stop_creating_coins():
                                timer.clear_interval(generate_coin_timer)
                            timer.set_timeout(stop_creating_coins, 2500)
                timer.set_timeout(clear_timer, 1200)
                
                def move_lever():
                    global lever_stick, ball
                    if lever_stick.get_y() != canvas_length / 2 + 90:
                        remove(lever_stick)
                        lever_stick_y = lever_stick.get_y()
                        if lever_stick_y < canvas_length / 2 + 7.5:
                            lever_stick = Rectangle(15, lever_stick.get_height() - 20)
                            lever_stick.set_position(345, lever_stick_y + 20)
                        elif lever_stick_y >= canvas_length / 2 + 7.5:
                            lever_stick = Rectangle(15, lever_stick.get_height() + 16)
                            lever_stick.set_position(345, canvas_length / 2 + 7.5)
                        lever_stick.set_color("#505050")
                        add(lever_stick)
                        remove(ball)
                        add(ball)
                    if ball.get_y() != 345:
                        ball.move(0, 20)
                        ball_current_location = ball.get_y()
                        ball_current_radius = ball.get_radius()
                        if ball.get_y() < canvas_length / 2:
                            remove(ball)
                            ball = Circle(ball_current_radius + 1.5)
                            ball.set_position(352.5, ball_current_location)
                            ball.set_color(Color.red)
                            add(ball)
                        elif ball.get_y() > canvas_length / 2 and ball_current_radius != 16:
                            remove(ball)
                            ball = Circle(ball_current_radius - 1.5)
                            ball.set_position(352.5, ball_current_location)
                            ball.set_color(Color.red)
                            add(ball)
                            
                    
                lever_timer = timer.set_interval(move_lever, 50)
                
                def clear_lever_timer():
                    timer.clear_interval(lever_timer)
                    global ball
                    def move_lever_back():
                        global lever_stick, ball
                        if ball.get_y() > canvas_width / 2 - 20:
                            ball.move(0, - 20)
                            ball_current_location = ball.get_y()
                            ball_current_radius = ball.get_radius()
                            if ball.get_y() < canvas_length / 2:
                                remove(ball)
                                ball = Circle(ball_current_radius - 1.5)
                                ball.set_position(352.5, ball_current_location)
                                ball.set_color(Color.red)
                                add(ball)
                            elif ball.get_y() > canvas_length / 2:
                                remove(ball)
                                ball = Circle(ball_current_radius + 1.5)
                                ball.set_position(352.5, ball_current_location)
                                ball.set_color(Color.red)
                                add(ball)
                            remove(lever_stick)
                            lever_stick = Rectangle(15, lever_stick.get_height() - 20)
                            lever_stick.set_position(345, canvas_length / 2 + 7.5)
                            lever_stick.set_color("#505050")
                            add(lever_stick)
                            remove(ball)
                            add(ball)
                    lever_timer2 = timer.set_interval(move_lever_back, 50)
                    ball_current_location = ball.get_y()
                    ball_current_radius = ball.get_radius()
                    remove(ball)
                    ball = Circle(16)
                    ball.set_position(352.5, ball_current_location)
                    ball.set_color(Color.red)
                    add(ball)
                    def clear_lever_timer2():
                        timer.clear_interval(lever_timer2)
                        global lever_stick
                        remove(lever_stick)
                        remove(ball)
                        lever_stick = Rectangle(15, 98)
                        lever_stick.set_position(345, canvas_length / 2 - 90)
                        lever_stick.set_color("#505050")
                        add(lever_stick)
                        add(ball)
                    timer.set_timeout(clear_lever_timer2, 600)
                timer.set_timeout(clear_lever_timer, 600)
            
            
        else:
            pass

add_mouse_click_handler(clicked)