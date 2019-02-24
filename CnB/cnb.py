import pygame,time

pygame.init()

w,h=(800,600)
bg_color=(255,255,255)

def set_text(string,_font,_size):
	global w,h,bg_color
	
	font = pygame.font.Font(_font, _size)
	text = font.render(string, True, (0,0,0), (256,256,256))
	textRect = text.get_rect()
	textRect.center = (400, 300)
	screen.fill(bg_color)
	screen.blit(text,textRect)
	pygame.display.update()

def cb_check(guess1,number1):
	cow,bull=0,0
	done=[]
	for i in range(4):
		if(guess1[i]==number1[i]):
			bull+=1
			done.append(number1[i])

	for i in range(4):
		for j in range(4):
			if(guess1[i]==number1[j] and number1[j] not in done):
				cow+=1
	set_text("cows: "+str(cow)+" bulls: "+str(bull),'n_font.ttf',30)	
	time.sleep(2)
	if(bull==4):
		return 1
	else:
		return 0


def g_input(number1,text):
	
	alive=1
	while(alive):
		set_text(text,'n_font.ttf',30)	
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_1:
					number1+="1"
				elif event.key == pygame.K_2:
					number1+="2"
				elif event.key == pygame.K_3:
					number1+="3"
				elif event.key == pygame.K_4:
					number1+="4"
				elif event.key == pygame.K_5:
					number1+="5"
				elif event.key == pygame.K_6:
					number1+="6"
				elif event.key == pygame.K_7:
					number1+="7"
				elif event.key == pygame.K_8:
					number1+="8"
				elif event.key == pygame.K_9:
					number1+="9"	
				alive+=1
				if(alive>4):
					set_text('You have entered '+number1,'n_font.ttf',26)
					time.sleep(2)
					alive=0
			elif event.type == pygame.QUIT:
				pygame.quit()
				quit()	
	return number1

screen=pygame.display.set_mode((w,h))
pygame.display.set_caption('Cows and Bulls')

set_text('COWS AND BULLS','m_font.ttf',50)
time.sleep(3)

number1=""
number2=""
guess1=""
guess2=""
g_c=1

number1=g_input(number1,'Enter your Number Player 1:')
number2=g_input(number2,'Enter your Number Player 2:')	

while(1):
	if(g_c%2==1):
		guess1=g_input(guess1,'Enter your Guess Player 1:')
		passed=cb_check(guess1,number2)
		if(passed):
			set_text('You won, Player 1!','n_font.ttf',30)
			time.sleep(3)
			pygame.quit()
			quit()

	else:
		guess2=g_input(guess2,'Enter your Guess Player 2:')
		passed=cb_check(guess2,number1)
		if(passed):
			set_text('You won, Player 2!','n_font.ttf',30)
			time.sleep(3)
			pygame.quit()
			quit()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
	g_c+=1	
	guess1,guess2="",""
	
