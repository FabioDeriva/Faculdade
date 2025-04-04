public class Computador {
    public String marca;
    public float preco;
    public Hardware[] hard = new Hardware[3];
    public SistemaOperacional sist = new SistemaOperacional();
    public MemoriaUSB musb;

    public void MostraPCConfigs() {
        System.out.println("Marca = " + this.marca);
        System.out.println("Preço = R$ " + this.preco);
        for (int i = 0; i < hard.length; i++) {
            if (i == 0) {
                System.out.println(hard[i].nome + " - " + hard[i].capacidade + " Mhz");
                }
                else {
                    if (hard[i].capacidade >= 1000) {
                        System.out.println(hard[i].nome + " - " + hard[i].capacidade / 1000 + " TB");
                    } else {
                        System.out.println(hard[i].nome + " - " + hard[i].capacidade + " GB");
                    }
                }

        }
        System.out.println("Sistema Operacional = " + sist.nome + " (" + sist.tipo + "-bits)");

        if (musb != null) {
            if (musb.capacidade >= 1000) {
                System.out.println("Memória USB = " + musb.nome + " - " + (musb.capacidade / 1000) + " TB");
            } else {
                System.out.println("Memória USB = " + musb.nome + " - " + musb.capacidade + " GB");
            }
        } else {
            System.out.println("Nenhuma USBconectada.");
        }
    }
    public void addMemoria(MemoriaUSB musb) {
        this.musb = musb;
    }
}