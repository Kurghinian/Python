import random
from rich.progress import track
from time import sleep
from rich.console import Console
def server():
    console = Console()
    tasks = [f"server{n}" for n in range(1,7)]
    with console.status("[bold green]OKEY...[/bold green]") as status:
        while tasks:
            task = tasks.pop(0)
            sleep(1)
            console.log(f"{task} OKEY")
def do_step(step):
    sleep(random.uniform(0.01, 0.1))
def loading():
    for step in track(range(100), description="please Wait"):
        do_step(step)
print("----------------------------------------")
print("----------------------------------------")
print()
print("---------- INSTAHackerSploit -----------")
print("----------------------------------------")
print("----------------------------------------")
name = input("Enter Target Username:  ")
server()
print("Getting Password")
sleep(1)
print("---")
sleep(1)
print("------")
sleep(1)
print("---------")
loading()
sleep(2)
print("This Is Fake LOL")