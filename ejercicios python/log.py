import datetime

def abrir_log(nombre_Log):
	archivo_log=open(nombre_Log,"a")
	guardar_log(archivo_log,"iniciando registro de errores")
	return archivo_log


def guardar_log(archivo_log,mensaje):
	hora_actual = str(datetime.datetime.now())
	archivo_log.write(hora_actual+"  "+mensaje+"\\n")

def cerrar_log(archivo_log):
	guardar_log(archivo_log,"Fin del registro de errores")
	archivo_log.close()

def main():
	log = abrir_log("prueba.log")
	guardar_log(log,"prueba i210")
	cerrar_log(log)

if __name__ == "__main__":
	main()