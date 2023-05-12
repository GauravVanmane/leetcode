def hasCycle(self, head: Optional[ListNode]) -> bool:

        curr, post = head, head

        while post and post.next:
            curr = curr.next
            post = post.next.next
            if curr == post:
                return True 
        
        return False
