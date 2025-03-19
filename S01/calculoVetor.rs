fn preenche_arr(arr: &mut [i32; 10], x: i32) {
  for i in 0..10 {
      arr[i] = i as i32 * x;
  }
}

fn main() {
  let mut arr = [0; 10]; 
  let teste = 10; 

  preenche_arr(&mut arr, teste);

   for num in arr {
          print!("{}|", num);
      }
  }


