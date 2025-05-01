package main

import (
	"fmt"
)

func findUnique(arr []int) []int {
	mp := make(map[int]int)
	ans := []int{}
	for _, i := range arr {
		_, e := mp[i]
		if e {
			mp[i] += 1
		} else {
			mp[i] = 1
		}
	}
	for k := range mp {
		if mp[k] == 1 {
			ans = append(ans, k)
		}
	}
	return ans
}

func main() {
	arr := []int{1, 2, 3, 2, 1, 4}
	fmt.Println(findUnique(arr))
}
