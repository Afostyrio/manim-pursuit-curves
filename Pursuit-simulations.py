from manim import *

class BouguerCurve(Scene):
	startingPoint = 4 # El punto en el que inicia el perseguido $x_0$.
	speed = 2 # El factor de velocidad $k$.

	def parametricPath(self, t):
		return np.array((self.startingPoint,t,0)) # La parametrización de la ruta del perseguido.

	def construct(self):
		plane = NumberPlane() # Dibuja el plano coordenado
		rabbitPath = ParametricFunction(self.parametricPath, np.array([0, 4]), color=GRAY_C) # Define el camino del perseguido.
		rabbitPathLength = rabbitPath.get_arc_length() # Calcula la distancia del camino. Este dato luego se utiliza para que la rapidez del perseguido sea 1.
		rabbit = Dot([self.startingPoint, 0, 0]) # El perseguido
		self.add( #  Dibuja los componentes antes descritos.
			plane,
			rabbitPath,
			rabbit
		)
		fox = Dot([0,0,0], color=RED) # El perseguidor,
		foxPath = TracedPath(fox.get_center, color=RED, stroke_color=RED) # La curva de persecución.
		analyticCurve = plane.plot( # La solución encontrada para $k>1$
			lambda x: self.startingPoint/2*((1-x/self.startingPoint)**(1+1/self.speed)/(1+1/self.speed)
					-(1-x/self.startingPoint)**(1-1/self.speed)/(1-1/self.speed))
					+self.startingPoint*self.speed/(self.speed**2-1),
				x_range=[0, self.startingPoint-0.01],
				color=BLUE_A
			)
		
		time = DecimalNumber(0, unit="\mathrm s").to_corner(UR) # El tiempo de animación,
		time.add_updater(lambda mob: mob.set_value(self.renderer.time)) # actualizado en cada fotograma.

		self.add(analyticCurve, fox, foxPath, time) # Añadimos los componentes descritos.
		fps = config.frame_rate # El número de fotogramas por segundo.
		
		def shiftTowards(pursuer): # El persecutor se desplazará en dirección al perseguido de manera que, en 1 segundo, se habrá desplazado una distancia $k$.
			pursuer.shift(self.speed/fps*
			(rabbit.get_center()-pursuer.get_center())/np.linalg.norm(rabbit.get_center()-pursuer.get_center()))

		fox.add_updater(shiftTowards) # Actualizamos la posición del persecutor en cada fotograma siguiendo la regla antes descrita.
		self.play(
			MoveAlongPath(rabbit, rabbitPath), # Movemos al perseguido a lo largo de su ruta.
			run_time=rabbitPathLength, # La duración de la animación será la longitud del camino, por lo que la rapidez del perseguido será 1.
			rate_func=linear # Uniformiza la animación: la simulación no tiene aceleración.
		)

class HathawayCurve(Scene):
	speed = 1 # El factor de velocidad $k$.

	def parametricPath(self, t): # Define la parametrización del camino del perseguido.
		return np.array((np.cos(t),np.sin(t),0))
	
	def construct(self):
		plane = NumberPlane() # Dibuja el plano coordenado
		rabbitPath = ParametricFunction(self.parametricPath, np.array([0, 6*PI]), color=GRAY_C) # Define el camino del perseguido.
		rabbitPathLength = rabbitPath.get_arc_length() # Calcula la distancia del camino. Este dato luego se utiliza para que la rapidez del perseguido sea 1.
		rabbit = Dot([1, 0, 0]) # El perseguido
		self.add( #  Dibuja los componentes antes descritos.
			plane,
			rabbitPath,
			rabbit
		)
		fox = Dot([0,0,0], color=RED) # El perseguidor,
		foxPath = TracedPath(fox.get_center, color=RED, stroke_color=RED) # La curva de persecución.
		
		time = DecimalNumber(0, unit="\mathrm s").to_corner(UR) # El tiempo de animación,
		time.add_updater(lambda mob: mob.set_value(self.renderer.time)) # actualizado en cada fotograma.

		self.add(fox, foxPath, time) # Añadimos los componentes descritos.
		fps = config.frame_rate # El número de fotogramas por segundo.
		
		def shiftTowards(pursuer): # El persecutor se desplazará en dirección al perseguido de manera que, en 1 segundo, se habrá desplazado una distancia $k$.
			pursuer.shift(self.speed/fps*
			(rabbit.get_center()-pursuer.get_center())/np.linalg.norm(rabbit.get_center()-pursuer.get_center()))

		fox.add_updater(shiftTowards) # Actualizamos la posición del persecutor en cada fotograma siguiendo la regla antes descrita.
		self.play(
			MoveAlongPath(rabbit, rabbitPath), # Movemos al perseguido a lo largo de su ruta.
			run_time=rabbitPathLength, # La duración de la animación será la longitud del camino, por lo que la rapidez del perseguido será 1.
			rate_func=linear # Uniformiza la animación: la simulación no tiene aceleración.
		)

class pursuitCurves(Scene):
	def speed(self, t): # Función de velocidad.
		return -10*t*(t-1.5)
	
	def parametricPath(self, t): # Define la parametrización del camino del perseguido.
		return np.array((4,t,0))
	
	def construct(self):
		startingPoint = self.parametricPath(0) # El punto en el que inicia el perseguido.
		plane = NumberPlane() # Dibuja el plano coordenado
		rabbitPath = ParametricFunction(self.parametricPath, np.array([0, PI]), color=GRAY_C) # Define el camino del perseguido.
		rabbitPathLength = rabbitPath.get_arc_length() # Calcula la distancia del camino. Este dato luego se utiliza para que la rapidez del perseguido sea 1.
		rabbit = Dot(startingPoint) # El perseguido
		self.add( #  Dibuja los componentes antes descritos.
			plane,
			rabbitPath,
			rabbit
		)
		fox = Dot([0,0,0], color=RED) # El perseguidor,
		foxPath = TracedPath(fox.get_center, color=RED, stroke_color=RED) # La curva de persecución.
		
		time = DecimalNumber(0, unit="\mathrm s").to_corner(UR) # El tiempo de animación,
		time.add_updater(lambda mob: mob.set_value(self.renderer.time)) # actualizado en cada fotograma.

		self.add(fox, foxPath, time) # Añadimos los componentes descritos.
		fps = config.frame_rate # El número de fotogramas por segundo.
		
		def shiftTowards(pursuer): # El persecutor se desplazará en dirección al perseguido de manera que, en 1 segundo, se habrá desplazado una distancia $k(t)$.
			pursuer.shift(self.speed(self.renderer.time)/fps*
			(rabbit.get_center()-pursuer.get_center())/np.linalg.norm(rabbit.get_center()-pursuer.get_center()))

		fox.add_updater(shiftTowards) # Actualizamos la posición del persecutor en cada fotograma siguiendo la regla antes descrita.
		self.play(
			MoveAlongPath(rabbit, rabbitPath), # Movemos al perseguido a lo largo de su ruta.
			run_time=rabbitPathLength, # La duración de la animación será la longitud del camino, por lo que la rapidez del perseguido será 1.
			rate_func=linear # Uniformiza la animación: la simulación no tiene aceleración.
		)
