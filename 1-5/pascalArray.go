package main

import "fmt"

func makeArray(n int) []int {
	tmp := make([]int, n)
	for i := 0; i < n; i++ {
		tmp[i] = 1
	}
	return tmp
}

func pascalArray(n int) []int {
	prev := []int{1}
	for i := 2; i < n+1; i++ {
		tmp := makeArray(i)
		for j := 1; j < i-1; j++ {
			tmp[j] = prev[j] + prev[j-1]
		}
		prev = tmp
	}
	return prev
}

func main() {
	n := 5
	fmt.Println(pascalArray(n))
}
