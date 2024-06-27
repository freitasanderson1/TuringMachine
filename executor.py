import hashlib

def hash_code(code):
    return hashlib.md5(code.encode()).hexdigest()

def HashExiste(code, filename='t1.hashes'):
    codigoEmHash = hash_code(code)
    with open(filename, 'r') as f:
        allowed_hashes = f.read().splitlines()
    return codigoEmHash in allowed_hashes, codigoEmHash

def execute_turing_machine(tape, code):
    tape = list(tape)
    controlStep = 0
    steps = []

    for index,step in enumerate(tape):
      if step == '1' and index-1 >= 0 and tape[index-1] != '.':
          controlStep = '0'
      elif step == '1' and tape[index+1] == '.':
          controlStep = step
          steps[index-1] = '1'
      else:
          controlStep = step
      steps.append(controlStep)
    return steps

def print_steps(steps,tape):
    for index, step in enumerate(steps):
        print(f"{index+1} fita: {tape}")
        print(" " * (7 + (index + 1 if index < 10 else index + 2)) + "*")

    print(f'Output: {"".join(steps)}')

if __name__ == "__main__":
    import sys

    code = input('Insira seu código: ')

    codigoPermitido, codigoEmHash = HashExiste(code)
    
    if not codigoPermitido:
        print(f"Não permitido, hash: {codigoEmHash} não foi encontrado no arquivo t1.hashes (\"código corrompido/não autorizado não será executado.\")")
        sys.exit(1)
    
    print(f"Ok, hash é {codigoEmHash} e foi encontrado em t1.hashes")

    tape = input('Insira sua a fita: ')

    print("Ok, processando...\n")


    steps = execute_turing_machine(tape, code)
    print_steps(steps, tape)
