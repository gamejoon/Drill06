from pico2d import *

def handle_events():
    global running, arrow_arr

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            arrow_arr.append((event.x, TUK_HEIGHT - 1 - event.y))

def run_motion():
    global frame

    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    frame = (frame + 1) % 8

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

open_canvas(TUK_WIDTH, TUK_HEIGHT)

background = load_image("TUK_GROUND.png")
arrow = load_image("hand_arrow.png")
character = load_image("run_animation.png")

running = True

frame = 0
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
arrow_arr = []

while running:
    clear_canvas()

    handle_events()

    background.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    for i in range(0, len(arrow_arr)):
        arrow.draw(arrow_arr[i][0], arrow_arr[i][1])
    run_motion()

    update_canvas()
    delay(0.05)

close_canvas()