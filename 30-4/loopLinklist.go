package main

import "fmt"

type Node struct {
	data int
	next *Node
}

type linkList struct {
	head *Node
}

func (ll *linkList) insert(val int) {
	new_node := &Node{data: val, next: nil}
	if ll.head == nil {
		ll.head = new_node
		return
	}
	tmp := ll.head
	for tmp != nil {
		tmp = tmp.next
	}
	tmp.next = new_node
}

func (ll *linkList) lengthLoop() int {
	slow := ll.head
	fast := ll.head
	f := false
	for fast != nil && fast.next != nil {
		slow = slow.next
		fast = fast.next.next
		if slow == fast {
			f = true
			break
		}
	}
	if !f {
		return 0
	}
	tmp := slow.next
	cnt := 1
	for tmp != nil {
		if slow == tmp {
			break
		}
		tmp = tmp.next
		cnt += 1
	}
	return cnt
}

func main() {
	ll := linkList{}
	ll.insert(1)
	ll.insert(2)
	fmt.Println(ll.lengthLoop())
}
