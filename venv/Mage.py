import sys

# stores computed of silverhour index (copper, bronze)
computed = {}

def goldenHour(day):
    # rule 1
    return (silverHour(day, day) - 1) % 12 + 1

def silverHour(copper, bronze):
    # if already computed, return result and exit early
    if (copper, bronze) in computed:
        return computed[(copper, bronze)]
    # rule 2
    elif copper == 1:
        computed[(copper, bronsze)] = 1
        return computed[(copper, bronze)]
    # rule 3
    elif copper == bronze:
        computed[(copper-1, bronze)] = silverHour(copper - 1, bronze) 
        return computed[(copper -1, bronze)] + 1
    # rule 4
    elif copper > bronze:
        return goldenHour(bronze)
    # rule 5
    elif bronze > copper:
        computed[(copper, bronze - copper)] = silverHour(copper, bronze - copper)
        computed[(copper - 1, bronze)] = silverHour(copper - 1, bronze)
        return computed[(copper, bronze - copper)] + computed[(copper -1, bronze)]

if len(sys.argv) == 2:
    day = int(sys.argv[1])

    print(goldenHour(day))


