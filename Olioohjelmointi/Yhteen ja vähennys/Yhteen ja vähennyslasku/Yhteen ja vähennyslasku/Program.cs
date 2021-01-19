using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Yhteen_ja_vähennyslasku
{
    class Program
    {
        static void Main(string[] args)
        {
            string input = string.Empty;
            string nbr = string.Empty;
            int[] arr= new int[2];
            do
            {
                Console.Clear();
                Console.WriteLine("Yhteen vai vähennyslasku (+/-)");
                input = Console.ReadLine();
            }
            while (input != "-" && input != "+"); 

            for (int i = 0; i < 2; i++)
            {
                int val;
                do
                {
                    Console.Clear();
                    Console.WriteLine($"Anna luku {i + 1}.");
                    nbr = Console.ReadLine();
                } while (!Int32.TryParse(nbr, out val));
                arr[i] = val;
            }
            Console.WriteLine("Tulos {0}{1}{2}={3}",arr[0],input,arr[1],input == "+" ? arr[0] + arr[1] : arr[0] - arr[1]);
            Console.ReadLine();
        }
    }
}
