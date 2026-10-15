def logger(func):
	def wrapper(*args, **kwargs):
		print("Começoua pesagem")
		res = func(*args, **kwargs)
		print(f"Terminou a pesagem com retorno: {res}")
		return True
	return wrapper
 
 
@logger
def pesagem(argumento, host=None):
	print(f"fazendo a pesagem de {argumento} para host {host}")
	return "pesagem feita"
 
 
if __name__ == "__main__":
	res = pesagem("teste", host="teste2")
	print(res)
 
 
# *(arg1, arg2, arg3)
# arg1, arg2, arg3
 
 
# **{host: "teste"}
# host="teste"
