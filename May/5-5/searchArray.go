package main

import "fmt"

func searchArray(arr []int, target int) int {
	for i, v := range arr {
		if v == target {
			return i
		}
	}
	return -1
}

func main() {
	arr := []int{10, 3, 40, 20, 50, 80, 70}
	target := 40
	fmt.Println(searchArray(arr, target))
}
