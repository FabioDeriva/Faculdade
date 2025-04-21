class Animal {
  constructor(nome, idade, especie) {
    this.nome = nome;
    this.idade = idade;
    this.especie = especie;
  }

  printInfo() {
    console.log(`Nome: ${this.nome}, Idade: ${this.idade}, Espécie: ${this.especie}`);
  }
}

class Cachorro extends Animal {
  #raca;

  constructor(nome, idade, especie, raca) {
    super(nome, idade, especie);
    this.#raca = raca;
  }

  printInfo() {
    console.log(`Nome: ${this.nome}, Idade: ${this.idade}, Espécie: ${this.especie}, Raça: ${this.#raca}`);
  }
}

class Gato extends Animal {
  constructor(nome, idade, especie, cores) {
    super(nome, idade, especie);
    this.cores = cores;
  }

  printInfo() {
    console.log(`Nome: ${this.nome}, Idade: ${this.idade}, Espécie: ${this.especie}, Cores: ${this.cores}`);
  }
}

const pet = new Animal("Nina", 3, "Cadela");
pet.printInfo();

const cão = new Cachorro("Rodolfo", 5, "Cachorro", "Pastor Alemão");
cão.printInfo();

const gatos = new Gato("Mimi", 2, "Gato", ["Preto", "Branco", "Cinza", "Laranja", "Amarelo"]);
gatos.printInfo();
