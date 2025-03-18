use std::io;

fn main() {

  let mut n1_entrada = String::new();
  let mut n2_entrada = String::new();
  let mut operador= String::new();
  let mut result: i32;
  let mut n1: i32;
  let mut n2: i32;
  let mut button_entrada = String::new();
  let mut button: i32;

  loop {
  println!("Digite um numero: ");
  io::stdin().read_line(&mut n1_entrada).expect("A leitura falhou");
  println!("Digite outro numero: ");
  io::stdin().read_line(&mut n2_entrada).expect("A leitura falhou");

  println!("Digite o operador: + ou *");
  io::stdin().read_line(&mut operador).expect("A leitura falhou");
  

  n1 = n1_entrada.trim().parse().expect("A conversão falhou");
  n2 = n2_entrada.trim().parse().expect("A conversão falhou");

 
  if operador.trim() == "+"{
    result = n1 + n2 ;
    println!("A Soma de {} + {} =  {} ", n1, n2, result);
  }
  else {
    result = n1 * n2 ;
   println!("o Produto de {} * {} = {} ", n1, n2, result) 
}

 println!("Digite -1 para sair ou qualquer outro numero para continuar" );
 io::stdin().read_line(&mut button_entrada).expect("A leitura falhou");

button = button_entrada.trim().parse().expect("A conversão falhou");

      if button == -1 {
        break;
      } 
}

    }

//não sei pq, mas quando eu coloquei as variaveis dentr de um loop, o programa não rodava,e apontava q as variaveis deviam ser mutaveis, dai transformei todas em mutaveis e deu certo.