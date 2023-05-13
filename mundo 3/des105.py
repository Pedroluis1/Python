def notas(*boletim, sit=False):
    dicio = {'Total': len(boletim), 'Maior': max(boletim), 'Menor':min(boletim), 'Média': sum(boletim)/len(boletim)}
    if sit:
        if sum(boletim)/len(boletim) < 6:
            dicio['Situação'] = 'Ruim'
        elif sum(boletim)/len(boletim) < 7:
            dicio['Situação'] = 'Razoável'
        elif sum(boletim)/len(boletim) < 8:
            dicio['Situação'] = 'Boa'
        else:
            dicio['Situação'] = 'Otima'
    print(dicio)
    

notas(5,4.4,8.9,sit=True)

''''def notas(*n, sit=False):
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n)/len(n)
    if sit:
        if sum(boletim)/len(boletim) < 6:
            dicio['Situação'] = 'Ruim'
        elif sum(boletim)/len(boletim) < 7:
            dicio['Situação'] = 'Razoável'
        elif sum(boletim)/len(boletim) < 8:
            dicio['Situação'] = 'Boa'
        else:
            dicio['Situação'] = 'Otima'
    return r


resp = notas(5,4.4,8.9,True)
print(resp)'''
#:>5.2f, :.<25, :.3f ( nesse exemplo não funcionou )

