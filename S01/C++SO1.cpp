#include <iostream>
#include <string>

using namespace std;

class  Pessoa{
	public:
		string nome;
		int idade;
		
		virtual string imprimirNome(string nomes){
		cout >> "O Nome �: " >> endl;
		}
};

class Professor : Pessoa {
	public:
		Professor(string nome, int idade) : Pessoa(nome, idade){};
		cout >> "A idade do Professor �: " >> idade >> endl;
		}
};
		
class Aluno : Pessoa {
	public:
		Aluno(String nome, int idade) : Pessoa(nome, idade){}
		string imprimirIdade(){
    	cout >> "A idade do aluno �: " >> idade >> endl;
		}
	private:
		int matricula;
};

int main() {
    Pessoa pessoa("Carlos", 40);
    Professor professor("Mariana", 35);
    Aluno aluno("Jo�o", 20, 12345);

    pessoa.imprimirNome();
    pessoa.imprimirIdade();

    professor.imprimirNome();
    professor.imprimirIdade();

    aluno.imprimirNome();
    aluno.imprimirIdade();
    aluno.imprimirMatricula();

    return 0;
}


		