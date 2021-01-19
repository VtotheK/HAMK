using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Tervehtijä
{
    class Program
    {
        static void Main(string[] args)
        {
            Tervehtijä t = new Tervehtijä();
            t.AsetaTervehdys("Terve terve");
            t.Tervehdi();
            t.Tervehdi("Tässä oma tervehdys");
            Console.WriteLine("Haettu tervehdys: {0}",t.HaeTervehdys());
            Console.ReadLine();
        }
    }
    
    class Tervehtijä
    {
        string _tervehdys;

        public void AsetaTervehdys(string uusiTervehdys)
        {
            _tervehdys = uusiTervehdys;
        }

        
        public string HaeTervehdys()
        {
            return _tervehdys;
        }

        public void Tervehdi()
        {
            Console.WriteLine(_tervehdys);
        }
        public void Tervehdi(string omaTervehdys)
        {
            Console.WriteLine("Oma tervehdyksesi: {0}", omaTervehdys);
        }

    }
}
