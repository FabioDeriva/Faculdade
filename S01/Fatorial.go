package main

import (
	"fmt"
	"math/rand"
	)

func factorial(n int) int {
	if n <= 1 {
		return 1
	}
	return n * factorial(n-1)
}


func main() {
	var n = rand.Intn(10) + 1
	
	var f = factorial(n)
	
	fmt.Printf("Fatorial de %d é: %d\n", n, f)
}

