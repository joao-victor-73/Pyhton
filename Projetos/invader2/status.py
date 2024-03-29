class GameStats():
    ''' Armazena dados estatísticos do Jogo! '''

    def __init__(self, configs):
        ''' Inicializa os dados estatísticos. '''
        self.configs = configs
        self.reset_stats()

        # Inicia o jogo em um estado inativo
        self.game_active = False

        # A pontuação máxima jamais deverá ser reiniciada
        self.max_pontuacao = 0

    def reset_stats(self):
        ''' Inicializa os dados estatísticos que podem mudar durante o jogo. '''
        self.nave_esquerda = self.configs.nave_limite

        self.pontuacao = 0
        self.level = 1
