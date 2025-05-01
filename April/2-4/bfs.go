package main

import "fmt"

func bfs(adj [][]int) []int {
	n := len(adj)
	q := []int{}
	visited := make([]int, n)
	q = append(q, 0)
	for i := range adj {
		visited[i] = 0
	}
	fmt.Println(q, visited)
	ans := []int{}
	visited[0] = 1
	for len(q) > 0 {
		val := q[0]
		ans = append(ans, val)
		q = q[1:]
		for _, i := range adj[val] {
			if visited[i] != 1 {
				visited[i] = 1
				q = append(q, i)
			}
		}
	}
	return ans
}

func main() {
	adj := [][]int{
		{2, 3, 1},
		{0},
		{0, 4},
		{0},
		{2},
	}
	fmt.Println(bfs(adj))
}
