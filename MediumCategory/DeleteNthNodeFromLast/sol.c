/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    //idea is that we have two pointers, slow and fast. fast moves n+1 nodes before slow, if fast ends up at null (tail) element at slow is the one to delete
    //create a dummy node in the case where head is the one to be removed
    struct ListNode dummy;
    dummy.val = 0;
    dummy.next = head;

    struct ListNode *fast = &dummy;
    struct ListNode *slow = &dummy;
    //advance fast n+1 nodes
    for(int i = 0; i <= n; i++){
        fast = fast->next;
    }

    //advance both at the same time
    while (fast != NULL){
        fast = fast->next;
        slow = slow->next;
    }

    //delete the node at slow->next
    struct ListNode* deleteThis = slow->next;
    slow->next = slow->next->next;

    free(deleteThis);

    //head is dummy.next (we may have deleted it)
    return dummy.next;
}
