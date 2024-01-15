import openai

openai.api_key = "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"
system_init = '''Hace de cuenta que sos un analizador de setnimientos.
                yo te paso sentimeintos y vos anilizas el sentimiento de los mensajes y me das una respuesta al menos de 1 caracter y como maximo 4 caracteres
                SOLO RESPUESTAS NUMERICAS, donde -1 es negactividad maxima, 0 esneutral y 1 es positiva maxima.
                (pUedes responder solo con ints o floats)'''
                
mensajes = [{"role": "system", "content": system_rol}]

class Sentimeinto:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color 
    def __str__(self):
        return "\x1b[1;{}m{}\x1b[0;37m".format(self.color,self.nombre)
    
    
class AnalizadorDeSentimeintos:
   def __init__(self, rangos):
       self.rangos = rangos
       
       
    def analizar_sentimiento(self, polaridad):
    for rango, sentimiento in self.rangos:
        if rango [0] < polaridad <= rango[1]:
            return sentimiento
        return Sentimeinto("Muy negativo","31")
    
rangos = [
    ((-0.6,-0.3),Sentimeinto("negativo","31")),
    ((-0.3,-0.1),Sentimeinto("algo negativo","31")),
    ((-0.1,0.1),Sentimeinto("neutral","33")),
    ((0.1,0.4),Sentimeinto("algo positivo","32")),
    ((0.4,0.9),Sentimeinto("positivo","32")),
    ((0.9,1),Sentimeinto("muy positivo","32")),
]


    
analizador = AnalizadorDeSentimeintos()
#resultado = analizador.analizar_sentimiento(0.95)
while True:
    user_prompt = input ("\x1b[1;33m" + "\n Decime Algo: " + "\x1b[0;37m")
    mensajes.append({"role": "user", "content": user_prompt})
    
    completion = openai.ChatCompletion.create(
        model = "gpt -3.5-turbo", 
        messages = mensajes,
        max_tokens = 8
    )
    
    respuesta = completion.choices[0].message["content"]
    mensajes.append({"role":"assistant", "content": respuesta})
    
    sentimiento = analizador.analizar_sentimiento(float(respuesta))
    print(sentimiento)