from tank_war import TankWar
from settings import Settings

if __name__ == '__main__':
    settings = Settings()
    tankWar = TankWar(settings)
    tankWar.run_game()
