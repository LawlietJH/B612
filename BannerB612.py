# -*- coding: utf-8 -*-
# Página 1: http://www.kammerl.de/ascii/AsciiSignature.php
# Página 2: http://patorjk.com/software/taag
#
# Añadir una 'r' (significado de 'raw' = 'crudo') antes de una cadena,
# al imprimir en pantalla tomará la cadena tal cual como esta escrita
# ignorando los \n \t etc... 

import random

Banner1 = r"""
                         ██████╗  ██████╗ ██╗██████╗ 
                         ██╔══██╗██╔════╝███║╚════██╗
                         ██████╔╝███████╗╚██║ █████╔╝
                         ██╔══██╗██╔═══██╗██║██╔═══╝ 
                         ██████╔╝╚██████╔╝██║███████╗
                         ╚═════╝  ╚═════╝ ╚═╝╚══════╝
"""
#(Font: 'ANSI shadow' - Desde: http://patorjk.com/software/taag)


Banner2 = """
 ==============================================================================
 ===================      =====       ======  ========   ======================
 ===================  ===  ===  =====  ====   ======   =   ====================
 ===================  ====  ==  ============  =====   ===   ===================
 ===================  ===  ===       =======  ==========   ====================
 ===================      ====   ===  ======  =========   =====================
 ===================  ===  ===  =====  =====  ========   ======================
 ===================  ====  ==  =====  =====  =======   =======================
 ===================  ===  ====  ===   =====  ======   ========================
 ===================      ======     =====      ===        ====================
 ==============================================================================

"""
#(Font: 'rev')


Banner3 = """
                    oooooooooo.      .ooo     .o    .oooo.  
                    `888'   `Y8b   .88'     o888  .dP""Y88b 
                     888     888  d88'       888        ]8P'
                     888oooo888' d888P"Ybo.  888      .d8P' 
                     888    `88b Y88[   ]88  888    .dP'    
                     888    .88P `Y88   88P  888  .oP     .o
                    o888bood8P'   `88bod8'  o888o 8888888888
"""
#(Font: 'Roman')


Banner4 = """
                    oooooooooo    ooooooo    oo    ooooooo  
                     888    888 o88        o888  o88     888
                     888oooo88  888888888o  888        o888 
                     888    888 88o    o888 888     o888   o
                    o888ooo888    88ooo88  o888o o8888oooo88
"""
#(Font: 'o8')


Banner5 = """
                   _______     .------.     ,---.    .`````-.   
                  \  ____  \  /  .-.   \   /_   |   /   ,-.  \  
                  | |    \ | /  /   `--'     ,_ |  (___/  |   | 
                  | |____/ / |  .----.   ,-./  )|        .'  /  
                  |   _ _ '. |   _ _  '. \  '_ '`)   _.-'_.-'   
                  |  ( ' )  \|  ( ' )   \ > (_)  ) _/_  .'      
                  | (_{;}_) || (_{;}_)  |(  .  .-'( ' )(__..--. 
                  |  (_,_)  /\  (_,_)  /  `-'`-'|(_{;}_)      | 
                  /_______.'  `...__..'     '---' (_,_)-------' 
"""
#(Font: 'Flower Power' - http://patorjk.com/software/taag/#p=display&f=Flower%20Power&t=B612)



def Banner():
	
    Banners = [ Banner1, Banner2, Banner3, Banner4, Banner5 ]
    
    return random.choice(Banners)

