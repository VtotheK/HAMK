using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Keskiarvo
{
    class Program
    {
        static void Main(string[] args)
        {
            uint count;
            int sum = 0;
            float avg;
            do
            {
                Console.Clear();
                Console.WriteLine("Montako lukua");
            }
            while (!UInt32.TryParse(Console.ReadLine(), out count));

            for (int i = 0; i < count; i++)
            {
                int val;
                do
                {
                    Console.Clear();
                    Console.WriteLine($"Anna luku {i+1}");
                }
                while (!Int32.TryParse(Console.ReadLine(), out val));
                sum += val;
            }

            avg = sum / (float)count;
            Console.WriteLine($"Average of your numbers are {avg}");
            Console.ReadLine();
        }
    }
}
