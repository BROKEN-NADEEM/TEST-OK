import requests
import os
import sys
import time
import random
import json
from datetime import datetime
from colorama import Fore, Style
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TimeElapsedColumn

console = Console()

# क्लियर स्क्रीन
os.system('clear')

# Animated Logo Function
def print_animated_logo():
    logo = [
        "  _          _______    ______     _______    _______    _______",
        " ( (    /|  (  ___  )  (  __  \   (  ____ \  (  ____ \  (       )",
        " |  \  ( |  | (   ) |  | (  \  )  | (    \/  | (    \/  | () () |",
        " |   \ | |  | (___) |  | |   ) |  | (__      | (__      | || || |",
        " | (\ \) |  |  ___  |  | |   | |  |  __)     |  __)     | |(_)| |",
        " | | \   |  | (   ) |  | |   ) |  | (        | (        | |   | |",
        " | )  \  |  | )   ( |  | (__/  )  | (____/\  | (____/\  | )   ( |",
        " |/    )_)  |/     \|  (______/   (_______/  (_______/  |/     \|"
    ]
    
    for line in logo:
        console.print(f"[cyan]{line}[/cyan]")
        time.sleep(0.2)

print_animated_logo()

console.print("[bold green]𝗠𝗨𝗟𝗧𝗬 𝗣𝗢𝗦𝗧 𝗖𝗢𝗠𝗠𝗘𝗡𝗧𝗦 𝗧𝗢𝗢𝗟 𝗙𝗨𝗟𝗟 𝗪𝗢𝗥𝗞𝗜𝗡𝗚[/bold green]")

# Password Animation
def password_input():
    console.print("[yellow]𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗 𝗩𝗘𝗥𝗜𝗙𝗜𝗖𝗔𝗧𝗜𝗢𝗡...[/yellow]")
    with Progress(SpinnerColumn(), BarColumn(), TimeElapsedColumn()) as progress:
        task = progress.add_task("Verifying...", total=100)
        for _ in range(100):
            time.sleep(0.02)
            progress.update(task, advance=1)
    
    password = input("\033[1;32m𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗➜ ")
    correct_password = "your_password_here"  # Replace with actual password checking logic
    if password != correct_password:
        console.print("[red]𝗜𝗡𝗖𝗢𝗥𝗥𝗘𝗖𝗧 𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗![/red]")
        sys.exit()

password_input()

# Delay Animation
def countdown_timer(seconds):
    for i in range(seconds, 0, -1):
        console.print(f"[yellow]Repeating in {i} seconds...[/yellow]", end="\r")
        time.sleep(1)

# Comment Sending Animation
def send_comment(user_id, message):
    with Progress(SpinnerColumn(), BarColumn(), TimeElapsedColumn()) as progress:
        task = progress.add_task(f"Sending Comment to {user_id}...", total=100)
        for _ in range(100):
            time.sleep(0.03)
            progress.update(task, advance=1)

    console.print(f"[green]Comment sent to {user_id}: {message}[/green]")

# Main Loop
while True:
    user_id = "1234567890"  # Example User ID
    message = "Hello, this is a test comment!"
    
    send_comment(user_id, message)

    countdown_timer(10)  # 10 सेकंड का काउंटडाउन
