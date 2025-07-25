import random
import numpy as np
from constants import *

class gameObject:
    def __init__(self, img_id, position, velocity, acceleration):
        self.img_id = img_id
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.ticks = 0

    def get_img_id(self):
        return self.img_id

    def get_position(self):
        return self.position

    def get_velocity(self):
        return self.velocity

    def get_acceleration(self):
        return self.acceleration

    def set_img_id(self, new_img_id):
        self.img_id = new_img_id

    def set_position(self, new_position):
        self.position = new_position

    def set_velocity(self, new_velocity):
        self.velocity = new_velocity

    def set_acceleration(self, new_acceleration):
        self.acceleration = new_acceleration

    def update_position(self, targets):
        self.position += self.velocity + random.random() * (random.randint(-1, 1))
        self.velocity += self.acceleration + random.random() * (random.randint(-1, 1))
        self.ticks += 1

        if self.ticks == 20:
            self.ticks = 0
            target = self.position
            min_dist = float('inf')

            for target_obj in targets:
                if target_obj.get_img_id() == WIN_RULES[self.img_id]:
                    dist = np.sum((target_obj.get_position() - self.position) ** 2)
                    if dist < min_dist:
                        min_dist = dist
                        target = target_obj.get_position()

            if np.array_equal(target, self.position):
                target = np.array([random.randint(WINDOW_WIDTH // 5, 4 * WINDOW_WIDTH // 5),
                                   random.randint(WINDOW_HEIGHT // 5, 4 * WINDOW_HEIGHT // 5)], dtype=np.float64)

            vector = target - self.position
            self.acceleration = MAX_ACCEL * vector / np.array([WINDOW_WIDTH, WINDOW_HEIGHT], dtype=np.float64)

        self.position = self.trim(self.position, [4 * WINDOW_WIDTH / 5, 4 * WINDOW_HEIGHT / 5], [WINDOW_WIDTH / 5, WINDOW_HEIGHT / 5])
        self.velocity = self.trim(self.velocity, [MAX_VEL, MAX_VEL], [-MAX_VEL, -MAX_VEL])
        self.acceleration = self.trim(self.acceleration, [MAX_ACCEL, MAX_ACCEL], [-MAX_ACCEL, -MAX_ACCEL])

    def update_img_id(self):
        self.img_id = (self.img_id + 1) % 3

    @staticmethod
    def trim(vector, upper, lower):
        return np.clip(vector, lower, upper)
