from textblob import TextBlob

class AnalizadorDeSentimientos:
    def analizar_sentimeintos(self, texto):
        analisis = TextBlob(texto)
        if analisis.sentimeintos.polarity > 0:
            return "Positivo"
        elif analisis.sentimeintos.polarity ==0:
            return "Neutro"
        else:
            return "negativo"
        
analizador = AnalizadorDeSentimientos()
resultado + analizador.analizar_sentimeintos("")

