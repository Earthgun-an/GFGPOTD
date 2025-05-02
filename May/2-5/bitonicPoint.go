package main

import (
	"fmt"
)

func bitonicPoint(arr []int) int {
	max_num := arr[0]
	for i := 1; i < len(arr); i++ {
		if max_num < arr[i] {
			max_num = arr[i]
		}
	}
	return max_num
}

func main() {
	arr := []int{1, 2, 4, 5, 7, 8, 3}
	fmt.Println(bitonicPoint(arr))
}
