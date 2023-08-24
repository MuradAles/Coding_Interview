class Solution:
    def connect(self, root):
        # edge case check
        if not root:
            return None

        node = root  # create a pointer to the root node

        # iterate only until we have a new level (because the connections for Nth level are done when we are at N-1th level)
        while node.left:
            head = node
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left

                head = head.next

            node = node.left

        return root
