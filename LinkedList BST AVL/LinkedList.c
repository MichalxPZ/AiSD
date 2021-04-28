#include <stdio.h>
#include <mm_malloc.h>
#include "time.h"

struct Node {
    int value;
    struct Node *child;
};

struct Node * createNode(int value) {
    struct Node *newNode = (struct Node *)malloc(sizeof (struct Node));
    newNode->value = value;
    newNode->child = NULL;

    return newNode;
}

void getList(struct Node *head) {
    struct Node *touchNode = head;
    while (touchNode != NULL) {
        printf("%d ", touchNode->value);
        touchNode = touchNode->child;
    }

}

void insert(struct Node** head_ref,
                  struct Node* new_node)
{
    struct Node* current;
    /* Special case for the head end */
    if (*head_ref == NULL
        || (*head_ref)->value
               >= new_node->value) {
        new_node->child = *head_ref;
        *head_ref = new_node;
    }
    else {
        /* Locate the node before
the point of insertion */
        current = *head_ref;
        while (current->child != NULL
               && current->child->value < new_node->value) {
            current = current->child;
        }
        new_node->child = current->child;
        current->child = new_node;
    }
}

int inList(struct Node **head, struct Node *node) {
    struct Node *touchnode = *head;
    if (*head == NULL) {
        return 0;
    } else {
        while (touchnode != NULL) {
            if (touchnode->value == node->value) {
                return 1;
            }
            touchnode = touchnode->child;
        }
    }
    return 0;
}

void delete(struct Node** head_ref, int key){
    // Store head node
    struct Node *temp = *head_ref, *prev;

    // If head node itself holds the key to be deleted
    if (temp != NULL && temp->value == key) {
        *head_ref = temp->child; // Changed head
        free(temp); // free old head
        return;
    }

    // Search for the key to be deleted, keep track of the
    // previous node as we need to change 'prev->child'
    while (temp != NULL && temp->value != key) {
        prev = temp;
        temp = temp->child;
    }

    // If key was not present in linked list
    if (temp == NULL)
        return;

    // Unlink the node from linked list
    prev->child = temp->child;

    free(temp); // Free memory
}

int main() {
    FILE *input = fopen("txt/input.txt", "r");
    FILE *result = fopen("txt/result.txt", "a");
    FILE *resultFind = fopen("txt/resultFind.txt", "a");
    FILE *resultDelete = fopen("txt/resultDelete.txt", "a");
    struct Node *head = NULL;
    clock_t start = clock();
    while (!feof(input)) {
        int val = fscanf(input, "%d\n", &val);
        struct Node *node = createNode(val);
        insert(&head, node);
    }
    clock_t end = clock();
    double time = (double ) (end - start) / CLOCKS_PER_SEC;
    fprintf(result, "%lf\n", 1000 * time);
    start = clock();
    inList(&head, createNode(-1));
    inList(&head, createNode(10000000));
    inList(&head, createNode(50));
    inList(&head, createNode(5));
    inList(&head, createNode(14));
    end = clock();
    time = (double ) (end - start) / CLOCKS_PER_SEC;
    fprintf(resultFind, "%lf\n", 1000*time);
    start = clock();
    delete(&head, -1);
    delete(&head, 10000000);
    delete(&head, 50);
    delete(&head, 5);
    delete(&head, 14);
    end = clock();
    time = (double ) (end - start) / CLOCKS_PER_SEC;
    fprintf(resultDelete, "%lf\n", 1000*time);
    return 0;
}
