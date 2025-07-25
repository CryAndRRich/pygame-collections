import math
import random
import numpy as np
import pygame
from balls import Ball

class gamePlay:
    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height

        self.circle_center = np.array([window_width / 2, window_height / 2], dtype=np.float64)
        self.circle_radius = 150

        self.gravity = 0.2
        self.spinning_speed = 0.01
        self.arc_mass = 1_000_000_000

        self.arc_deg = 60
        self.start_angle = math.radians(-self.arc_deg / 2)
        self.end_angle = math.radians(self.arc_deg / 2)

        self.ball_velocity = np.array([0, 0], dtype=np.float64)
        self.balls = [Ball([window_width // 2, window_height // 2 - 120], self.ball_velocity)]

    def draw(self, DISPLAYSURF):
        p1 = self.circle_center + (self.circle_radius + 1000) * np.array([math.cos(self.start_angle), math.sin(self.start_angle)])
        p2 = self.circle_center + (self.circle_radius + 1000) * np.array([math.cos(self.end_angle), math.sin(self.end_angle)])
        pygame.draw.polygon(DISPLAYSURF, (0, 0, 0), [self.circle_center, p1, p2], 0)

        for ball in self.balls:
            pygame.draw.circle(DISPLAYSURF, ball.get_color(), ball.get_positions(), ball.get_radius())

    def check_inside(self, ball_pos):
        dx = ball_pos[0] - self.circle_center[0]
        dy = ball_pos[1] - self.circle_center[1]
        ball_angle = math.atan2(dy, dx)

        self.end_angle %= (2 * math.pi)
        self.start_angle %= (2 * math.pi)

        if self.start_angle > self.end_angle:
            self.end_angle += 2 * math.pi

        return (self.start_angle <= ball_angle <= self.end_angle) or (self.start_angle <= ball_angle + 2 * math.pi <= self.end_angle)

    def check_ball_collides_arc(self):
        for ball in self.balls:
            if (ball.get_positions()[1] > self.window_height or ball.get_positions()[0] < 0 or
                    ball.get_positions()[0] > self.window_width or ball.get_positions()[1] < 0):
                self.balls.remove(ball)
                self.balls.append(Ball([self.window_width // 2, self.window_height // 2 - 120],
                                       [random.uniform(-4, 4), random.uniform(-1, 1)]))
                if len(self.balls) < 40:
                    self.balls.append(Ball([self.window_width // 2, self.window_height // 2 - 120],
                                           [random.uniform(-4, 4), random.uniform(-1, 1)]))

            velocity = ball.get_velocity()
            velocity[1] += self.gravity
            ball.set_velocity(velocity)
            ball.set_positions(ball.get_positions() + ball.get_velocity())

            dist = np.linalg.norm(ball.get_positions() - self.circle_center)
            if dist + ball.get_radius() > self.circle_radius:
                if self.check_inside(ball.get_positions()):
                    ball.set_state(False)

                if ball.get_state():
                    normal = ball.get_positions() - self.circle_center
                    normal = normal / np.linalg.norm(normal)
                    spinning_velocity = np.dot(ball.get_velocity(), normal)
                    ball.set_positions(self.circle_center + (self.circle_radius - ball.get_radius()) * normal)
                    new_velocity = (ball.get_velocity() * (ball.get_mass() - self.arc_mass)) / (ball.get_mass() + self.arc_mass)
                    new_velocity += spinning_velocity * self.spinning_speed
                    new_velocity *= ball.get_elastic()
                    ball.set_velocity(new_velocity)

    def check_ball_collides_ball(self):
        for i in range(len(self.balls)):
            for j in range(i + 1, len(self.balls)):
                ball1 = self.balls[i]
                ball2 = self.balls[j]
                dist = np.linalg.norm(ball1.get_positions() - ball2.get_positions())
                if dist <= ball1.get_radius() + ball2.get_radius():
                    normal = ball2.get_positions() - ball1.get_positions()
                    normal = normal / np.linalg.norm(normal)

                    relative_velocity = np.dot(ball2.get_velocity() - ball1.get_velocity(), normal)

                    if relative_velocity > 0:
                        restitution = 0.1
                        impulse = -(1 + restitution) * relative_velocity / (1 / ball1.get_mass() + 1 / ball2.get_mass())

                        ball1.set_velocity(ball1.get_velocity() + impulse * normal / ball1.get_mass())
                        ball2.set_velocity(ball2.get_velocity() - impulse * normal / ball2.get_mass())
                        ball1.set_velocity(ball1.get_velocity() * ball1.get_elastic())
                        ball2.set_velocity(ball2.get_velocity() * ball2.get_elastic())

    def check_collisions(self):
        self.check_ball_collides_arc()
        self.check_ball_collides_ball()
