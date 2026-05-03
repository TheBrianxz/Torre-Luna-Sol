import os 
import time
import random

#--- COLORES ANSI ---
ROJO = '\033[91m'
VERDE = '\033[92m'
AMARILLO = '\033[93m'
AZUL = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
BLANCO = '\033[97m'
RESET = '\033[0m' 

#----ESTADISTICAS DEL HÉROE----
nombre = input(f"{CYAN}¿Cómo te llamas, Aventurero? {RESET}")
vida_jugador = 100
vida_maxima = 100
umbra = 50          # Energía para habilidades
max_umbra = 50
pociones = 3
piso = 1            # Progreso de la Aventura

def generar_enemigos():
    if piso == 1:
        return "Sombra Errante", 50, 10
    elif piso == 2:
        return "Caballero Caído", 80, 15
    elif piso == 3:
        return "EL DEMONIO PRIMORDIAL", 250, 40

def limpiar(): 
    os.system('clear' if os.name != 'nt' else 'cls')

def combatir(nombre_e, vida_e, dano_e):
    global vida_jugador, umbra, pociones

    while vida_e > 0 and vida_jugador > 0:
        limpiar()
        #--- HUD ---
        print(f"{BLANCO}--- ⚔  {nombre.upper()} VS {nombre_e} ⚔  ---{RESET}")
        print(f"{AMARILLO}Piso: {piso}{RESET} | Vida Enemigo: {ROJO}{vida_e}{RESET}")
        print(f"Tu Vida: {VERDE}{vida_jugador}/{vida_maxima}{RESET} | Umbra: {CYAN}{umbra}/{max_umbra}{RESET} | Pociones: {MAGENTA}{pociones}{RESET}")
        print(f"{BLANCO}--------------------------------------------------{RESET}")
        print(f"1. {BLANCO}Ataque Básico{RESET}")
        print(f"2. {AMARILLO}Filo Desesperante (15 Umbra){RESET}")
        print(f"3. {CYAN}Mil Cortes Divinos (20 Umbra){RESET}")
        print(f"4. {MAGENTA}Usar Poción{RESET}")
        print(f"5. {ROJO}Rendirse{RESET}")

        opcion = input(f"\n{BLANCO}Elije tu movimiento: {RESET}")

        # Regeneración pasiva de Umbra por turno
        umbra = min(max_umbra, umbra + 2)

        if opcion == "1":
            dano = random.randint(15, 35)
            suerte = random.randint(1, 10)
            if suerte == 10:
                dano = int(dano * 1.8)
                print(f"{AMARILLO}🔥 ¡GOLPE CRÍTICO! Heriste a {nombre_e} por {dano} HP.{RESET}")
            else:
                print(f"{BLANCO}💥 Heriste a {nombre_e} por {dano} HP.{RESET}")
            vida_e -= dano
            
        elif opcion == "2":
            if umbra >= 15:
                dano = random.randint(35, 50)
                vida_e -= dano
                umbra -= 15
                print(f"{AMARILLO}🔥 ¡FILO DESESPERANTE! Un impacto crítico de {dano} HP.{RESET}")
            else:
                print(f"{ROJO}❌ No tienes suficiente Umbra...{RESET}")

        elif opcion == "3":
            if umbra >= 20:
                golpes = random.randint(6, 13)
                dano_total = golpes * 5
                vida_e -= dano_total
                umbra -= 20
                print(f"{CYAN}⚔  ¡MIL CORTES DIVINOS! {golpes} tajos impactan por {dano_total} HP.{RESET}")
            else:
                print(f"{ROJO}❌ No tienes suficiente Umbra....{RESET}")
        
        elif opcion == "4":
            if pociones > 0:
                curacion = 48
                vida_jugador = min(vida_maxima, vida_jugador + curacion)
                pociones -= 1
                print(f"{VERDE}🧪 Te has tomado una poción. Recuperas {curacion} HP.{RESET}")
            else: 
                print(f"{ROJO}❌ No te quedan pociones.{RESET}")

        elif opcion == "5":
            print(f"{ROJO}🏳  Has huido del combate...{RESET}")
            vida_jugador = 0

        time.sleep(1.4)

        # Turno del Enemigo
        if vida_e > 0 and vida_jugador > 0:
            golpe_rival = random.randint(max(1, dano_e - 5), dano_e + 5)
            vida_jugador -= golpe_rival
            print(f"{ROJO}👿 {nombre_e} contraataca y te quita {golpe_rival} HP.{RESET}")
            time.sleep(1.2)

    if vida_jugador > 0: 
        print(f"{VERDE}✨ ¡Victoria! Has derrotado a {nombre_e}.{RESET}")
        return "victoria"
    else: 
        return "derrota"

def iniciar_aventura():
    global piso, umbra, vida_maxima, max_umbra, vida_jugador, pociones

    print(f"{MAGENTA}\n🏰 {nombre} entra en la Torre que conecta la Luna y el Sol...{RESET}")
    time.sleep(2)

    while piso <= 3 and vida_jugador > 0:
        nom_e, hp_e, dmg_e = generar_enemigos()
        resultado = combatir(nom_e, hp_e, dmg_e)

        if resultado == "victoria":
            piso += 1
            if piso <= 3:
                vida_maxima += 15
                max_umbra += 10
                umbra = max_umbra
                vida_jugador = vida_maxima
                pociones += 1
                print(f"{AMARILLO}✨ ¡SUBISTE DE NIVEL! Vida Máxima: {vida_maxima} | +1 poción{RESET}")
                time.sleep(2.2)
        else:
            break

    if piso > 3:
        print(f"{VERDE}\n 🏆 ¡ERES UNA LEYENDA! Has purificado la torre.{RESET}")
    else:
        print(f"{ROJO}\n💀 Has sido derrotado... 🎮 FIN DEL JUEGO.{RESET}")

if __name__ == "__main__":
    iniciar_aventura()
