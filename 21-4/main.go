/*
You are given an array arr[] of size n - 1 that contains distinct integers in the range from 1 to n (inclusive).
This array represents a permutation of the integers from 1 to n with one element missing.
Your task is to identify and return the missing element.

Examples:

Input: arr[] = [1, 2, 3, 5]
Output: 4
Explanation: All the numbers from 1 to 5 are present except 4.

Input: arr[] = [8, 2, 4, 5, 3, 7, 1]
Output: 6
Explanation: All the numbers from 1 to 8 are present except 6.


Input: arr[] = [1]
Output: 2
Explanation: Only 1 is present so the missing element is 2.
*/

package main

import (
	"fmt"
)

func findMax(arr []int) int {
	var max_element = arr[0]
	for _, val := range arr {
		if val > max_element {
			max_element = val
		}
	}
	return max_element
}

func findSum(arr []int) int {
	s := 0
	for _, val := range arr {
		s += val
	}
	return s
}

func missingNum(arr []int) int {
	n := findMax(arr)
	fmt.Println("max is ", n)
	s := (n * (n + 1)) / 2
	t := s - findSum(arr)
	if t == 0 {
		return n + 1
	}
	return t
}

func main() {
	arr := []int{1}
	var x = missingNum(arr)
	fmt.Println("Solution is ", x)
}
