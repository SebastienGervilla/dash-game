from Objects.UI.game_button import GameButton

class QuitButton(GameButton):

    def __init__(self, pos: tuple, size: tuple, image_name: str, button_name: str):
        super().__init__(pos, size, image_name, button_name)