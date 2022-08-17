def zombie_shootout(zombies, distance, ammo): 
    if ammo < zombies:
        if ammo >= distance*2:
            return f"You shot {distance*2} zombies before being eaten: overwhelmed."
        else:
            return f"You shot {ammo} zombies before being eaten: ran out of ammo."          
    elif 2*distance < zombies:
        return f"You shot {distance*2} zombies before being eaten: overwhelmed."
    else:
        return f"You shot all {zombies} zombies."
