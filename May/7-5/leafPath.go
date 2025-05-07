package main

import "fmt"

type Node struct {
	data  int
	left  *Node
	right *Node
}

func leafPath(n *Node, ans *[]int, tmp []int) {
	if n == nil {
		return
	}
	tmp = append(tmp, n.data)
	if n.left != nil && n.right != nil {
		*ans = append(*ans, tmp...)
	} else {
		leafPath(n.left, ans, tmp)
		leafPath(n.right, ans, tmp)
	}
	fmt.Println(*ans)
	tmp = tmp[:len(tmp)-1]
}

func main() {
	n := &Node{data: 1}
	n.left = &Node{data: 2}
	n.left.left = &Node{data: 4}
	n.left.right = &Node{data: 5}
	n.right = &Node{data: 3}
	ans := []int{}
	leafPath(n, &ans, []int{})
	fmt.Println(ans)
}
