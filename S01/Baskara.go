package main

import (
	"fmt"
	"math"
	)
	
func main() {

  var a , b , c float64

	fmt.Print("Digite o valor de a:")
	fmt.Scan(&a)
	
	fmt.Print("Digite o valor de b:")
	fmt.Scan(&b)
	
	fmt.Print("Digite o valor de c:")
	fmt.Scan(&c)

	delta := b*b - 4*a*c

	if delta < 0 {
		fmt.Println("Delta negativo")
		return 
	}
	
	x1 := (-b + math.Sqrt(delta)) / (2*a)
	x2 := (-b - math.Sqrt(delta)) / (2*a)
 
	fmt.Println("raiz 1:",x1)
	fmt.Print("raiz 2:",x2)
}
