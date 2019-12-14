import pygame
pygame.font.init()

def getWelcomeText():
    myfont1 = pygame.font.SysFont('华文宋体', 50)
    #print(pygame.font.get_fonts()) #获取系统字体名称列表
    # myfont1 = pygame.font.Font('simkai.ttf',50)
    ksyx = myfont1.render('开始游戏', True, (0, 0, 0))
    ksyx1 = myfont1.render('开始游戏', True, (255, 0, 0))
    yxsm = myfont1.render('游戏说明', True, (0, 0, 0))
    yxsm1 = myfont1.render('游戏说明', True, (255, 0, 0))
    gyzz = myfont1.render('关于作者', True, (0, 0, 0))
    gyzz1 = myfont1.render('关于作者', True, (255, 0, 0))
    tcyx = myfont1.render('退出游戏', True, (0, 0, 0))
    tcyx1 = myfont1.render('退出游戏', True, (255, 0, 0))

    myfont2 = pygame.font.SysFont('Curlz', 200)
    title = myfont2.render('Adaptation', True, (116, 0, 161))
    return (title, ksyx, ksyx1, yxsm, yxsm1, gyzz, gyzz1, tcyx, tcyx1)
    

def getAuthorText():
    myfont1 = pygame.font.SysFont('华文宋体', 50)
    back = myfont1.render('返回', True, (0, 0, 0))
    back1 = myfont1.render('返回', True, (255, 0, 0))

    myfont2 = pygame.font.SysFont('幼圆', 30)
    hmc = myfont2.render('侯牧村 2016xxxxxxxxx', True, (0, 0, 0))
    lcr = myfont2.render('李宬睿 2016141021030', True, (0, 0, 0))
    htq = myfont2.render('何天其 2016yyyyyyyyy', True, (0, 0, 0))
    wsn = myfont2.render('王胜男 2016zzzzzzzzz', True, (0, 0, 0))
    jby = myfont2.render('焦炳祎 2016wwwwwwwww', True, (0, 0, 0))
    return (hmc, lcr, htq, wsn, jby, back, back1)

def getIntroText():
    myfont1 = pygame.font.SysFont('方正粗活意简体', 50)
    back = myfont1.render('返回', True, (0, 0, 0))
    back1 = myfont1.render('返回', True, (255, 0, 0))

    myfont2 = pygame.font.SysFont('幼圆', 30)
    intro = myfont2.render('这是游戏玩法的介绍……其中要手动换行', True, (0, 0, 0))
    return (intro, back, back1)

def getGameText():
    myfont1 = pygame.font.SysFont('方正粗活意简体', 50)
    back = myfont1.render('返回', True, (0, 0, 0))
    back1 = myfont1.render('返回', True, (255, 0, 0))

    myfont2 = pygame.font.SysFont('幼圆', 30)
    intro = myfont2.render('这是游戏玩法的介绍……其中要手动换行', True, (0, 0, 0))
    return (intro, back, back1)