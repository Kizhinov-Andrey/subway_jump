from constants import *


class BlockBorder(pygame.sprite.Sprite):
    """Граница для блока"""

    def __init__(self, x1, y1, x2, y2, block):
        super().__init__()
        if x1 == x2:  # вертикальная стенка
            self.image = pygame.Surface((3, y2 - y1))
            self.rect = pygame.Rect(x1, y1, 3, y2 - y1)
        else:  # горизонтальная стенка
            self.image = pygame.Surface((x2 - x1, 3))
            self.rect = pygame.Rect(x1, y1, x2 - x1, 3)
        self.x = x1
        self.y = y1
        self.block = block  # Блок которому принадлежит стенка

    def get_block(self):
        return self.block

    def update(self, x_off_cet, y_off_cet):
        self.rect.x = self.x - x_off_cet
        self.rect.y = self.y - y_off_cet


class StandardBlock(pygame.sprite.Sprite):
    """Абстрактный класс блока"""
    BLOCK_SIZE = 50  # Размер одного блока

    def __init__(self, pos):
        super().__init__()
        self.rect = pygame.rect.Rect(pos[0], pos[1], StandardBlock.BLOCK_SIZE, StandardBlock.BLOCK_SIZE)
        self.x = pos[0]
        self.y = pos[1]

    def update(self, x_off_cet):
        self.rect.x = self.x - x_off_cet


class SnowPlatform(StandardBlock):
    """Обычная платформа на которой может находиться герой"""
    IMAGE = pygame.image.load(r"..\Images\standard_platform.png")

    def __init__(self, pos):
        super().__init__(pos)
        self.image = self.IMAGE
        # Добавляем верхнюю границу для блока
        self.top_border = pygame.sprite.GroupSingle()
        self.top_border.add(BlockBorder(self.x, self.y - 1, self.x + StandardBlock.BLOCK_SIZE, self.y, self))

    def get_top_border(self):
        return self.top_border

    def update(self, x_off_cet):
        super(SnowPlatform, self).update(x_off_cet)
        self.top_border.update(x_off_cet, 0)


class Ground(StandardBlock):
    """Класс земли которого нельзя касаться"""
    IMAGE = pygame.image.load(r"..\Images\ground.jpg")

    def __init__(self, pos):
        super().__init__(pos)
        self.image = self.IMAGE
