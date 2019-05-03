import java.util.*;

public class Assn13{
	public static void main(String[] args){
		System.out.print("i. Floating point number converter.\n");
		float pi = (float) 3.14159265358979;
		System.out.print(pi + " -> " + convertFloat(pi) + "\n");

		System.out.print( "\nii. Floating point number enumeration.\n");
		float fp = (float) 0.0;
		int i = 0;
		while (fp < 1.4E-44){
			System.out.print((++i) + ("th number: ") + (fp = nextFloat(fp)) + "\n");
		}

		System.out.print("\niii. Floating point number counting\n"); 
		int posFPs = countBetween((float) 0.0, Float.MAX_VALUE);
		int zeroOneFPs = countBetween((float)0.0, (float) 1.0);
		System.out.print("Number of positive floating point numbers: " + posFPs + "\n");
		System.out.print("Number of floating point numbers between 0 and 1: " + zeroOneFPs + "\n");
		System.out.print("Proportion (# of 0~1) / (# of positive): " + ((double) zeroOneFPs / (double) posFPs * 100.0) + "%\n");
	}

	static String convertFloat(float number){
		int num = Float.floatToIntBits(number);// converts float (number) to floating-point number bits
        int signBit = (num & 0x80000000) >> 31;// gets sign bit 31
        int exponentBits = (num & 0x7f800000) >> 23;// gets exponent bits 30-23
        int mantissaBits = (num & 0x007fffff);// gets mantissa bits 22-0
		return '(' + Integer.toString(signBit) + ", " + Integer.toString(exponentBits) + ", " + Integer.toString(mantissaBits) + ')';// returns float as a String
	}

     static float nextFloat(float number){
        int theNumber = Float.floatToIntBits(number);// converts float (number) to floating-point number bits
		int theAnswer = ((theNumber & 0x007fffff) + 0x00000001);// go to the next float by adding one 
		float getFloat = Float.intBitsToFloat(theAnswer);// convert to float
        return getFloat;// return the solution
     }

	static int countBetween(float lower, float upper){
		int theLowerValue = Float.floatToIntBits(lower);// converts float (lower) to floating-point number bits
		int theUpperValue = Float.floatToIntBits(upper);// converts float (upper) to floating-point number bits
		return theUpperValue - theLowerValue;// subtract the values of the upper and lower and return the result
	}
}