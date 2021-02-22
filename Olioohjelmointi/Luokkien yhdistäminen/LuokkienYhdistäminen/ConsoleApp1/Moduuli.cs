using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Moduuli
    {
        string Nimi { get; set; }
        List<Opettaja> opettajat = new List<Opettaja>();
        public Moduuli(string nimi)
        {
            Nimi = nimi;
        }

        public void LisääOpettaja(params Opettaja[] opet)
        {
            foreach(Opettaja opettaja in opet)
            {
                opettajat.Add(opettaja);
            }
        }

        public void Tulosta()
        {
            Console.WriteLine($"\tModuulin nimi on: {Nimi}.");
            Console.WriteLine("\tOpettajina moduulilla toimii:");
            foreach (var item in opettajat)
            {
                item.Tulosta();
                Console.WriteLine("\t\t------------");
            }
        }
    }
}
