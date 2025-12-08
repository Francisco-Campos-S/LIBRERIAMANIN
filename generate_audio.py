from gtts import gTTS

text = '''
En este video explicamos el área bajo la curva y su relación con la integral.

Primero mostramos la función f de x igual a media por x al cuadrado.
Luego aproximamos el área entre cero y cuatro con sumas de Riemann, usando pocos rectángulos.
Al aumentar el número de rectángulos la aproximación mejora.
En el límite, la suma de Riemann converge a la integral definida.
La integral de cero a cuatro de un medio por x al cuadrado es treinta y dos tercios, aproximadamente diez coma sesenta y siete.

Fin. Prueba este ejemplo con otras funciones y límites.
'''

tts = gTTS(text, lang='es')
output = 'area_bajo_curva_es.mp3'
tts.save(output)
print(f'Archivo de audio generado: {output}')
