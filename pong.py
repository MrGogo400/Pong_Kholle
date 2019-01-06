from tkinter import *
import tkinter.messagebox as messagebox
import random
import time


tk = Tk()
tk.title('Pong | Hugo Marques')

canvas = Canvas(tk,width=700,height=500)
canvas.config(bg='black')
canvas.pack()


tk.update()


canvas.create_line(350,0,350,500,fill='white')

#Balle
class balle:
	def __init__(self,canvas,raquette1,raquette,color):
		self.canvas = canvas
		self.raquette = raquette
		self.raquette1 = raquette1
		self.ScoreG = 0
		self.ScoreD = 0
		self.JD = None
		self.JG = None
		self.id = self.canvas.create_oval(10,10,35,35,fill = color)
		self.canvas.move(self.id,327,220)
		self.canvas_height=self.canvas.winfo_height()
		self.canvas_width=self.canvas.winfo_width()
		self.x = random.choice([-2.5,2.5])
		self.y = -2.5
		
	#Check si le score est a 10
	def checkwin(self):
		winner = None
		if self.ScoreG == 10:
			winner = 'Joueur de gauche'
		if self.ScoreD == 10:
			winner = 'Joueur de droite'
			
		return winner
	
	#Change le score du joueur de gauche
	def updatep(self,val):
		self.canvas.delete(self.JG)
		self.JG = self.canvas.create_text(170,50,
		font=('',40),text=str(val),fill='white')
		
	#Change le score du joueur de droite
	def updatep1(self,val):
		self.canvas.delete(self.JD)
		self.JD = self.canvas.create_text(550,50,
		font=('',40),text=str(val),fill='white')		
	
	#Check les collision pour la raquette du joueur gauche	
	def hit_raquette_G(self,pos):
		
		raquette_pos = self.canvas.coords(self.raquette.id)
		
		if pos[2] >= raquette_pos[0] and pos[0] <= raquette_pos[2]:
			if pos[3] >= raquette_pos[1] and pos[3] <= raquette_pos[3]:
				return True	
				
			return False
	
	#Check les collision pour la raquette du joueur droite			
	def hit_raquette_D(self,pos):
		
		raquette_pos = self.canvas.coords(self.raquette1.id)
		
		if pos[2] >= raquette_pos[0] and pos[0] <= raquette_pos[2]:
			if pos[3] >= raquette_pos[1] and pos[3] <= raquette_pos[3]:
				return True	
				
			return False
			
	# Dessine la balle et check les collision sur les murs
	def draw(self):
		self.canvas.move(self.id,self.x,self.y)
		pos = self.canvas.coords(self.id)
		if pos[1] <= 0:
			self.y = 4
		if pos[3] >= self.canvas_height:
			self.y =-4
		if pos[0] <= 0:
			self.ScoreD += 1
			self.canvas.move(self.id,327,220)
			self.x = 4
			self.updatep1(self.ScoreD)
		if pos[2] >= self.canvas_width:
			self.ScoreG += 1
			self.canvas.move(self.id,-327,-220)
			self.x = -4
			self.updatep(self.ScoreG)
		if self.hit_raquette_G(pos):
			self.x = 4
		if self.hit_raquette_D(pos):
			self.x = -4
		
		
#Raquette	
class raquette:
	def __init__(self,canvas,color):
		self.canvas = canvas
		self.id = self.canvas.create_rectangle(0,200,20,310,fill=color)
		self.y = 0
		self.canvas_height=self.canvas.winfo_height()
		self.canvas_width=self.canvas.winfo_width()
		#Binding
		self.canvas.bind_all('z',self.up)
		self.canvas.bind_all('s',self.down)	
		
	#mouvement raquette
	def up(self,e):
		self.y = -5
		
	def down(self,e):
		self.y = 5
	
	#Dessin raquette 
	def draw(self):
		self.canvas.move(self.id,0,self.y)
		pos = self.canvas.coords(self.id)
		if pos[1] <= 0:
			self.y = 0
		if pos[3] >= 500:
			self.y = -0

#raquette droite
class raquette1:
	def __init__(self,canvas,color):
		self.canvas = canvas
		self.id = self.canvas.create_rectangle(680,200,710,310,fill=color)
		self.y = 0
		self.canvas_height=self.canvas.winfo_height()
		self.canvas_width=self.canvas.winfo_width()
		self.canvas.bind_all('<KeyPress-Up>',self.up)
		self.canvas.bind_all('<KeyPress-Down>',self.down)	
		
	def up(self,e):
		self.y = -5
		
	def down(self,e):
		self.y = 5
	
	def draw(self):
		self.canvas.move(self.id,0,self.y)
		pos = self.canvas.coords(self.id)
		if pos[1] <= 0:
			self.y = 0
		if pos[3] >= 500:
			self.y = 0
			

raquette = raquette(canvas,'white')
raquette1 = raquette1(canvas,'white')		
balle = balle(canvas,raquette1,raquette,'white')


while 1:

	balle.draw()
	raquette.draw()
	raquette1.draw()
	if balle.checkwin():
		messagebox.showinfo('Fin du jeu',balle.checkwin()+' a gagner !!')
		break
	tk.update_idletasks()
	tk.update()
	time.sleep(0.01)

	
quit()

tk.mainloop()