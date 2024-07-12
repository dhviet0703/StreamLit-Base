from os.path import join, dirname


class Config:
    IMAGE_AVATAR = join(dirname(dirname(__file__)), '../template/avatar_web.jpg')


cfg = Config()
