from thongso import *
import os

class manhinh( ):
    def __init__ (self,scr) -> None:
        scr.geometry("{}x{}+{}+{}". format(WINDOW_WIDTH,WINDOW_HEIGHT,WINDOW_POSITION_DOWN,WINDOW_POSITION_LEFT))
        scr.iconbitmap(os.path.join(PATH_IMAGES,"1.ico" ))
        scr.title("App hỗ trợ học tập")

        #scr.state('zoomed')
        #scr['background'] = '#ffffff'

