import os 
import time
import random

#----ESTADISTICAS DEL HÉROE----
nombre = input("¿Cómo te llamas, Aventurero? ")
vida_jugador = 100
vida_maxima = 100
umbra = 50          # Energía para habilidades
max_umbra = 50
pociones = 3
piso = 1            # Progreso de la Aventura

def generar_enemigos():
    if piso == 1:
        return "Sombra Errante", 50, 10 # Nombre, Vida, Daño Base
    elif piso == 2:
        return "Caballero Caído", 80, 15
    elif piso == 3:
        return "EL DEMONIO PRIMORDIAL", 150, 30

def limpiar(): 
    # 'posix' es para linux/Mac (Chromebook), 'nt' es para windows
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def combatir(nombre_e, vida_e, dano_e):
    # El permiso para modificar las variables globales (estadisticas)
    global vida_jugador, umbra, pociones # DECLARACIÓN AL INICIO

    while vida_e > 0 and vida_jugador > 0:
        limpiar()
        #--- HUD: Interfaz de Usuario ---
        print(f"--- ⚔  {nombre} VS {nombre_e} ⚔  ---")
        print(f"Piso: {piso} | Vida Enemigo: {vida_e}")
        print(f"Tu Vida: {vida_jugador}/{vida_maxima} | Umbra: {umbra}/{max_umbra} | Pociones: {pociones}")
        print("--------------------------------------------------")
        print("1. Ataque Basico")
        print("2. Filo Desesperante (Cuesta 15 de Umbra)")
        print("3. Mil Cortes Divinos (Cuesta 20 de Umbra)")
        print("4. Usar Poción")
        print("5. Rendirse")

        opcion = input("\nElije tu movimiento: ")

        if opcion == "1":
            dano = random.randint(15, 35)
            suerte = random.randint(1, 10) # 10% de probabilidad
            if suerte == 10:
                dano = int(dano * 1.8)
                print(f"🔥 ¡GOLPE CRÍTICO! Heriste a {nombre_e} por {dano} HP.")
            else:
                print(f"💥 Heriste a {nombre_e} por {dano} HP.")
            vida_e -= dano
            
        elif opcion == "2":
            if umbra >= 15:
                dano = random.randint(35, 50)
                vida_e -= dano
                umbra -= 15
                print(f"🔥 ¡FILO DESESPERANTE! Un impacto crítico de {dano} HP.")
            else:
                print("❌ No tienes suficiente Umbra...")

        elif opcion == "3":
            if umbra >= 20:
                # Simulamos ataques múltiples
                golpes = random.randint(6, 13)
                dano_total = golpes * 5
                vida_e -= dano_total
                umbra -= 20
                print(f"⚔  ¡MIL CORTES DIVINOS! {golpes} tajos impactan por {dano_total} HP.")
            else:
                 print("❌ No tienes suficiente Umbra....")
        
        elif opcion == "4":
            if pociones > 0:
                curacion = 48
                vida_jugador = min(vida_maxima, vida_jugador + curacion)
                pociones -= 1
                print(f"🧪 Te has tomado una poción. Recuperas {curacion} HP.")
                print(f"Vida actual: {vida_jugador}/{vida_maxima}")
            else: 
                print("❌ No te quedan pociones.")

        elif opcion == "5":
            print("🏳  Has huido del combate...")
            vida_jugador = 0 # Esto fuerza a finalizar 

        time.sleep(1.2) # Pausa para leer la acción

        # Si el enemigo sobrevivió, él responderá
        if vida_e > 0 and vida_jugador > 0:
            golpe_rival = random.randint(max(1, dano_e - 5), dano_e + 5)
            vida_jugador -= golpe_rival
            print(f"👿 {nombre_e} contraataca y te quita {golpe_rival} HP.")
            time.sleep(1.2)

    #---CIERRE DE LA FUNCION (Fuera del while)---
    if vida_jugador > 0: 
        print(f"✨ ¡Victoria! Has derrotado a {nombre_e}.")
        return "victoria"
    else: 
        print(f"💀 Has sido derrotado por {nombre_e}...")
        return "derrota"

def iniciar_aventura():
    # TODAS las globales que se van a modificar se declaran AQUÍ al inicio
    global piso, umbra, vida_maxima, max_umbra, vida_jugador, pociones

    print(f"\n🏰 {nombre} entra en la Torre que conecta la Luna y el Sol...")
    time.sleep(2)

    while piso <= 3 and vida_jugador > 0:
        # 1. Traemos al enemigo del piso actual
        nom_e, hp_e, dmg_e = generar_enemigos()

        # 2. Iniciamos el combate
        resultado = combatir(nom_e, hp_e, dmg_e)

        if resultado == "victoria":
            piso += 1
            
            # --- Mejoras de Nivel ---
            vida_maxima += 15               # Subes vida máxima
            max_umbra += 10                 # Más energía
            umbra = max_umbra
            vida_jugador = vida_maxima       # Te curas al subir de nivel
            pociones += 1                   # Botín: poción gratis
            
            print(f"✨ ¡SUBISTE DE NIVEL! Vida Máxima: {vida_maxima} | +1 poción")
            time.sleep(2.2)
        else:
            break

    if piso > 3:
        print("\n 🏆 ¡ERES UNA LEYENDA! Has purificado la torre.")
    else:
        print("\n🎮 FIN DEL JUEGO. Inténtalo de nuevo.")

#--- LA LLAMADA FINAL ---
iniciar_aventura()
