""" Made by bypequeno / https://github.com/bypequeno/oneliner
Simple cli applicatiom made in python to one-linize yor python code."""

#CLI library:

from fire import Fire as cli

#Some definitions for easy printing:

def logo():
    print(' _____             __    _\n|     |___ ___ ___|  |  |_|___ ___ ___\n|  |  |   | -_|___|  |__| |   | -_|  _|\n|_____|_|_|___|   |_____|_|_|_|___|_|\nThanks for using oneliner!\n')
def error(reason='Unknown',e='Unknown',tip='Unkown'):
    print(f'There was an error doing the operation!\n  Reason: {reason}\n  Exception name: {e}\n  Tip: {tip}\nFor any further help, post an issue at https://github.com/bypequeno/oneliner\n')

#Main code

def main(path=False,spaces=4,deletion='yes'):
    logo()
    if deletion=='yes':comention='no'
    if deletion=='no':comention='yes'
    oneline=''
    print(f'  - Spaces set as: {spaces}\n  - Commented regions deletion: {deletion}\n  - Commented regions commention: {comention}\n')
    spaces=int(spaces)
    try:
        script=open(path, 'r').readlines()
    except Exception as e:
        error('Unavaliable python file path.',e,'Check if path is written correctly.')
        return
    for line in script:
        if line.startswith(' '*spaces):
            indents=(len(line)-len(line.lstrip()))//spaces
            line=line.lstrip()
            for indent in range(indents):
                line=f'\\t{line}'
        if line.startswith('#') or '\\t#' in line:
                if deletion=='yes': continue
                else:
                    line.replace('#','')
                    line=f'"""{line}"""'
        if '"' in line:
            line=line.replace('"','\\"')
        if line=='': #Just in case
            continue
        else:
            oneline=f'{oneline}\\n{line.rstrip()}'
    final=open(f'{path[:-3]}_output.py','w+')
    final.write(f'exec("{oneline[2:]}")')
    final.close()
    print(f'Output of {path} generated as {path[:-3]}_output.py')

if __name__=='__main__':
    cli(main)
