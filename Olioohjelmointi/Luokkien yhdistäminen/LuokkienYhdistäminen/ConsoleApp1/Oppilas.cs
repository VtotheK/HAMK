using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Oppilas
    {
        string Nimi { get; set; }
        List<Moduuli> moduulit = new List<Moduuli>();

        public Oppilas(string nimi)
        {
            Nimi = nimi;
        }

        public void LisääModuuli(params Moduuli[] moduuli)
        {
            foreach (Moduuli item in moduuli)
            {
                moduulit.Add(item);
            }
        }

        public void Tulosta()
        {
            Console.WriteLine($"Oppilas {Nimi}");
            Console.WriteLine("------------");
            foreach (var item in moduulit)
            {
                item.Tulosta();
            }
        }
    }
}
