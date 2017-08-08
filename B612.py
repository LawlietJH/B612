# -*- Coding: UTF-8 -*-
# Python 3
# Windows
#                       ██████╗  ██████╗ ██╗██████╗ 
#                       ██╔══██╗██╔════╝███║╚════██╗
#                       ██████╔╝███████╗╚██║ █████╔╝
#                       ██╔══██╗██╔═══██╗██║██╔═══╝ 
#                       ██████╔╝╚██████╔╝██║███████╗
#                       ╚═════╝  ╚═════╝ ╚═╝╚══════╝
#                                                         By: LawlietJH
#                                                              v.1.0.8
from BannerB612 import Banner
import time
import os

os.system("Color 0A")

#=======================================================================

Version = "v1.0.8"

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
xD = False


def B612(Cadena, Cifrar=True, Dats="12+"):
	
	global String, Bool
	
	Dats = int(Dats[:-1])
	
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
				
				elif y == "9":
					
					String += "\t"
					continue
					
				elif y == "10":
					
					String += "\n"
					continue
					
				elif y == "32":
					
					String += " "
					continue
					
				y = str(int(y) * 72)
				
				if len(y) == 4:
					
					C1, C2 = int(y[:2])+Dats, int(y[-2:])+Dats
					
					if C1 == 128: C1 -= 1
					if C2 == 128: C2 -= 1
					
					Asc = Dec_Asc(str(C1)+" "+str(C2))
					String += Asc
					
				if len(y) == 5:
					
					C1, C2 = int(y[:3])+Dats, int(y[-2:])+Dats
					
					if C1 == 128: C1 -= 1
					if C2 == 128: C2 -= 1
					
					Asc = Dec_Asc(str(C1)+" "+str(C2))
					String += Asc
				
			if xD != True: String += "\n"
			
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
				
				if y == "9" and Cont == 1: #Atento!
					
					String += "\t"
					Cont = 0
					yy = ""
					continue
					
				if y == "10" and Cont == 1: #Atento!
					
					String += "\n"
					Cont = 0
					yy = ""
					continue
					
				elif y == "32" and Cont == 1: #Atento!
					
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
					
					C1, C2 = int(yy[0])-Dats, int(yy[1])-Dats
					
					if C1 < 10:
						C1 = "0" + str(C1)
						
					if C2 < 10:
						C2 = "0" + str(C2)
						
					if C1 == 95: C1 += 1
					if C2 == 95: C2 += 1
						
					yy = str(C1) + str(C2)
					
					yy = str(int(yy)//72)
										
					yy = Dec_Asc(yy)
					
					String += yy
					Cont = 0
					yy = ""
					
			if xD != True: String += "\n"



def LeerArchivo(Nombre, Dats="12+"):
	
	global String
	
	try: Eny = open(Nombre,"r")
	except FileNotFoundError:
		
		print("\n\n\t [!] Ese Archivo No Existe.")
		Sleep()
		return True
	
	Cadena = Eny.read()
	
	print("\n\n\t [+] En Archivo:\n\n" + Cadena)
	
	Cadena = Cadena.split("\n")
	
	if Cadena[-1] == r"]|k\r(t8rp`pk\ÎX0": B612(Cadena, False, Dats)
	else: B612(Cadena, True, Dats)
	
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
	
	global String, xD
	
	Dats = "12+"
	
	Dat()
	print("\n\n [*] Escribe el Nombre de Archivo."+
		"\n\n [!] Indíca el Número de 'Dats' a Utilizar. Por Defecto es 12+"+
		"\n\n\t [~] Ejemplo: Archivo.txt 12+"+
		"\n\n [*] Dats Soportados:  11,  12  y del  14  al  32\n\n [¡] Del  22  al  32  es más Estable Por Ahora.")
	Cadena = input("\n\n\n >>> ")
	
	if Cadena.endswith("+"):
		
		Dats = Cadena.split(" ")[-1]
		
		if Dats != "11+" and Dats != "12+" and Dats != "14+" and Dats != "15+"\
		and Dats != "16+" and Dats != "17+" and Dats != "18+" and Dats != "19+"\
		and Dats != "20+" and Dats != "21+" and Dats != "22+" and Dats != "23+"\
		and Dats != "24+" and Dats != "25+" and Dats != "26+" and Dats != "27+"\
		and Dats != "28+" and Dats != "29+"  and Dats != "30+" and Dats != "31+"\
		and Dats != "32+":
			
			print("\n\n\t [!]", Dats, "No Soportado.")
			Pause()
			return
		
		Cadena = " ".join(Cadena.split(" ")[:-1])
	
	if os.path.exists(Cadena): # or Cadena.endswith((".txt", ".zion")):
		
		LeerArchivo(Cadena, Dats)
	
	else:
			
		xD = True
		
		#~ if Cadena.endswith("0x"): B612(Cadena, False)
		#~ else: B612(Cadena, True)
		B612(Cadena, True, Dats)
		
		print("\n\n [+] Cadena\n  |\n   ---------> " + String.replace("\n", "" ))
		
		xD = False
		
		Pause()
		
	GuardarArchivo()



#=======================================================================



if __name__ == "__main__":
	
	while True:
		
		Clear()
		
		Main()


