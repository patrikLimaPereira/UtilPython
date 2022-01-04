from pygame import mixer
import time
import enum



def  playSimpleSound (type,repeat =3,timeRepeat= 2.3):
		mixer.init() 
		sound=mixer.Sound (type.value)
		i = 0
		while i < repeat :			
				sound.play()
				i =i+1		
				time.sleep(0.3)
				while mixer.get_busy ():
					time.sleep(timeRepeat)
			
			
			
			
class SoundOption ( enum.Enum):
         GATO =  'sounds/cat.wav'
         GATO_IMITATE_LION =  'sounds/catImitateLion.wav'         
         PACOTE = 'sounds/bombpl.wav'
         
         			
         						
         									
         															
		
			
	
