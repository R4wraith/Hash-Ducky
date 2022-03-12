import vt
import easygui
import time
import os
from rich.console import Console
from rich import inspect
import rich
from rich.progress import track
from time import sleep
from contextlib import redirect_stdout
from datetime import date    

"""
requirements.txt
vt-py
easygui
rich

"""

today = date.today().isoformat()
console=Console()
clinet=""
logo= """


    __  __           __          ____             __        
   / / / /___ ______/ /_        / __ \__  _______/ /____  __
  / /_/ / __ `/ ___/ __ \______/ / / / / / / ___/ //_/ / / /
 / __  / /_/ (__  ) / / /_____/ /_/ / /_/ / /__/ ,< / /_/ / 
/_/ /_/\__,_/____/_/ /_/     /_____/\__,_/\___/_/|_|\__, /  
                                                   /____/   



"""
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
def process_data():
    sleep(0.02)


def regular_app():
	global client
	console.print(f"[bold yellow] \nYour REST.v3 API key has been set to:\n[bold green] defualt.")
	time.sleep(3)
	client = vt.Client("enter your api key-here!")

def client_app(api_key):
	console.print(f"[bold yellow] \nYour REST.v3 API key has been set to:\n{api_key}")
	client = vt.Client(api_key)

def lens_to_check(files_hashes):
	num_lines = sum(1 for line in open(files_hashes))
	return num_lines

def list_of_hashes(files_hashes):
	hashes_list=[]
	with open(files_hashes) as file:
		for line in file:
		 line=line.replace("\n","")
		 hashes_list.append(line)
	return hashes_list

def md5_graber(file_to_scan):
	clearConsole()
	json_toload=""
	console.print(f"[bold green]{logo}\n[bold red] Generating request to VT-Api ..")
	length_scan=lens_to_check(file_to_scan)
	original_hash_list=list_of_hashes(file_to_scan)
	time2 = format((length_scan*0.4), ".2f")
	console.print(f"[bold yellow]Total of [bold red]{length_scan} [bold yellow] hashes to scan,\nEstimated time for the request : [bold red]{time2} minutes.")
	for file in original_hash_list:
		try:
			index = original_hash_list.index(file)
			file = client.get_object(f"/files/{file}")
			client.close()
			with open(f'hash_ducky_output_md5_{today}.txt', 'a') as f:	
				with redirect_stdout(f):
					print(file.md5)
			for _ in track(range(400), description='[green]Generating next request'):
				process_data()
			console.print(f"[bold yellow]Hash number {index+1} finished.")
		except:
				console.print(f"[bold yellow]Unfortunately there was an [bold red]ERROR.\n [bold yellow]the hash [bold red]{file} [bold yellow]was not found in VT.\nSaving to log and continue with the next one")
				with open(f'hash_ducky_output_md5_{today}.txt', 'a') as f:	
					with redirect_stdout(f):
						print(f"{file} - Hash was not found in VT! ")
				pass
	clearConsole()
	time.sleep(4)
	console.print(f"[bold green]{logo}")
	console.print(f"[bold yellow]Thanks for using hash-ducky.\nOutput file has been saved to {os.getcwd()} as hash_ducky_output_md5_{today}.txt")
	time.sleep(3)
	main()






def main():
	clearConsole()
	console.print(f"[bold green]{logo}")
	for _ in track(range(100), description='[green]Loading Scripts'):
		process_data()
	inspect(rich)
	time.sleep(1)
	inspect(easygui)
	time.sleep(0.25)
	inspect(vt)
	time.sleep(0.5)
	inspect(os)
	console.print(f"[bold green] Successfully loaded [bold red] All scripts..")
	console.print(f"[bold green]{logo}\n[bold red] loading main app ..")
	time.sleep(2)
	api_choose=console.input(f"[bold yellow]Use the original API provided?")

	if api_choose.lower() == "yes":
		clearConsole()
		console.print(f"[bold green]{logo}")
		regular_app()

	elif api_choose.lower() == "no":
		api_from_user=console.input(f"[bold yellow] Please enter your api key:\n")
		client_app(api_from_user)
		time.sleep(3)

	else:
		console.print(f"[bold yellow]{api_choose} is not a valid answer. reloading scrpit from scratch again.")
		time.sleep(3)
		main()

	clearConsole()
	console.print(f"[bold green]{logo}\n[bold red] loading file to scan")
	console.print(f"[bold yellow] A check box will open in 5 secounds. please choose the text file to scan.\n")
	#time.sleep(5)
	file_to_scan = easygui.fileopenbox()
	while not file_to_scan :
		console.print("[bold red]You didnt choose any file! try again.")
		time.sleep(1.5)
		file_to_scan = easygui.fileopenbox()
	console.print(f"[bold yellow]\nThis file has been choosen : \n{file_to_scan}")
	md5_graber(file_to_scan)


if __name__ == '__main__':
	main()


