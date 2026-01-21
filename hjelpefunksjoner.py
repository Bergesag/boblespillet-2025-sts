"""
Ulike funksjoner som er til bruk i animasjonslogikk etc.
main.py skal helst ikke bli noe lengre.
"""

def processKeypress(evt):
    global dx, dy, x_step, y_step
    key = evt.keysym
    print(f'key: {key}')
    if key == "Left":
        dx = -x_step
        dy = 0
    elif key == "Up":
        dx = 0
        dy = -y_step
    elif key == "Right":
        dx= x_step
        dy = 0
    elif key == "Down":
        dx = 0
        dy = y_step
