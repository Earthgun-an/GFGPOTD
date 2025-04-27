package main

import (
	"fmt"
	"strconv"
)

func removeZero(s string) string {
	for s[0] == '0' {
		s = s[1:]
	}
	return s
}

func mutliplyStrings(s1 string, s2 string) string {
	neg := false
	if s1[0] == '-' {
		neg = !neg
		s1 = s1[1:]
	}
	if s2[0] == '-' {
		neg = !neg
		s2 = s2[1:]
	}
	n1 := len(s1)
	n2 := len(s2)
	prod := make([]int, n1+n2)
	for i := n2 - 1; i > -1; i-- {
		digit1, _ := strconv.Atoi(string(s2[i]))
		carry := 0

		for j := n1 - 1; j > -1; j-- {
			digit2, _ := strconv.Atoi(string(s1[j]))
			prod[i+j+1] = (digit2 * digit1) + carry
			carry = int(prod[i+j+1] / 10)
			prod[i+j+1] = prod[i+j+1] % 10
		}
		next_index := i
		for carry > 0 {
			prod[next_index] += carry
			carry = int(prod[next_index] / 10)
			prod[next_index] = prod[next_index] % 10
			next_index -= 1
		}
	}
	ans := ""
	for _, v := range prod {
		ans += strconv.Itoa(v)
	}
	ans = removeZero(ans)
	if neg {
		return "-" + ans
	}
	return ans
}

func main() {
	s1 := "0010"
	s2 := "44"
	fmt.Println(mutliplyStrings(s1, s2))
}
