import pygame

class Fighter:
    def __init__ (self, player, x, y, flip, character_idle, character_running, character_attacking, character_hurt, character_dead, heart_list, slash_fx, type):
        # Fighter data
        self.rect = pygame.Rect((x, y, 70, 40))
        self.flip = False
        self.attack_cooldown = 0
        self.attack_aim = 50
        self.hp = 3
        self.heart_list = heart_list
        self.current_hp = self.heart_list[2]
        self.flip = flip
        self.player = player
        self.type = type
        
        # Fighter sound effects
        self.slash_fx = slash_fx

        # Fighter image
        self.character_idle = character_idle
        self.character_running = character_running
        self.character_attacking = character_attacking
        self.character_hurt = character_hurt
        self.character_dead = character_dead
        self.current_sprite = 0
        self.image = self.character_idle[self.current_sprite]
        self.scale = 2.2

        # Fighter actions
        self.idle = True
        self.attacking = False
        self.running = False
        self.hurt = False
        self.hit = False
        self.alive = True
    
    def move(self, screen_width, screen_height, surface, target, round_over):
        SPEED = 5
        move_x = 0
        move_y = 0

        key = pygame.key.get_pressed()
    
        self.running = False

        if self.player == 1:
            if self.attacking == False and self.alive and round_over == False:
            # Playyer 1 Movement
                if key[pygame.K_a]:
                    move_x = -SPEED
                    self.running = True
                elif key[pygame.K_d]:
                    move_x = SPEED
                    self.running = True
                elif key[pygame.K_w]:
                    move_y = -SPEED
                    self.running = True
                elif key[pygame.K_s]:
                    move_y = SPEED
                    self.running = True
            
            # Attack
            if key[pygame.K_r] and self.alive:
                self.attack(surface, target)

        if self.player == 2:
            # Playyer 2 Movement
            if self.attacking == False and self.alive and round_over == False:
                if key[pygame.K_LEFT]:
                    move_x = -SPEED
                    self.running = True
                elif key[pygame.K_RIGHT]:
                    move_x = SPEED
                    self.running = True
                elif key[pygame.K_UP]:
                    move_y = -SPEED
                    self.running = True
                elif key[pygame.K_DOWN]:
                    move_y = SPEED
                    self.running = True
            
            # Attack
            if key[pygame.K_p] and self.alive:
                self.attack(surface, target)
           
        # Corners
        if self.rect.right + move_x > screen_width:
            move_x = screen_width - self.rect.right
        elif self.rect.left + move_x < 0:
            move_x = 0 - self.rect.left
        elif self.rect.top + move_y < 170:
            move_y = 170 - self.rect.top
        elif self.rect.bottom + move_y > 480:
            move_y = 480 - self.rect.bottom

        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True

        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
            self.hit = False

        self.rect.x += move_x
        self.rect.y += move_y

    def update(self, target):
        self.current_sprite += 1

        if not self.alive:
            # Death animation
            if self.current_sprite >= len(self.character_dead):
                self.current_sprite = len(self.character_dead) - 1
            self.image = self.character_dead[self.current_sprite]

        elif self.attacking:
            if self.current_sprite >= len(self.character_attacking):
                self.attacking = False
                self.idle = True
                self.current_sprite = 0
            self.image = self.character_attacking[self.current_sprite]
            self.attack_cooldown = 50

        elif self.hurt:
            if self.current_sprite >= len(self.character_hurt):
                self.current_sprite = 0
                self.hurt = False
            self.image = self.character_hurt[self.current_sprite]

        elif self.running:
            self.update_action(self.character_running)
            self.image = self.character_running[self.current_sprite]

        elif self.idle:
            self.update_action(self.character_idle)
            self.image = self.character_idle[self.current_sprite]

        # Update player health
        if target.hp == 2:
            target.current_hp = target.heart_list[1]
        elif target.hp == 1:
            target.current_hp = target.heart_list[0]

    # Updates sprite action animation
    def update_action(self, action_list):
        if self.current_sprite >= len(action_list):
            self.current_sprite = 0

        
    def attack(self, surface, target):
        if self.attack_cooldown == 0:
            self.attacking = True
            self.slash_fx.play()
            attack_rect = pygame.Rect(self.rect.centerx - (1 * self.rect.width * self.flip), self.rect.y , 1 * self.rect.width,  self.rect.height)
            # pygame.draw.rect(surface, (0, 255, 0), attack_rect)

            # If player hits another player
            if attack_rect.colliderect(target.rect):
                if not self.hit:
                    self.hit = True
                    target.hp -= 1
                    target.hurt = True

                if target.hp <= 0:
                    target.alive = False

    def draw(self, surface):
        # pygame.draw.rect(surface, (255, 0, 0), self.rect)
        flipped_img = pygame.transform.flip(self.image, self.flip, False)
        if self.type == "Golem" or self.type == "Satyr":
            scaled_img = pygame.transform.scale(flipped_img, (self.rect.width * self.scale, (self.rect.height + 40) * self.scale))
        elif self.type == "Mino":
            scaled_img = pygame.transform.scale(flipped_img, (self.rect.width * self.scale, (self.rect.height + 30) * self.scale))

        surface.blit(scaled_img , (self.rect.x - 40, self.rect.y - 80) )



