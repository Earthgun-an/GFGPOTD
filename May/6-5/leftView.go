package main

import "fmt"

type Node struct {
	value int
	left  *Node
	right *Node
}

func solve(m *Node, ans *[]int, l int) {
	if m == nil {
		return
	}
	if l == len(*ans) {
		*ans = append(*ans, m.value)
	}

	solve(m.left, ans, l+1)
	solve(m.right, ans, l+1)

}

func leftView(n *Node) []int {
	ans := []int{}
	if n == nil {
		return ans
	}
	solve(n, &ans, 0)
	return ans
}

func main() {
	n := &Node{value: 1}
	n.left = &Node{value: 2}
	n.left.left = &Node{value: 4}
	n.left.right = &Node{value: 5}
	n.right = &Node{value: 3}
	fmt.Println(leftView(n))
}
