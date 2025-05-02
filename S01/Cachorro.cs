using System;

class Cachorro{
    public string Nome { get; set; }
    public int Idade { get; set; }

    public Cachorro(string nome, int idade) {
        Nome = nome;
        Idade = idade;
    }

    public void MostrarNome() {
        Console.WriteLine($"O nome do cachorro é: {Nome}");
    }

    public virtual void ShowIdade() {
        Console.WriteLine($"A idade do cachorro é: {Idade}");
    }
}

class CachorroPequeno : Cachorro
{
    private string tamanho;
    public CachorroPequeno(string nome, int idade, string tamanho) : base(nome, idade) {
      this.tamanho = tamanho;
    }

    public override void ShowIdade() {
        Console.WriteLine($"Esse cachorrinho tem {Idade} anos!");
    }

    public string GetTamanho() {
          return tamanho;
      }
    
}

class CachorroGrande : Cachorro {
    private string tamanho;

    public CachorroGrande(string nome, int idade, string tamanho) : base(nome, idade){
        this.tamanho = tamanho;
    }

    public string GetTamanho(){
        return tamanho;
    }

    public override void ShowIdade() {
        Console.WriteLine($"Esse cachorrão tem {Idade} anos!");
    }
}

class Program{
    static void Main(string[] args)  {

        Cachorro cachorro = new Cachorro("Tobby", 3);
        CachorroPequeno pequeno = new CachorroPequeno("Loiro", 2, "Pequeno");
        CachorroGrande grande = new CachorroGrande("nina", 5, "Grande");
      
        Console.WriteLine("=== Cachorro ===");
        cachorro.MostrarNome();
        cachorro.ShowIdade();

        Console.WriteLine("\n=== Cachorro Pequeno ===");
        pequeno.MostrarNome();
        pequeno.ShowIdade();
        Console.WriteLine($"O tamanho do cachorro é: {pequeno.GetTamanho()}");

        Console.WriteLine("\n=== Cachorro Grande ===");
        grande.MostrarNome();
        grande.ShowIdade();
        Console.WriteLine($"O tamanho do cachorro é: {grande.GetTamanho()}");
    }
}
