import random
import numpy as np
from constants import *
from objects import gameObject

class gamePlay:
    def __init__(self):
        self.objects = []

    def fill_objects(self):
        for img_id in range(3):
            for _ in range(20):
                position = np.array([random.randint(WINDOW_WIDTH // 5, 4 * WINDOW_WIDTH // 5),
                                     random.randint(WINDOW_HEIGHT // 5, 4 * WINDOW_HEIGHT // 5)], dtype=np.float64)
                velocity = np.array([random.randint(-MAX_VEL, MAX_VEL), 
                                     random.randint(-MAX_VEL, MAX_VEL)], dtype=np.float64)
                acceleration = np.array([random.randint(-MAX_ACCEL, MAX_ACCEL), 
                                         random.randint(-MAX_ACCEL, MAX_ACCEL)], dtype=np.float64)
                self.objects.append(gameObject(img_id, position, velocity, acceleration))
        random.shuffle(self.objects)

    def clear_objects(self):
        self.objects = []

    def draw_objects(self):
        for obj in self.objects:
            DISPLAYSURF.blit(CHOICES[obj.get_img_id()], obj.get_position())

    def draw_text(self):
        counts = [0, 0, 0]
        for obj in self.objects:
            counts[obj.get_img_id()] += 1
        result_text = f'Rock: {counts[0]} Paper: {counts[1]} Scissors: {counts[2]}'
        DISPLAYSURF.blit(FONT.render(result_text, True, WHITE), (15, WINDOW_HEIGHT - 30))

    def check_collisions(self):
        for i in range(len(self.objects)):
            for j in range(i + 1, len(self.objects)):
                obj1, obj2 = self.objects[i], self.objects[j]
                if obj1.get_img_id() == obj2.get_img_id():
                    continue

                pos1, pos2 = obj1.get_position(), obj2.get_position()
                dist = np.sum((pos1 - pos2) ** 2)
                if dist < (RADIUS * 2) ** 2:
                    if obj1.get_img_id() < obj2.get_img_id():
                        if obj1.get_img_id() == 0 and obj2.get_img_id() == 2:
                            obj2.update_img_id()
                        else:
                            obj1.update_img_id()
                    else:
                        if obj1.get_img_id() == 2 and obj2.get_img_id() == 0:
                            obj1.update_img_id()
                        else:
                            obj2.update_img_id()
                    SOUND_COLLIDE.play()

    def update(self, ticks):
        if ticks >= 150:
            DISPLAYSURF.fill(BLACK)
            self.draw_objects()
            for obj in self.objects:
                obj.update_position(self.objects)
            self.check_collisions()
        elif ticks < 120:
            if ticks % 2 == 0:
                obj = self.objects[ticks // 2]
                DISPLAYSURF.blit(CHOICES[obj.get_img_id()], obj.get_position())
                SOUND_APPEAR.play()
