class ListNode:
    def __init__(self,val=0,next=None) -> None:
        self.val=val
        self.next=next

    def __repr__(self) -> str:
        vals=[]
        while self:
            vals.append(self.val)
            self=self.next
        return f'{vals}'

def convert(input: list[int])->ListNode:
    head=ListNode(0)
    curr=head
    for val in input:
        node=ListNode(val)
        curr.next=node
        curr=curr.next
    return head.next