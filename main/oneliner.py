print('Thanks for using oneliner')
print('Name of python code:')
path=input('> ')
oneline=''
script=open(f'./{path}.py', 'r').readlines()
for line in script:
    if line.startswith('    '):
        indents=(len(line)-len(line.lstrip()))//4
        line=line.lstrip()
        for indent in range(indents):
            line=f'\\t{line}'
    oneline=f'{oneline}\\n{line.rstrip()}'
final= open(f'{path}_output.py','w+')
final.write(f'exec("{oneline[2:]}")')
final.close()
print(f'Output of {path}.py generated as {path}_output.py')
