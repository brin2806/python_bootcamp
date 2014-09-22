def celsius(F):
	return (F-32)*5/9

def farenheit(C):
	return C*9/5 +32

print ('{} degrees F = {} degrees C'.format(72,celsius(72)))
print ('{} degrees C = {} degrees F'.format(37,farenheit(37)))
