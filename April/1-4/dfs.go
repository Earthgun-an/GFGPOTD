package main

import "fmt"

func solve(adj [][]int, i int, v []int, ans *[]int) {
	v[i] = 1
	*ans = append(*ans, i)
	for _, j := range adj[i] {
		if v[j] != 1 {
			v[j] = 1
			solve(adj, j, v, ans)
		}
	}
}

func dfs(adj [][]int) []int {
	ans := []int{}
	n := len(adj)
	visited := make([]int, n)
	for i := range adj {
		visited[i] = 0
	}
	fmt.Println(visited)
	solve(adj, 0, visited, &ans)
	fmt.Println(ans)
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
	fmt.Println(dfs(adj))
}
