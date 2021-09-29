print('Thanks for using oneliner.')
print('Name of python code:')
path=input('> ')
print('Number of spaces for indent (press Enter for default):')
spaces=input('> ')
if spaces=='':
    spaces=4
else:
    spaces=int(spaces)
oneline=''
script=open(f'./{path}.py', 'r').readlines()
for line in script:
    if line.startswith(' '):
        indents=(len(line)-len(line.lstrip()))//spaces
        line=line.lstrip()
        for indent in range(indents):
            line=f'\\t{line}'
    if line.startswith('#') or line.startswith('\\t#'):
        error=True
        while error==True:
            print(f'Comented region detected in {line.rstrip()}.\nUncomment(u) or Delete(d) line?:')
            result_1=input('> ')
            if result_1=='u':
                line=line.replace('#','')
                error=False
            elif result_1=='d':
                line=''
                error=False
            else:
                 print('Please give an avaliable answer (u or d)')
    if '"' in line:
        line=line.replace('"','\\"')
    if line=='':
        continue
    else:
        oneline=f'{oneline}\\n{line.rstrip()}'
final= open(f'{path}_output.py','w+')
final.write(f'exec("{oneline[2:]}")')
final.close()
print(f'Output of {path}.py generated as {path}_output.py')
