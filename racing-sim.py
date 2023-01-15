#!/usr/bin/env python3

# PYTHON RACING SIMULATOR
# Inspired by https://www.youtube.com/watch?v=KkMZI5Jbf18
# Copyright (C) 2023 Daniele Verducci

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# REQUIREMENTS:
# pip install pysdl2 pysdl2-dll

import sdl2.ext
import math
import time

WIN_WIDTH = 640
WIN_HEIGHT = 480
SKY_COLOR = [0,128,255]
FLOOR_COLOR = [64,64,64]

class Main:

	def __init__(self):
		# Print instructions
		print('RACING SIMULATOR by penguin86\n\nMovement: up, down, left, right\n\nFPS:')

		# Graphics
		sdl2.ext.init()
		self.window = sdl2.SDL_CreateWindow(b"Racing simulator", 100, 100, WIN_WIDTH, WIN_HEIGHT,sdl2.SDL_WINDOW_SHOWN)
		self.renderer = sdl2.SDL_CreateRenderer(self.window, -1,sdl2.SDL_RENDERER_ACCELERATED |sdl2.SDL_RENDERER_PRESENTVSYNC)
		self.surface = sdl2.SDL_CreateRGBSurface(0,WIN_WIDTH,WIN_HEIGHT,32,0,0,0,0)

	def run(self):
		lastFpsCalcTime = 0
		frames = 0

		running = True
		while running:
			events = sdl2.ext.get_events()
			for event in events:
				if event.type == sdl2.SDL_QUIT or (event.type == sdl2.SDL_KEYDOWN and event.key.keysym.sym == sdl2.SDLK_ESCAPE):
					running = False
					break

			keystate = sdl2.SDL_GetKeyboardState(None)
			if keystate[sdl2.SDL_SCANCODE_LEFT]:
				print("left")
			elif keystate[sdl2.SDL_SCANCODE_RIGHT]:
				print("right")
			elif keystate[sdl2.SDL_SCANCODE_UP]:
				print("accelerate")
			elif keystate[sdl2.SDL_SCANCODE_DOWN]:
				print("brake")

			self.draw()

			# Calculate FPS
			frames = frames + 1
			if time.time() - lastFpsCalcTime > 1:
				fps = frames/(time.time() - lastFpsCalcTime)
				print(int(fps))
				frames = 0
				lastFpsCalcTime = time.time()

		return 0

	def draw(self):
		self.drawRoad()
		self.drawCar()
		sdl2.SDL_RenderPresent(self.renderer)

	def drawRoad(self):
		# Sky
		sdl2.SDL_SetRenderDrawColor(self.renderer, SKY_COLOR[0], SKY_COLOR[1], SKY_COLOR[2], sdl2.SDL_ALPHA_OPAQUE)
		sdl2.SDL_RenderClear(self.renderer)
		# Floor
		sdl2.SDL_SetRenderDrawColor(self.renderer, FLOOR_COLOR[0], FLOOR_COLOR[1], FLOOR_COLOR[2], sdl2.SDL_ALPHA_OPAQUE)
		sdl2.SDL_RenderFillRect(self.renderer, sdl2.SDL_Rect(0, int(WIN_HEIGHT/2), WIN_WIDTH, int(WIN_HEIGHT)))

	def drawCar(self):
		return


if __name__ == '__main__':
	try:
		main = Main()
		main.run()
	except KeyboardInterrupt:
		exit(0)
