import pygame   # pip install pygame
import neat     # pip install neat-python
import time
import os
import random

pygame.font.init()

WINDOW_SIZE = (288, 512)
FRAME_RATE = 30

BIRD_IMAGES = [
    #pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))),
    pygame.image.load(os.path.join('imgs', 'bird1.png')),
    pygame.image.load(os.path.join('imgs', 'bird2.png')),
    pygame.image.load(os.path.join('imgs', 'bird3.png'))
]

PIPE_IMAGE = pygame.image.load(os.path.join('imgs', 'pipe.png'))
GROUND_IMAGE = pygame.image.load(os.path.join('imgs', 'base.png'))
BG_IMAGE = pygame.image.load(os.path.join('imgs', 'bg.png'))

SCORE_FONT = pygame.font.SysFont('Arial', 20)

GEN = 0

class Bird:
    SPRITES = BIRD_IMAGES
    MAX_ROTATION_ANLE = 30
    ROTATION_VELOCITY = 20
    ANIMATION_TIME = 5

    JUMP_HEIGHT = 7
    GRAVITY = 1.2

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.velocity = 0
        self.height = self.y
        self.image_count = 0
        self.image = self.SPRITES[0]

    def jump(self):
        self.velocity = -self.JUMP_HEIGHT
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1

        d = self.velocity * self.tick_count + self.GRAVITY * self.tick_count ** 2

        if d >= 16:
            d = 16
        elif d < 0:
            d -= 2

        self.y = self.y + d

        '''
        if d < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION_ANLE:
                self.tilt = self.MAX_ROTATION_ANLE
        else:
            if self.tilt > -90:
                self.tilt -= self.ROTATION_VELOCITY
        '''
        
    def draw(self, window):
        self.image_count += 1

        if self.image_count < self.ANIMATION_TIME:
            self.image = self.SPRITES[0]
        elif self.image_count < self.ANIMATION_TIME * 2:
            self.image = self.SPRITES[1]
        elif self.image_count < self.ANIMATION_TIME * 3:
            self.image = self.SPRITES[2]
        elif self.image_count < self.ANIMATION_TIME * 4:
            self.image = self.SPRITES[1]
        elif self.image_count < self.ANIMATION_TIME * 4 + 1:
            self.image = self.SPRITES[0]
            self.image_count = 0

        if self.tilt <= -80:
            self.image = self.SPRITES[1]
            self.image_count = self.ANIMATION_TIME * 2

        rotated_image = pygame.transform.rotate(self.image, self.tilt)
        c = self.image.get_rect(topleft = (self.x, self.y)).center
        new_rect = rotated_image.get_rect(center = c)
        window.blit(rotated_image, new_rect.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.image)


class Pipe:
    GAP = 100
    VELOCITY = 5

    def __init__(self, x):
        self.x = x
        self.height = 0

        self.top = 0
        self.bottom = 0
        self.PIPE_TOP = pygame.transform.flip(PIPE_IMAGE, False, True)
        self.PIPE_BOTTOM = PIPE_IMAGE

        self.passed = False
        self.setHeight()


    def setHeight(self):
        mid_Y = WINDOW_SIZE[1] * 0.5 - 100
        offset = 50

        self.height = random.randrange(mid_Y - offset, mid_Y + offset)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.GAP

    def move(self):
        self.x -= self.VELOCITY

    def draw(self, window):
        window.blit(self.PIPE_TOP, (self.x, self.top))
        window.blit(self.PIPE_BOTTOM, (self.x, self.bottom))

    def collide(self, bird):
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)
        
        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        t_point = bird_mask.overlap(top_mask, top_offset)
        b_point = bird_mask.overlap(bottom_mask, bottom_offset)

        if t_point or b_point:
            return True

        return False

