package main

import (
	"fmt"
)

func uniqueNumber(arr []int) int {
	mp := make(map[int]int)
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
			return k
		}
	}
	return 0
}

func main() {
	arr := []int{1, 2, 1, 5, 5}
	fmt.Println(uniqueNumber(arr))
}
