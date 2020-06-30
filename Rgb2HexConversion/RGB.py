def rgb(r, g, b):
    rgb2hex = lambda r,g,b: f"#{r:02x}{g:02x}{b:02x}"
    convertion = rgb2hex(r,g,b)
    return convertion.upper()



print(rgb(0,0,0)) # Return: "000000", "testing zero values"
print(rgb(1,2,3)) # Return: "010203", "testing near zero values"
print(rgb(255,255,255)) # Return:  "FFFFFF", "testing max values"
print(rgb(254,253,252)) # Return:  "FEFDFC", "testing near max values"
print(rgb(-20,275,125)) # Return:  "00FF7D", "testing out of range values"