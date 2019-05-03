function convertFloat(number){
    var buffer = new ArrayBuffer(4); //making a byte buffer 
    var floatBuffer = new Float32Array(buffer);
    floatBuffer.fill(number); //we are filling the buffer with the number that is passed in as an argument 
    var uInt =new Uint32Array(buffer); //getting the unsigned int form of the numbers 
    var signBit =  (uInt & 0x80000000) >>> 31; //getting sign bit 31 
    var exponentBit =   (uInt & 0x7f800000) >>> 23; //gets exponent bits 30-23
    var mantissaBit =  (uInt & 0x007fffff); //get mantissa bits 22-0
    return ("(" +signBit+","+exponentBit+","+mantissaBit+")");   
};

function nextFloat(number){
var buffer = new ArrayBuffer(4); //create byte buffer 
var floatBuffer = new Float32Array(buffer);
floatBuffer.fill(number); //flling the buffer with the value 
var intBuffer = new Uint32Array(buffer);
intBuffer.fill(intBuffer[0]+1); //increment to next float 
return floatBuffer;
};

function countBetween(lower, upper){
    var buffer = new ArrayBuffer(4); //create byte buffer 
    var floatBuffer = new Float32Array(buffer);
    floatBuffer.fill(lower); //fill buffer with the floating point number 
    var intBuffer = new Uint32Array(buffer);
    var lowerUInt = intBuffer[0]; //retrieve the unsigned int number for lower 
    floatBuffer.fill(upper); //fill buffer with the floating point number 
    var upperUInt = intBuffer[0]; //retrieve the unsigned int number for upper 
    return upperUInt - lowerUInt;
};



console.log("i. Floating point number converter.\n");
	var pi = 3.14159265358979;
	console.log(pi + " -> " + convertFloat(pi));


console.log("\nii. Floating point number enumeration.\n");
	fp = 0.0;
	var i = 0;
	while (fp < 1.4e-44) {
        console.log(++i + "th number: "+ (fp = nextFloat(fp)));
    }

    
	console.log("\niii. Floating point number counting\n");
	var posFPs = countBetween(0.0, 3.40282346638528860E38);
	var zeroOneFPs = countBetween(0.0, 1.0);
	console.log("Number of positive floating point numbers: "+posFPs);
	console.log("Number of floating point numbers between 0 and 1: " + zeroOneFPs);
	console.log("Proportion (# of 0~1) / (# of positive): " + zeroOneFPs / posFPs * 100.0 +"%\n");
    