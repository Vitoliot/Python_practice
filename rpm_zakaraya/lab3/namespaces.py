n = int(input())
a = {'global': {'vars' : 
    [], 'namespaces' :
        [],}}


def add(namespace, var):
    if var not in a[namespace]['vars']:
        a[namespace]['vars'].append(var)

 
def create(namespace, parent):
    if namespace not in a:
        a[namespace] = {} 
        a[namespace]['vars'] = []
        a[namespace]['namespaces'] = []
        a[namespace]['parent'] = parent
        a[parent]['namespaces'].append(namespace)

def get(namespace, var):
    for i in a[namespace]['vars']:
        if var == i : 
            return namespace
    if namespace == 'global':
        return None 
    return get(a[namespace]['parent'], var)

for i in range(n):
    com = input().split()
    if com[0] == 'add':
        add(com[1], com[2])
    if com[0] == 'create':
        create(com[1], com[2])
    if com[0] == 'get':
        print(get(com[1], com[2]))
