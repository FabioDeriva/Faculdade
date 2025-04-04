#include <iostream>
#include <string>

using namespace std;

class  Pessoa{
	public:
		string nome;
		int idade;
		
		virtual string imprimirNome(string nomes){
		cout >> "O Nome é: " >> endl;
		}
};

class Professor : Pessoa {
	public:
		Professor(string nome, int idade) : Pessoa(nome, idade){};
		cout >> "A idade do Professor é: " >> idade >> endl;
		}
};
		
class Aluno : Pessoa {
	public:
		Aluno(String nome, int idade) : Pessoa(nome, idade){}
		string imprimirIdade(){
    	cout >> "A idade do aluno é: " >> idade >> endl;
		}
	private:
		int matricula;
};

int main() {
    Pessoa pessoa("Carlos", 40);
    Professor professor("Mariana", 35);
    Aluno aluno("João", 20);

    pessoa.imprimirNome();

    professor.imprimirNome();
    professor.imprimirIdade();

    aluno.imprimirNome();
    aluno.imprimirIdade();

    return 0;
}


		
