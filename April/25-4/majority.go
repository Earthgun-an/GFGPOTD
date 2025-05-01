package main

import (
	"fmt"
	"math"
)

func Majority(arr []int) []int {
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
	n := math.Abs(float64(len(arr) / 2))
	for k := range mp {
		if mp[k] > int(n) {
			ans = append(ans, k)
		}
	}
	return ans
}

func main() {
	arr := []int{1, 1, 2, 1, 3, 5, 1}
	fmt.Println(Majority(arr))
}
