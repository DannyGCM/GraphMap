# Danny Garcia
# sample_program.py

# Modules
import GraphMap as gm

# Creates window
window = gm.Window("Sample Program", (500, 500), background=(80, 80, 80))
window.change_icon("sample_icon.ico")

# Primitive graphic objects
gm.Polygon(window, (50, 10, 150, 10, 100, 150), color=(60, 60, 120), outline_color=(30, 30, 60), outline_width=4)
circle = gm.Circle(window, (250, 250), radius=25, color=(200, 100, 100), inplace_draw=False)
circle.draw()
circle.draw()  # Shows error message instead of crashing

# Complex graphic objects
button = gm.Button(window, (40, 250), (140, 350), text="BUTTON", font="Consolas")

# Main loop
while window.running:
	# Event handling
	if len(window.last_key) == 1:
		print(f"You pressed the key '{window.last_key}'")
	if window.last_mouse[0]:
		if window.last_motion[1] < (window.height() // 2):
			print("You clicked on the upper half of the window.")
		else:
			print("You clicked on the lower half of the window.")

	if circle.point[0] >= 400:
		circle.move(x=-200, y=-200)
	else:
		circle.move(x=1, y=1)

	# Progresses time
	window.tick()

# Termination
window.quit()
