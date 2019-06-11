using System;
using System.Linq;
using static System.Console;

namespace Triangle
{
    class Program
    {
        static void Main(string[] args)
        {
            int start = 0;
            string concation;
            WriteLine("Please type the symbol you want to see being built: ");
            String UserSymbol = ReadLine();


            for (start = 0; start <= 10; start++)
            {
                concation = String.Concat(Enumerable.Repeat(UserSymbol, start));
                WriteLine(concation);
            }
            for (start = 10; start > 0; start--)
            {
                concation = String.Concat(Enumerable.Repeat(UserSymbol, start));
                WriteLine(concation);
            }

            for (start = 10; start > 0; start--)
            {
                concation = String.Concat(Enumerable.Repeat(UserSymbol, start));
                WriteLine(concation);
            }
            for (start = 0; start <= 10; start++)
            {
                concation = String.Concat(Enumerable.Repeat(UserSymbol, start));
                WriteLine(concation);
            }
        }
    }
}
