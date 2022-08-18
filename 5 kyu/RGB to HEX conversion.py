def rgb(r, g, b):

	def conversion(number):
        if number == 10:
            return "A"
        elif number == 11:
            return "B"
        elif number == 12:
            return "C"
        elif number == 13:
            return "D"
        elif number == 14:
            return "E"
        elif number == 15:
            return "F"

    #red = 14 -> hex = 0E
	#r_hex1 = E
	#r_hex2 = 0

	#red

	if 0 <= r <=15:
        r_hex2 = "0"
        if r > 9:
            r_hex1 = conversion(r)
        else:
            r_hex1 = str(r)
        r_hex = r_hex2 + r_hex1

    elif 16 <= r <= 255:
    	r_hex2 = r // 16
    	if r_hex2 > 9:
    		r_hex2 = conversion(r_hex2)
    	else:
    		r_hex2 = str(r_hex2)
    	r_hex1 = r % 16
    	if r_hex1 > 9:
    		r_hex1 = conversion(r_hex1)
    	else:
    		r_hex1 = str(r_hex1)
    	r_hex = r_hex2 + r_hex1

    else:
    	if r < 0:
    		r_hex = "00"
    	else:
    		r_hex = "FF"

    #green

    if 0 <= g <=15:
        g_hex2 = "0"
        if g > 9:
            g_hex1 = conversion(g)
        else:
            g_hex1 = str(g)
        g_hex = g_hex2 + g_hex1

    elif 16 <= g <= 255:
    	g_hex2 = g // 16
    	if g_hex2 > 9:
    		g_hex2 = conversion(g_hex2)
    	else:
    		g_hex2 = str(g_hex2)
    	g_hex1 = g % 16
    	if g_hex1 > 9:
    		g_hex1 = conversion(g_hex1)
    	else:
    		g_hex1 = str(g_hex1)
    	g_hex = g_hex2 + g_hex1

    else:
    	if g < 0:
    		g_hex = "00"
    	else:
    		g_hex = "FF"

	#blue

	if 0 <= b <=15:
        b_hex2 = "0"
        if b > 9:
            b_hex1 = conversion(b)
        else:
            b_hex1 = str(b)
        b_hex = b_hex2 + b_hex1

    elif 16 <= b <= 255:
    	b_hex2 = b // 16
    	if b_hex2 > 9:
    		b_hex2 = conversion(b_hex2)
    	else:
    		b_hex2 = str(b_hex2)
    	b_hex1 = b % 16
    	if b_hex1 > 9:
    		b_hex1 = conversion(b_hex1)
    	else:
    		b_hex1 = str(b_hex1)
    	b_hex = b_hex2 + b_hex1

    else:
    	if b < 0:
    		b_hex = "00"
    	else:
    		b_hex = "FF"

    #assembling
    rgb = r_hex + g_hex + b_hex
    return rgb

print(rgb(0,0,0)) #"000000"
print(rgb(1,2,3)) #"010203"
print(rgb(255,255,255)) #"FFFFFF"
print(rgb(254,253,252)) #"FEFDFC"
print(rgb(-20,275,125)) #"00FF7D"