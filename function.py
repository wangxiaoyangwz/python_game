from pygame.locals import *
pygame.init()
windows原点在左上

screen=pygame.display.set_mode((宽，高))
myfont=pygame.font.Font(字体，字体大小)
文本渲染到图像上
myfont=pygame.font .Font(None,60)
textImage=myfont.render(文本消息，（抗锯齿字体），颜色)
screen.blit(textImage,position)
pygame.draw.circal(screen,color,position,radius,width)
pygame.display.set_caption()当前窗口名
pygame.draw.line(screen,color,(起始位置坐标),(结束位置坐标),width)
random.randint(a, b)
Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
pygame.event.get()创建等待处理的事件的列表
for event in pygame.event.get():遍历列表
典型的事件：按键按下、释放，鼠标移动、QUIT-->窗口关闭时
响应退出键
while True:
	for event in pygame.event.get():
		if event.type==QUIT：
		    sys.exit()
		elif event.type==KEYDOWN:
			if enent.type ==pygame.K_ESCAPE:
				sys.exit()

MOUSEMOTION
for event in pygame.event.get():
	if event.type==MOUSEMOTION:
		mouse_x,mouse_y=event.pos
		move_x,move_y=event.rel


MOUSEBUTTONUP MOUSEBUTTONDOWN
for event in pygame.event.get():
	elif event.type==MOUSEBUTTONDOWN:
		mouse_down=event.button
		mouse_down_x,mouse_down_y=event.pos
	elif event.type==MOUSEBUTTONUP:
		mouse_up=event.button
		mouse_up_x,mouse_up_y=event.pos

key=pygame.key.get_pressed()
if keys[K_ESCAPE]:
	sys.exit()

pygame.mouse.get_pos()返回鼠标当前位置x,y
pos_x,pos_y=pygame.mouse.get_pos()

pygame.mouse.get_rel()鼠标移动的相对移动
rel_x,rel_y=pygame.mouse.get_rel()

pygame.mouse.get_pressed()读取鼠标按钮，返回按钮状态的数组
button1,button2,button3=pygame.mouse.get_pressed()


math.degrees()
math.radians()

RTS(实时策略)让物体移动到想让他到达的位置

计算子弹等的方向

math.cos()弧度为参数，使用角度，转换即可
x=math.cos(math.radians(90))

datetime.today()获得当前的日期和时间





