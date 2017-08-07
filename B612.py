# -*- Coding: UTF-8 -*-
# Python 3
#                       ██████╗  ██████╗ ██╗██████╗ 
#                       ██╔══██╗██╔════╝███║╚════██╗
#                       ██████╔╝███████╗╚██║ █████╔╝
#                       ██╔══██╗██╔═══██╗██║██╔═══╝ 
#                       ██████╔╝╚██████╔╝██║███████╗
#                       ╚═════╝  ╚═════╝ ╚═╝╚══════╝
#                                                         By: LawlietJH
#                                                              v.1.0.4
from BannerEMCrk import Banner
import time
import os

#=======================================================================

Version = "v1.0.4"

BannerB612 = Banner()

Autor = """
                            ╦  ┌─┐┬ ┬┬  ┬┌─┐┌┬┐╦╦ ╦
                            ║  ├─┤││││  │├┤  │ ║╠═╣
                            ╩═╝┴ ┴└┴┘┴─┘┴└─┘ ┴╚╝╩ ╩
"""
# Fuente: Calvin S - http://patorjk.com/software/taag/#p=display&f=Calvin%20S&t=LawlietJH



def Dat():
	
	os.system("cls && Title B612.py                "+\
			"By: LawlietJH                "+Version+"    ")
	print("\n\n", BannerB612)
	print("\n\n", Autor)
	print("\n{:^80}".format(Version))



#=======================================================================



def Pause(Quiet=True):
	
	if Quiet: os.system("Pause > Nul")
	else: os.system("Pause")



def Clear():
	
	os.system("Cls")



def Sleep(Tiempo=1.5):
	
	time.sleep(Tiempo)



#=======================================================================



def Asc_Dec(Asc):	#~ Ascii a Decimal.
	
	Lista = []
	Decimal = ""
	
	for Letra in Asc:				#~ Se Añaden los Caracteres a la Lista
		Lista.append(ord(Letra))	#~ Convertidos en su Respectivo Decimal.  
	
	for Dec in Lista:				#~ Se Añaden los Números a la Cadena.
		Decimal += str(Dec) + " "
	
	return Decimal



def Dec_Asc(Dec):	#~ Decimal a Ascii.
	
	xD = ""
	Ascii = ""
	Lista = []
	
	for num in Dec:
		
		if num != " ":
			xD = xD + num
		
		else:
			Lista.append(chr(int(xD)))
			xD = ""
			
	Lista.append(chr(int(xD)))
	
	for Asc in Lista:
		
		Ascii += Asc	
	
	return Ascii



#=======================================================================



String = ""
Bool = True



def B612(Cadena, Cifrar=True):
	
	global String, Bool
	
	String = ""
	C1 = 0
	C2 = 0
	
	if Cifrar:
		
		Bool = True
		
		for x in Cadena:
			
			if x.startswith("VirusZióN"):
				
				String = String[:-2]
				continue
						
			Dec = Asc_Dec(x)
			Dec = Dec.split(" ")
			
			for y in Dec:
				
				if y == "": continue
				elif y == "32":
					
					String += " "
					continue
					
				y = str(int(y) * 72)
				
				if len(y) == 4:
					
					C1, C2 = int(y[:2])+32, int(y[-2:])+32
					
					if C1 == 128: C1 -= 1
					if C2 == 128: C2 -= 1
					
					Asc = Dec_Asc(str(C1)+" "+str(C2))
					String += Asc
					
				if len(y) == 5:
					
					C1, C2 = int(y[:3])+32, int(y[-2:])+32
					
					if C1 == 128: C1 -= 1
					if C2 == 128: C2 -= 1
					
					Asc = Dec_Asc(str(C1)+" "+str(C2))
					String += Asc
				
			String += "\n"
	else:
		
		Bool = False
		
		yy = ""
		Cont = 0
		
		for x in Cadena:
			
			if x.startswith(r"]|k\r(t8rp`pk\ÎX0"):
				
				String = String[:-2]
				continue
			
			Dec = Asc_Dec(x)
			Dec = Dec.split(" ")
			
			for y in Dec:
				
				Cont += 1
				yy += y + " "
				
				if y == "32" and Cont == 1: #Atento!
						
						String += " "
						Cont = 0
						yy = ""
						continue
					
				elif y == "":
					Cont = 0
					yy = ""
					continue
				
				if Cont == 2:
					
					yy = yy.split(" ")
					
					C1, C2 = int(yy[0])-32, int(yy[1])-32
					
					if C1 < 10:
						C1 = "0" + str(C1)
						
					if C2 < 10:
						C2 = "0" + str(C2)
						
					#~ if C1 == 95: C1 += 1
					if C2 == 95: C2 += 1
						
					yy = str(C1) + str(C2)
					
					yy = str(int(yy)//72)
										
					yy = Dec_Asc(yy)
					
					String += yy
					Cont = 0
					yy = ""
					
			String += "\n"



def LeerArchivo():
	
	Nombre = input("\n\n\t [+] Nombre de Archivo: ")
	
	try: Eny = open(Nombre,"r")
	except FileNotFoundError:
		
		print("\n\n\t [!] Ese Archivo No Existe.")
		Sleep()
		return True
	
	Cadena = Eny.read()
	
	print("\n\n\t [+] En Archivo:\n\n" + Cadena)
	
	Cadena = Cadena.split("\n")
	
	if Cadena[-1] == r"]|k\r(t8rp`pk\ÎX0": B612(Cadena, False)
	else: B612(Cadena, True)
	
	Eny.close()
	
	print("\n\n\t [+] Cadena:\n\n" + String)
	
	Pause()
	
	return False



def GuardarArchivo():
	
	global String, Bool
	
	open("Eny.zion", "a")
	Eny = open("Eny.zion", "w")
	if Bool: Eny.write(String + "\n" + r"]|k\r(t8rp`pk\ÎX0")
	else: Eny.write(String)
	Eny.close()



#=======================================================================



def Main():
	
	Dat()
	LeerArchivo()
	GuardarArchivo()



#=======================================================================



if __name__ == "__main__":
	
	while True:
		
		Clear()
		
		Main()


