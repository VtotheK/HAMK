using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Opettaja
    {
        string Nimi { get; set; }

        public Opettaja(string nimi)
        {
            Nimi = nimi;
        }

        public void Tulosta()
        {
            Console.WriteLine($"\t\t{Nimi}");
        }
    }
}
