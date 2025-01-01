import random
import numpy as np

class Ball:
    def __init__(self, position, velocity):
        self.positions = np.array(position, dtype=np.float64)
        self.radius = random.random() + 4.5
        self.velocity = np.array(velocity, dtype=np.float64)
        self.elastic = random.randint(70, 100) / 100
        self.mass = 150 + self.radius * 50
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.inside = True

    def get_positions(self):
        return self.positions
    
    def get_radius(self):
        return self.radius
    
    def get_velocity(self):
        return self.velocity
    
    def get_elastic(self):
        return self.elastic
    
    def get_mass(self):
        return self.mass
    
    def get_color(self):
        return self.color
    
    def get_state(self):
        return self.inside

    def set_positions(self, new_positions):
        self.positions = np.array(new_positions, dtype=np.float64)
    
    def set_velocity(self, new_velocity):
        self.velocity = np.array(new_velocity, dtype=np.float64)
    
    def set_state(self, new_state):
        self.inside = new_state
