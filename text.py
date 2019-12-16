import pygame
import os

filepath = os.path.dirname(__file__)

pygame.font.init()

def getWelcomeText():
    myfont1 = pygame.font.Font(os.path.join(filepath,"fonts/FZCHYJW.ttf"), 50)
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

    myfont2 = pygame.font.Font(os.path.join(filepath,"fonts/CURLZ.ttf"), 200)
    title = myfont2.render('Adaptation', True, (116, 0, 161))
    return (title, ksyx, ksyx1, yxsm, yxsm1, gyzz, gyzz1, tcyx, tcyx1)
    

def getAuthorText():
    myfont1 = pygame.font.Font(os.path.join(filepath,"fonts/FZCHYJW.ttf"), 50)
    back = myfont1.render('返回', True, (0, 0, 0))
    back1 = myfont1.render('返回', True, (255, 0, 0))

    myfont2 = pygame.font.Font(os.path.join(filepath,"fonts/SIMYOU.ttf"), 30)
    hmc = myfont2.render('侯牧村 2016xxxxxxxxx', True, (0, 0, 0))
    lcr = myfont2.render('李宬睿 2016141021030', True, (0, 0, 0))
    htq = myfont2.render('何天其 2016yyyyyyyyy', True, (0, 0, 0))
    wsn = myfont2.render('王胜男 2016zzzzzzzzz', True, (0, 0, 0))
    jby = myfont2.render('焦炳祎 2016wwwwwwwww', True, (0, 0, 0))
    return (hmc, lcr, htq, wsn, jby, back, back1)

def getIntroText():
    myfont1 = pygame.font.Font(os.path.join(filepath,"fonts/FZCHYJW.ttf"), 50)
    back = myfont1.render('返回', True, (0, 0, 0))
    back1 = myfont1.render('返回', True, (255, 0, 0))

    myfont2 = pygame.font.Font(os.path.join(filepath,"fonts/SIMYOU.ttf"), 30)
    intro2 = myfont2.render('适者生存 不适者淘汰', True, (0, 0, 0))
    # intro2 = myfont2.render(' 这里是 Adaption', True, (0, 0, 0))
    intro3 = myfont2.render('0.开始游戏：', True, (0, 0, 0))
    intro4 = myfont2.render('  首先会选择游戏难度：', True, (0, 0, 0))
    intro5 = myfont2.render('  颜色难度：Three Color、Five Color、Seven Color；', True, (0, 0, 0))
    intro6 = myfont2.render('  速度难度：Low Speed、Middle Speed；High Speed.', True, (0, 0, 0))
    intro7 = myfont2.render('  颜色变换和速度都选择后，点击确认后开始游戏   ', True, (0, 0, 0))
    
    intro8 = myfont2.render('1.游戏操作：', True, (0, 0, 0))
    intro9 = myfont2.render('  游戏开始后重力开始作用，请注意重力翻转时间', True, (0, 0, 0))
    intro10 = myfont2.render('  点击i开始游戏，i是上，k是下，j是左，l是右', True, (0, 0, 0))
    intro11 = myfont2.render('  点击space键切换颜色，其中颜色依次变换：红橙黄绿青蓝紫', True, (0, 0, 0))
    intro12 = myfont2.render('2.障碍设置：', True, (0, 0, 0))
    intro13 = myfont2.render('  重力挑战：重力翻转时间在左上角，物体受重力作用向上向下移动', True, (0, 0, 0))
    intro14 = myfont2.render('  过膜挑战：物体经过不同颜色的膜时，需切换成相同颜色才能通过 ', True, (0, 0, 0))
    intro15 = myfont2.render('现在开始挑战吧！ ', True, (0, 0, 0))

    intro = [intro2, intro3, intro4, intro5, intro6, intro7, intro8, intro9, intro10, intro11, intro12, intro13, intro14, intro15]

    return (intro, back, back1)

def getLevelText():
    option_font = pygame.font.Font(os.path.join(filepath,"fonts/FZCHYJW.ttf"), 20)
    v3color = option_font.render("Three Color", True, (0,0,0))
    v5color = option_font.render("Five Color", True, (0,0,0))
    v7color = option_font.render("Seven Color", True, (0,0,0))
    SpeedLow = option_font.render("Low Speed", True, (0,0,0))
    SpeedMid = option_font.render("Middle Speed", True, (0,0,0))
    SpeedHig = option_font.render("High Speed", True, (0,0,0))
    gosky = option_font.render("噩梦难度", True, (0, 0, 0))

    level_title_font = pygame.font.Font(os.path.join(filepath,"fonts/ARLRDBD.ttf"), 100)
    level_title = level_title_font.render("Level Selection",True, (116, 0, 161))

    myfont1 = pygame.font.Font(os.path.join(filepath,"fonts/FZCHYJW.ttf"), 50)
    back = myfont1.render('返回', True, (0, 0, 0))
    back1 = myfont1.render('返回', True, (255, 0, 0))
    click = myfont1.render('确认', True, (0, 0, 0))
    click1 = myfont1.render('确认', True, (255, 0, 0))

    return (level_title, v3color, v5color, v7color, SpeedLow, SpeedMid, SpeedHig, gosky, back, back1, click, click1)

def getScoreText(score):
    score_text_font = pygame.font.Font(os.path.join(filepath,"fonts/FZCHYJW.ttf"), 60)
    score_text = score_text_font.render(str(score), True, (0, 0, 0))

    myfont1 = pygame.font.Font(os.path.join(filepath,"fonts/FZCHYJW.ttf"), 50)
    back = myfont1.render('返回', True, (0, 0, 0))
    back1 = myfont1.render('返回', True, (255, 0, 0))
    again = myfont1.render('重来', True, (0, 0, 0))
    again1 = myfont1.render('重来', True, (255, 0, 0))

    score_title_font = pygame.font.Font(os.path.join(filepath,"fonts/ARLRDBD.ttf"), 100)
    score_title = score_title_font.render("Your Score",True, (116, 0, 161))
    
    return (score_title, score_text, back, back1, again, again1)