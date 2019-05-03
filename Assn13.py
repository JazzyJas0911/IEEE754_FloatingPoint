import struct

def convertFloat (number):
    #using the struct library interpret a string as packed binary data. allowing me to manipulate the bits
    num = struct.unpack('I', struct.pack('f', number))[0]
    
    #gets sign bit 31
    signBit = (num & 0x80000000) >> 31
    
    #gets exponent bits 30-23
    exponentBits =  (num & 0x7f800000) >> 23
    
    #gets mantissa bits 22-0
    mantissaBits = (num & 0x007fffff)
    
    #returns the float in the correct format
    return '(' + str(signBit) + "," + str(exponentBits) + "," + str(mantissaBits) + ')'


def nextFloat (number):
    #formatting the number
    num = struct.unpack('I', struct.pack('f', number))[0]
    
    #incrementing num to the next number
    nextNum = num + 1
    
    # returning the incremented formatted number
    return (struct.unpack('f', struct.pack('I', nextNum)))[0]

def countBetween (lower, upper):
    #reading in both numbers in the correct formatting and subtracting them
    theLowerValue = struct.unpack('I', struct.pack('f', lower))[0]
    theUpperValue = struct.unpack('I', struct.pack('f', upper))[0]
    return (theUpperValue - theLowerValue)

def main():
    #given main statements
    
    #part 1
    print("i. Floating point number converter.")
    pi = 3.14159265358979
    print("3.14159 -> ", convertFloat(pi))
    
    #part 2
    print("\nii. Floating point number enumeration.")
    fp = 0.0
    i = 0
    while fp < 1.4E-44:
        #must calculate these before hand to use the str() method in order for an out of bounds to not be thrown
        fp = nextFloat(fp)
        i = i + 1
        print (str(i), "th number: ", str(fp))
    
    #part 3
    print("\niii. Floating point number counting")
    #max value store in a float
    posFPs = countBetween(0.0, 3.4028235E38)  
    zeroOneFPs = countBetween(0.0, 1.0)
    print("Number of positive floating point numbers:", str(posFPs))
    print("Number of floating point numbers between 0 and 1:", str(zeroOneFPs))
    print("Proportion (# of 0~1) / (# of positive):", str(float(zeroOneFPs) / float(posFPs) * 100.0), "%")




main()