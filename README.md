# IEEE754_FloatingPoint

Draw a distribution of 32-bit IEEE 754 floating point numbers.

i. Find the Assn11.cpp and Assn11.py.

ii. YouareaskedtoimplementthefunctionconvertFloat,nextFloatandcountBetween in Assn11.cpp.

iii. You can refer Figure 1 and this site to have a high level idea of the IEEE 754 format.

Expected output
   g++ Assn11.cpp -o Assn11.exe; .\Assn11.exe count.dat
   i. Floating point number converter.
   3.14159 -> (0,128,4788187)
   ii. Floating point number enumeration.
   1th number: 1.4013e-045
   2th number: 2.8026e-045
   3th number: 4.2039e-045
   4th number: 5.60519e-045
   5th number: 7.00649e-045
   6th number: 8.40779e-045
   7th number: 9.80909e-045
   8th number: 1.12104e-044
   9th number: 1.26117e-044
   10th number: 1.4013e-044
   iii. Floating point number counting
   Number of positive floating point numbers: 2139095039
   Number of floating point numbers between 0 and 1: 1065353216
   Proportion (# of 0~1) / (# of positive): 49.8039%
   iv. Floating point number distribution
   The output file is ready. Execute "Python3 Assn11.py count.dat"
