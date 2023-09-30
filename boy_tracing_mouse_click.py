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

TUK_WIDHT, TUK_HEIGHT = 1280, 1024

open_canvas(TUK_WIDHT, TUK_HEIGHT)

background = load_image("TUK_GROUND.png")
arrow = load_image("hand_arrow.png")
character = load_image("run_animation.png")

running = True

arrow_arr = []

while running:
    clear_canvas()

    handle_events()

    background.draw(TUK_WIDHT // 2, TUK_HEIGHT // 2)
    for i in range(0, len(arrow_arr)):
        arrow.draw(arrow_arr[i][0], arrow_arr[i][1])

    update_canvas()

close_canvas()