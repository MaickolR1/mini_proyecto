from groq import Groq
# configuracion inicial
mi_llave = ""

def programa_principal():
    print("--- Bienvenido al Proyecto de Programacion (C7)--- ")
programa_principal()

 # PASO a) el usuario va ingresar un mensaje
mensaje_usuario= input("\nEscribe tu pregunta para el modelo:")
print("\nConectando con llama-3-370b-veratile.")

#  PASO b) creacion de conexion con el LLM
cliente=Groq(api_key=mi_llave)

# PASO c) envia el mensaje al LLM
# # guardamos la orden en una variable llamada "peticion"
peticion = cliente.chat.completions.create(
    model= "llama-3.3-70b-versatile",
    messages=[{"role":"user",
               "content": mensaje_usuario}]
)
#  PASO d) el LLM procesa el mensaje y genera una repuesta 
repuesta_final= peticion.choices[0].message.content

#  PASO e) el programa recibe la respuesta y muestra la respuesta
print(" la IA dice:", repuesta_final)
