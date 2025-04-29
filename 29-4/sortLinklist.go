package main

import (
	"fmt"
	"sort"
)

type Node struct {
	data int
	next *Node
}

type linklist struct {
	head *Node
}

func (list *linklist) insert(data int) {
	newNode := &Node{data: data, next: nil}
	if list.head == nil {
		list.head = newNode
		return
	}
	tmp := list.head
	for tmp.next != nil {
		tmp = tmp.next
	}
	tmp.next = newNode
}

func (list *linklist) printList() {
	tmp := list.head
	for tmp != nil {
		fmt.Println(tmp.data)
		tmp = tmp.next
	}
}

func (list *linklist) sortList() []int {
	tmp := []int{}
	cur := list.head
	for cur != nil {
		tmp = append(tmp, cur.data)
		cur = cur.next
	}
	sort.Ints(tmp)
	return tmp
}

func (ll *linklist) solve(arr []int) {
	ll.head = nil
	for _, i := range arr {
		ll.insert(i)
	}
}

func main() {
	ll := linklist{}
	ll.insert(1)
	ll.insert(2)
	ll.insert(2)
	ll.insert(2)
	ll.insert(1)
	ll.insert(1)
	ll.insert(0)
	ll.insert(0)
	l := ll.sortList()
	ll.solve(l)
	ll.printList()
}
