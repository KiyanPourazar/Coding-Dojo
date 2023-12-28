class Options:
    music: bool
    ac: bool
    int_license: bool
    wheelChair_space: bool

    def __init__(self, music, ac, int_license, wheelChair_space):
        self.music = music
        self.ac = ac
        self.int_license = int_license
        self.wheelChair_space = wheelChair_space
