using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            Oppilas ville = new Oppilas("Ville");
            Oppilas laura = new Oppilas("Laura");
            Moduuli tekniikanViestintä = new Moduuli("Tekniikan viestintä 2");
            Moduuli mekaniikka = new Moduuli("Mekaniikka");
            Moduuli ohjelmointi = new Moduuli("Olio-ohjelmointi");
            Opettaja lea = new Opettaja("Lea Mustonen");
            Opettaja jukka = new Opettaja("Jukka Varrio");
            Opettaja toni = new Opettaja("Toni Laitinen");

            mekaniikka.LisääOpettaja(jukka);
            tekniikanViestintä.LisääOpettaja(toni);
            ohjelmointi.LisääOpettaja(lea);

            laura.LisääModuuli(mekaniikka, ohjelmointi);
            ville.LisääModuuli(mekaniikka,ohjelmointi,tekniikanViestintä);
            ville.Tulosta();
            Console.ForegroundColor = ConsoleColor.Cyan;
            Console.WriteLine("-------------------------------------------------");
            Console.ForegroundColor = ConsoleColor.White;
            laura.Tulosta();
            Console.ReadLine();
        }
    }
}
