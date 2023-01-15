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

RENDER_WIDTH = 128
RENDER_HEIGHT = 96
RENDER_SCALE = 8
WIN_WIDTH = RENDER_WIDTH * RENDER_SCALE
WIN_HEIGHT = RENDER_HEIGHT * RENDER_SCALE

SKY_COLOR = [0,127,255]
GRASS_COLOR = [0,127,0]
KERB_COLOR = [255,0,0]
ROAD_COLOR = [127,127,127]
KERB_WIDTH = 0.05

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
		sdl2.SDL_SetRenderDrawColor(self.renderer, ROAD_COLOR[0], ROAD_COLOR[1], ROAD_COLOR[2], sdl2.SDL_ALPHA_OPAQUE)
		sdl2.SDL_RenderFillRect(self.renderer, sdl2.SDL_Rect(0, int(WIN_HEIGHT/2), WIN_WIDTH, int(WIN_HEIGHT)))

		# Draw road
		for y in range(int(RENDER_HEIGHT/2), RENDER_HEIGHT):
			perspectiveMult = (y - RENDER_HEIGHT / 2) / (RENDER_HEIGHT / 2) * 0.8 + 0.2 # Range 0.2 - 1.0
			roadWidth = 0.6
			roadWidthPixels = roadWidth * RENDER_WIDTH * perspectiveMult
			roadCenterPixels = (RENDER_WIDTH - roadWidth) / 2
			kerbWidth = KERB_WIDTH * RENDER_WIDTH * perspectiveMult

			sdl2.SDL_SetRenderDrawColor(self.renderer, KERB_COLOR[0], KERB_COLOR[1], KERB_COLOR[2], sdl2.SDL_ALPHA_OPAQUE)
			# Left Kerb
			x = roadCenterPixels - roadWidthPixels / 2 - kerbWidth
			self.drawScaledHLine(x, y, kerbWidth)
			# Right Kerb
			x = roadCenterPixels + roadWidthPixels / 2
			self.drawScaledHLine(x, y, kerbWidth)

			sdl2.SDL_SetRenderDrawColor(self.renderer, GRASS_COLOR[0], GRASS_COLOR[1], GRASS_COLOR[2], sdl2.SDL_ALPHA_OPAQUE)
			# Left Grass
			xEnd = roadCenterPixels - roadWidthPixels / 2 - kerbWidth
			self.drawScaledHLine(0, y, xEnd) # xEnd = length, because xStart = 0
			# Right Grass
			x = roadCenterPixels + roadWidthPixels / 2 + kerbWidth
			length = RENDER_WIDTH - x
			self.drawScaledHLine(x, y, length)

	def drawCar(self):
		return

	def drawScaledHLine(self, x, y, length):
		sdl2.SDL_RenderFillRectF(self.renderer, sdl2.SDL_FRect(x * RENDER_SCALE, y * RENDER_SCALE, length * RENDER_SCALE, RENDER_SCALE))



if __name__ == '__main__':
	try:
		main = Main()
		main.run()
	except KeyboardInterrupt:
		exit(0)
