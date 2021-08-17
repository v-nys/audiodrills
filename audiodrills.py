import os
import random
import sys
from pathlib import Path
from playsound import playsound
from rich import print

# gebruik: python audiodrills.py <locatie van map met wav files> <aantal herhalingen>

if __name__ == '__main__':
    input_dir = Path(sys.argv[1])
    repetitions_per_drill = int(sys.argv[2])
    audio_files = [f for f in os.listdir(input_dir) if f.endswith('.wav')]
    results = { audio_file: [False, 0] for audio_file in audio_files }
    todo = { audio_file for audio_file in audio_files }
    while len(todo):
        random_file = random.choice(list(todo))
        playsound(input_dir / random_file)
        answer = ''
        while answer not in ['j','n']:
            answer = input('Was je antwoord juist? (j/n)\n').lower()
        if answer == 'n':
            results[random_file][0] = True
        results[random_file][1] += 1
        if results[random_file][1] >= repetitions_per_drill:
            todo.remove(random_file)
    for result in results:
        if results[result][0]:
            print(f'[bold red]{result}[/bold red]')
        else:
            print(f'[bold green]{result}[/bold green]')
