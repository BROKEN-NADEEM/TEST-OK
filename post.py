import time
import sys
import os
import random
import hashlib

# Colors
GREEN = "\033[1;32m"
RED = "\033[1;31m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
RESET = "\033[0m"

# Animation Effect - Typing
def typing_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Loading Animation
def loading_animation(text, duration=3):
    chars = ["|", "/", "-", "\\"]
    start_time = time.time()
    while time.time() - start_time < duration:
        for char in chars:
            sys.stdout.write(f"\r{GREEN}{text} {char}{RESET}")
            sys.stdout.flush()
            time.sleep(0.2)
    print()

# Clear Screen
def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

# Stylish Logo with Animation
def display_logo():
    logo = f"""
{GREEN}      
  ██████╗ ██████╗  ██████╗ ██╗  ██╗███████╗███╗   ██╗
  ██╔══██╗██╔══██╗██╔═══██╗██║  ██║██╔════╝████╗  ██║
  ██║  ██║██████╔╝██║   ██║███████║█████╗  ██╔██╗ ██║
  ██║  ██║██╔═══╝ ██║   ██║██╔══██║██╔══╝  ██║╚██╗██║
  ██████╔╝██║     ╚██████╔╝██║  ██║███████╗██║ ╚████║
  ╚═════╝ ╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝
{RESET}
"""
    typing_effect(logo, 0.002)

# Start the Script
clear_screen()
display_logo()

# Show Start Time
start_time = time.strftime("%Y-%m-%d %H:%M:%S")
typing_effect(f"{GREEN}START TIME: {start_time}{RESET}")

# Password System
correct_password_hash = hashlib.sha256("NADIM-XD".encode()).hexdigest()  # Secure Hash for Password

def password_prompt():
    typing_effect(f"\n{YELLOW}<<━━━━━━━━━━━━━━ LOGIN REQUIRED ━━━━━━━━━━━━━━>>{RESET}")
    
    attempts = 3
    while attempts > 0:
        password = input(f"{GREEN}𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗 ➜  {RESET}")
        password_hash = hashlib.sha256(password.encode()).hexdigest()

        if password_hash == correct_password_hash:
            typing_effect(f"{GREEN}✔ SUCCESSFULLY LOGGED IN!{RESET}")
            time.sleep(1)
            clear_screen()
            return True
        else:
            attempts -= 1
            typing_effect(f"{RED}❌ INCORRECT PASSWORD! {attempts} attempts left.{RESET}")

    typing_effect(f"\n{RED}❌ Too many failed attempts! EXITING...{RESET}")
    sys.exit()

password_prompt()

# Fake Boot Loading
loading_animation("Loading Secure Modules...", 3)

# Auto-Generated Conversation UID
conversation_uid = hashlib.sha256(str(time.time()).encode()).hexdigest()[:12]
typing_effect(f"{CYAN}✔ Conversation UID: {conversation_uid}{RESET}")

# Encrypted Chat System (Offline)
def encrypt_message(message):
    return hashlib.sha256(message.encode()).hexdigest()

def load_messages():
    if not os.path.exists("messages.txt"):
        typing_effect(f"{RED}❌ Message file not found! Creating sample messages...{RESET}")
        with open("messages.txt", "w") as file:
            file.write("Hello, this is a test message!\n")
            file.write("This chat is encrypted.\n")

    with open("messages.txt", "r") as file:
        messages = file.readlines()
    
    typing_effect(f"{YELLOW}✔ Loading Messages...{RESET}")
    time.sleep(1)

    encrypted_messages = [encrypt_message(msg.strip()) for msg in messages]
    for i, enc_msg in enumerate(encrypted_messages, 1):
        typing_effect(f"{BLUE}Message {i}: {enc_msg[:20]}...{RESET}")  # Show part of the hash

load_messages()

# Chat System
def chat():
    typing_effect(f"\n{GREEN}🔒 Encrypted Chat Started! Type 'exit' to quit.{RESET}")
    while True:
        user_msg = input(f"{CYAN}You: {RESET}")
        if user_msg.lower() == "exit":
            typing_effect(f"{RED}❌ Chat Session Ended!{RESET}")
            break
        encrypted_msg = encrypt_message(user_msg)
        typing_effect(f"{YELLOW}Bot: {encrypted_msg[:20]}...{RESET}")  # Encrypted Response

chat()
