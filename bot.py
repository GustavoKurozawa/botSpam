import pyautogui
import time

def bot_spam (mensagem, quantidade):
    time.sleep(5)
    for x in range(quantidade):
        pyautogui.typewrite(mensagem)
        pyautogui.press("enter")

print("---------------------BOT DE SPAM----------------------------------")
mensagem = input("Informe a mensagem: ")
quantidade = int(input("Informe a quantidade de mensagem: "))
bot_spam(mensagem, quantidade)