class Ground:
    VELOCITY = 5
    WIDTH = GROUND_IMAGE.get_width()
    IMAGE = GROUND_IMAGE

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH

    def move(self):
        self.x1 -= self.VELOCITY
        self.x2 -= self.VELOCITY

        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH
        
        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    def draw(self, window):
        window.blit(self.IMAGE, (self.x1, self.y))
        window.blit(self.IMAGE, (self.x2, self.y))

def draw_window(window, birds, pipes, ground, score, gen):
    window.blit(BG_IMAGE, (0, 0))

    for p in pipes:
        p.draw(window)

    score_text = SCORE_FONT.render(f'Score: {score}', 1, (255, 255, 255))
    score_position = (WINDOW_SIZE[0] * 0.5 - score_text.get_width() * 0.5, score_text.get_height() * 0.5)
    window.blit(score_text, score_position)

    gen_text = SCORE_FONT.render(f'Gen: {gen}', 1, (255, 255, 255))
    pos = (WINDOW_SIZE[0] * 0.5 - gen_text.get_width() * 0.5, gen_text.get_height() + 10)
    window.blit(gen_text, pos)

    ground.draw(window)

    for b in birds:
        b.draw(window)

    pygame.display.update()

def main(genomes, config):
    global GEN
    GEN += 1
    
    nets = []
    ge = []
    birds = []

    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        birds.append(Bird(100, 250))
        g.fitness = 0
        ge.append(g)

    window = pygame.display.set_mode(WINDOW_SIZE)
    clock = pygame.time.Clock()
    
    ground_Y = WINDOW_SIZE[1] - GROUND_IMAGE.get_height()

    score = 0
    #bird = Bird(100, 250)

    ground = Ground(ground_Y)
    pipes = [Pipe(WINDOW_SIZE[0])]
    
    '''
    for i in range(3):
        x = WINDOW_SIZE[0] + i * 120
        p = Pipe(x)
        pipes.append(p)
    '''

    isRunning = True
    while isRunning:

        clock.tick(FRAME_RATE)
        flag = False

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                isRunning = False
                pygame.quit()
                quit()
            
            #if e.type == pygame.KEYDOWN:
            #    if e.key == pygame.K_SPACE:
            #        bird.jump()

        pipe_index = 0
        if len(birds) > 0:
            if len(pipes) > 1 and birds[0].x > pipes[0].x + pipes[0].PIPE_TOP.get_width():
                pipe_index = 1
        else:
            isRunning = False
            break

        for i, b in enumerate(birds):
            b.move()
            ge[i].fitness += 0.1

            d1 = abs(b.y - pipes[pipe_index].height)
            d2 = abs(b.y - pipes[pipe_index].bottom)
            output = nets[i].activate((b.y, d1, d2))

            if output[0] > 0.5:
                b.jump()


        pipes_remove = []

        for i, b in enumerate(birds):
            if b.y + b.image.get_height() >= ground_Y or b.y < 0:
                birds.pop(i)
                nets.pop(i)
                ge.pop(i)

        for p in pipes:
            for i, b in enumerate(birds):
                if p.collide(b):
                    ge[i].fitness -= 1
                    birds.pop(i)
                    nets.pop(i)
                    ge.pop(i)
                
                if not p.passed and p.x < b.x:
                    p.passed = True
                    flag = True
            
            if p.x + p.PIPE_BOTTOM.get_width() < 0:
                #p.x = WINDOW_SIZE[0]
                #p.setHeight()
                #p.passed = False
                pipes_remove.append(p)

            p.move()
        
        for p in pipes_remove:
            pipes.remove(p)

        if flag:
            score += 1
            #x = WINDOW_SIZE[0] + i * 120
            p = Pipe(WINDOW_SIZE[0])
            pipes.append(p)
            
            for g in ge:
                g.fitness += 5

        #for p in pipes_remove:
            

        ground.move()
        draw_window(window, birds, pipes, ground, score, GEN)



def run():
    #local_path = os.path.dirname(__file__)
    config_path = 'config-feedforward.txt'
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)
    
    p = neat.population.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(main, 50)

if __name__ == "__main__":
    run()
    #main()