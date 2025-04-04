import java.util.Scanner;

class ComputadorArray {
    private Computador[] pcs;
    private int tamanho;

    public ComputadorArray() {
        pcs = new Computador[5]; // Tamanho inicial
        tamanho = 0;
    }

    public void adicionarPC(Computador pc) {
        if (tamanho == pcs.length) {
            redimensionarArray();
        }
        pcs[tamanho++] = pc;
    }

    private void redimensionarArray() {
        Computador[] novoArray = new Computador[pcs.length * 2];
        for (int i = 0; i < pcs.length; i++) {
            novoArray[i] = pcs[i];
        }
        pcs = novoArray;
    }

    public void mostrarCompras() {
        for (int i = 0; i < tamanho; i++) {
            pcs[i].MostraPCConfigs();
            System.out.println("------------");
        }
    }

}

public class Main {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        Cliente cliente = new Cliente();

        System.out.println("Bem-vindo à PCmania!");
        System.out.println("Aproveite Nossas Promoções!\n");

        System.out.print("Digite seu nome: ");
        cliente.nome = entrada.nextLine();

        System.out.print("Digite seu CPF: ");
        cliente.cpf = entrada.nextLong();
        System.out.println();

        Computador pc1 = new Computador();
        pc1.marca = "Apple";
        pc1.preco = 396;
        pc1.hard[0] = new Hardware();
        pc1.hard[0].nome = "Pentium Core i3";
        pc1.hard[0].capacidade = 2200;
        pc1.hard[1] = new Hardware();
        pc1.hard[1].nome = "RAM";
        pc1.hard[1].capacidade = 8;
        pc1.hard[2] = new Hardware();
        pc1.hard[2].nome = "HD";
        pc1.hard[2].capacidade = 500;
        pc1.sist.nome = "Linux Ubuntu";
        pc1.sist.tipo = 32;
        pc1.musb = new MemoriaUSB();
        pc1.musb.nome = "Pendrive";
        pc1.musb.capacidade = 16;



        Computador pc2 = new Computador();
        pc2.marca = "Samsung";
        pc2.preco = 1630;
        pc2.hard[0] = new Hardware();
        pc2.hard[0].nome = "Pentium Core i5";
        pc2.hard[0].capacidade = 3370;
        pc2.hard[1] = new Hardware();
        pc2.hard[1].nome = "RAM";
        pc2.hard[1].capacidade = 16;
        pc2.hard[2] = new Hardware();
        pc2.hard[2].nome = "HD";
        pc2.hard[2].capacidade = 1000;
        pc2.sist.nome = "Windows 8";
        pc2.sist.tipo = 64;
        pc2.musb = new MemoriaUSB();
        pc2.musb.nome = "Pendrive";
        pc2.musb.capacidade = 32;

        Computador pc3 = new Computador();
        pc3.marca = "Dell";
        pc3.preco = 6074;
        pc3.hard[0] = new Hardware();
        pc3.hard[0].nome = "Pentium Core i7";
        pc3.hard[0].capacidade = 4500;
        pc3.hard[1] = new Hardware();
        pc3.hard[1].nome = "RAM";
        pc3.hard[1].capacidade = 32;
        pc3.hard[2] = new Hardware();
        pc3.hard[2].nome = "HD";
        pc3.hard[2].capacidade = 2000;
        pc3.sist.nome = "Windows 10";
        pc3.sist.tipo = 64;
        pc3.musb = new MemoriaUSB();
        pc3.musb.nome = "HD Externo";
        pc3.musb.capacidade = 1000;


        ComputadorArray pcsComprados = new ComputadorArray();

        int opcao;
        do {
            System.out.println("Menu:");
            System.out.println("1. Comprar PC 1");
            System.out.println("2. Comprar PC 2");
            System.out.println("3. Comprar PC 3");
            System.out.println("0. Sair");
            System.out.print("Escolha uma opção: ");
            opcao = entrada.nextInt();

            switch (opcao) {
                case 1:
                    cliente.CalculaTotalCompra(pc1);
                    pcsComprados.adicionarPC(pc1);
                    System.out.println("PC 1 adicionado ao seu carrinho.\n");
                    break;
                case 2:
                    cliente.CalculaTotalCompra(pc2);
                    pcsComprados.adicionarPC(pc2);
                    System.out.println("PC 2 adicionado ao seu carrinho.\n");
                    break;
                case 3:
                    cliente.CalculaTotalCompra(pc3);
                    pcsComprados.adicionarPC(pc3);
                    System.out.println("PC 3 adicionado ao seu carrinho.\n");
                    break;
                case 0:
                    break;
                default:
                    System.out.println("Ops, parece que sua opção não existe.");
                    System.out.println("Tente novamente.");
                    break;
            }
        } while (opcao != 0);

        System.out.println("\n\n");
        System.out.println("Obrigado Pela Preferencia, a PCmania Agradece!!! \n " + cliente.nome + "!");
        System.out.println("Seu Recibo");
        System.out.println("---------------------------------------------------------------------");
        pcsComprados.mostrarCompras();
        System.out.println("Total da compra: R$ " + cliente.CalculaTotalCompra(null));
        System.out.println("CPF do Cliente: " + cliente.cpf);
        System.out.println("VOLTE SEMPRE!");
        System.out.println("---------------------------------------------------------------------");
    }
}
