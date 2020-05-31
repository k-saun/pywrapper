using System;
using System.Dynamic;

namespace library
   {
      public class DynamicCalc: DynamicObject
      {
          Calculator calc;
          public DynamicCalc()
         {
              calc = new Calculator();
         }

         public double add(double a, double b) {
            return calc.add(a, b);
            }

        public double sub(double a, double b) {
            return calc.sub(a, b);
            }
        
      }
   }