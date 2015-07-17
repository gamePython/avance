import  pygame
import  time
#colores r,g y b
blanco=(255,255,255)
negro=(0,0,0)
rojo=(255,0,0)


pygame.init()
# tamanio de juego
superficie=pygame.display.set_mode((800,600))
pygame.display.set_caption('coches')
#actualiza toa la pantalla
# pygame.display.flip()

#eventos
gameExit=False
lead_x=300
lead_y=300
lead_x_cambio=0
lead_y_cambio=0
reloj=pygame.time.Clock()
font=pygame.font.SysFont(None,25)
def message_to_screen(msg,color):
	screen_texto=font.render(msg,True,color)
	superficie.blit(screen_texto,[lead_x,lead_y])
while not gameExit:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			gameExit=True
	if event.type==pygame.KEYDOWN:
		if event.key == pygame.K_LEFT:
			lead_x_cambio = -10
			lead_y_cambio = 0
		elif event.key == pygame.K_RIGHT:
			lead_x_cambio = 10
			lead_y_cambio = 0
		elif event.key == pygame.K_UP:
			lead_y_cambio = -10
			lead_x_cambio = 0
		elif event.key == pygame.K_DOWN:
			lead_y_cambio = 10
			lead_x_cambio = 0
		
	if lead_x>=800 or lead_x<0 or lead_y>=600 or lead_y<=0:
		gameExit=True

	lead_x +=lead_x_cambio
	lead_y +=lead_y_cambio
	# cambiar color pantalla esta funcion lo cambia
	superficie.fill(rojo)
	pygame.draw.rect(superficie,negro,[lead_x,lead_y,10,10])
	# otra forma de dibujar
	# superficie.fill(blanco,rect=[200,200,10,10])
	# actualiza solo un campo especifico  pero con parametro
	pygame.display.update()  
	reloj.tick(15)
message_to_screen("tu perdiste",negro)
pygame.display.update()  
time.sleep(5)

pygame.quit()
quit()
