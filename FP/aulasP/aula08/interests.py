
def main():
    A = "reading"
    B = "eating"
    C = "traveling"
    D = "writing"
    E = "running"
    F = "music"
    G = "movies"
    H = "programming"
    type_of_interests = {A, B, C, D, E, F, G, H}
    interests = {
        "Marco": {A, D, E, F},
        "Anna": {E, A, G},
        "Maria": {G, D, E},
        "Paolo": {B, D, F},
        "Frank": {D, B, E, F, A},
        "Teresa": {F, H, C, D}
        }


    print("a) Table of common interests:")
    commoninterests = common_interests(interests)
    print(commoninterests)

    print("b) Maximum number of common interests:")
    maxCI, maxmatches = max_common(commoninterests)
    print(maxCI)

    print("c) Pairs with maximum number of matching interests:")
    print(maxmatches)

    print("d) Pairs with low similarity:")
    lowJaccard = ...
    ## Note que a similaridade de Jaccard entre dois conjuntos A e B é dada por
    ## |A ∩ B| / |A ∪ B|, onde |A| é o número de elementos de A.
    ## Portanto, a similaridade é baixa quando o conjunto de interesses em comum
    ## é pequeno em relação ao conjunto de interesses de ambos.
    ##############33 Não me apetece fazer isto agora ############
    print(lowJaccard)

## Criar um dicionário com os interesses comuns a cada par de pessoas. Ou seja, a cada
#par de pessoas, deve associar o conjunto dos interesses comuns a ambos. Note que
#se incluir o par (X, Y) não deve incluir (Y, X)

def common_interests(interests):
    common_dict = {}
    people = list(interests.keys())
    for i in range(len(people)):
        for j in range(i + 1, len(people)):
            person1 = people[i]
            person2 = people[j]
            common = interests[person1] & interests[person2]
            common_dict[(person1, person2)] = common
    return common_dict  

def max_common(commoninterests):
    maxCI = 0
    max_pars = []
    for k in commoninterests:
        if len(commoninterests[k]) > maxCI:
            maxCI = len(commoninterests[k])
            max_pars.append(k)
    return maxCI, max_pars

             
# Start program:
main()

