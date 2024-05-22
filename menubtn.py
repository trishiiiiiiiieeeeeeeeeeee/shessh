class Pindot:
    def __init__(self, pos, base_color, hovering_color, image=None):
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.base_color = base_color
        self.hovering_color = hovering_color
        self.image = image

    def update(self, screen):
        pass

    def check_for_input(self, position):
        pass

    def change_color(self, position):
        pass


class ImagePindot(Pindot):
    def __init__(self, image, pos, base_color, hovering_color):
        super().__init__(pos, base_color, hovering_color, image)
        if self.image is None:
            self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        screen.blit(self.image, self.rect)

    def check_for_input(self, position):
        return self.rect.collidepoint(position)


class TextPindot(Pindot):
    def __init__(self, text_input, font, pos, base_color, hovering_color):
        super().__init__(pos, base_color, hovering_color)
        self.text_input = text_input
        self.font = font
        self.text = self.font.render(self.text_input, True, self.base_color)
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        screen.blit(self.text, self.text_rect)

    def check_for_input(self, position):
        return self.text_rect.collidepoint(position)

    def change_color(self, position):
        if self.check_for_input(position):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)
