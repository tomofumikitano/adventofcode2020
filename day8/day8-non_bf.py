#!/usr/bin/env python3
from collection import defaultdict

def proc2b(data):
    # Give op, arg pairs
    code = parse_code(data)

    # Graph of all instructions that lead to a particular instruction.
    rev_jmp_tbl = defaultdict(set)

    for pc, (op, arg) in enumerate(code):
        src = pc
        dst = pc + 1
        if op == "jmp":
            dst = pc + arg
        rev_jmp_tbl[dst].add(src)

    # Traverse the graph to find all nodes leading to the end. The patched code
    # must result in jumping into this set.
    targets = set()
    edges = {len(code)}
    while edges:
        node = edges.pop()
        targets.add(node)
        edges |= rev_jmp_tbl[node] - targets

    # Run the machine, but check for the first jmp or nop which when patched
    # will put the pc into the target set.
    pc = 0
    acc = 0
    patched = False
    while pc != len(code):
        op, arg = code[pc]
        if not patched:
            # もし nop を jmp に変えたら targets にたどり着きそうなら
            if op == "nop" and (pc + arg) in targets:
                op = "jmp"
                patched = True
            elif op == "jmp" and (pc + 1) in targets:
                op = "nop"
                patched = True
        if op == "acc":
            acc += arg
            pc += 1
        elif op == "nop":
            pc += 1
        elif op == "jmp":
            pc += arg
    print(acc)
