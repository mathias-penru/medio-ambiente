import discord

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
 if message.author == client.user:
        return
 if message.content.startswith('$como puedo reutilizar las botellas de plastico'):
        await message.channel.send('https://www.youtube.com/watch?v=ll5OXyrO5a8')
 elif message.content.startswith('$como reducir nuestra huella de carbono'):
        await message.channel.send('https://www.youtube.com/watch?v=EZbjwiNOO0I&t=239s')
 elif message.content.startswith('$que es el cambio climatico'):
        await message.channel.send('El cambio climático se refiere a los cambios a largo plazo de las temperaturas y los patrones climáticos. Estos cambios pueden ser naturales, debido a variaciones en la actividad solar o erupciones volcánicas grandes. Pero desde el siglo XIX, las actividades humanas han sido el principal motor del cambio climático, debido principalmente a la quema de combustibles fósiles como el carbón, el petróleo y el gas.')
 elif message.content.startswith('$causas del cambio climatico'):
        await message.channel.send('La generación de electricidad y calor a través de los combustibles fósiles provoca una gran cantidad de emisiones globales. La mayoría de la electricidad se genera todavía con la combustión de carbón o gas, lo que produce dióxido de carbono y óxido nitroso, que son potentes gases de efecto invernadero que cubren el planeta y atrapan el calor proveniente del sol. A nivel global, algo más de un cuarto de la electricidad proviene de fuentes de energía renovables eólicas y solares que, al contrario que los combustibles fósiles, emiten poca o ninguna cantidad de gases o contaminantes en el aire Productos de fabricaciónLa industria y las fábricas producen emisiones, en su mayoría provenientes de la quema de combustibles fósiles destinada a generar energía para la fabricación de cemento, hierro, acero, componentes electrónicos, ropa y otros bienes. La minería y otros procesos industriales también generan gases, de la misma forma que lo hace el sector de la construcción. La maquinaria utilizada en los procesos de fabricación a menudo realizados mediante carbón, petróleo o gas, y con algunos materiales, como los plásticos, están compuestos de sustancias químicas derivadas de los combustibles fósiles. La industria manufacturera es una de las que más contribuyen a las emisiones de gases de efecto invernadero a nivel mundial.')
 elif message.content.startswith('$que es la contaminacion'):
        await message.channel.send('La contaminación es la presencia o acumulación de sustancias en el medio ambiente que afectan negativamente el entorno y las condiciones de vida, así como la salud o la higiene de los seres vivos. Esto también se conoce como contaminación ambiental.')
 elif message.content.startswith('$que tanto afectan los plasticos al medio ambiente'):
        await message.channel.send('Una vez en el mar, la luz solar, el viento y las olas descomponen el plástico en partículas pequeñas que suelen medir menos de cinco milímetros de ancho. Estas, denominadas microplásticos, se propagan por la columna de agua y se han hallado en todos los rincones del planeta, desde el Everest, el lugar más alto, hasta la fosa de las Marianas, el punto más profundo. Los microplásticos se descomponen en fragmentos cada vez más pequeños. Asimismo, se han descubierto microfibras de plástico en sistemas municipales de agua potable y viajando en el aire.')
 elif message.content.startswith('$cual es tu funcion'):
        await message.channel.send('mi funcion es ayudarte a comprender algunos conceptos basicos sobre la contaminacion, el cambio climatico y formas de combatirlo')



client.run("token")