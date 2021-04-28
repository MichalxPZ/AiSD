#include <stdio.h>
#include <mm_malloc.h>
#include "time.h"

//struct definition
struct Node {
    int value;
    struct Node *childLeft;
    struct Node *childRight;
    int height;
};

int height(struct Node *N) {
    if (N == NULL)
        return 0;
    return N->height;
}

int max(int a, int b) {
    return (a > b)? a : b;
}

void preOrder(struct Node *root){
    if(root != NULL)
    {
        printf("%d ", root->value);
        preOrder(root->childLeft);
        preOrder(root->childRight);
    }
}

//function takes value and returns node struct with value and NULL childs
struct Node *creataNode(int value) {
    struct Node *node = (struct Node*)malloc(sizeof(struct Node));
    node->value = value;
    node->childRight = NULL;
    node->childLeft = NULL;
    node->height = 1;
    return node;
}

//right rotate 3 nodes
struct Node *rightRotate(struct Node *head) {
    struct Node *left = head->childLeft;
    struct Node *rightleft = left->childRight;

    left->childRight = head;
    head->childLeft = rightleft;

    head->height = max(height(head->childLeft), height(head->childRight) + 1);
    left->height = max(height(left->childLeft), height(left->childRight) + 1);

    return left;
}

//left rotate 3 nodes
struct Node *leftRotate(struct Node *head) {
    struct Node *right = head->childRight;
    struct Node *leftright = right->childLeft;

    right->childLeft = head;
    head->childRight = leftright;

    head->height = max(height(head->childLeft), height(head->childRight) + 1);
    right->height = max(height(right->childLeft), height(right->childRight) + 1);

    return right;
}

int getBalance(struct Node *head) {
    if (head == NULL) {
        return 0;
    } else {
        return height(head->childLeft) - height(head->childRight);
    }
}

struct Node *insert(struct Node *head, int value) {
    if (head == NULL) {
        return creataNode(value);
    } else {
        if (value < head->value) {
            head->childLeft = insert(head->childLeft, value);
        } else if (value > head->value) {
            head->childRight = insert(head->childRight, value);
        } else {
            return head;
        }

        head->height = 1 + max(height(head->childRight), height(head->childLeft));

        int balance = getBalance(head);

        if (balance > 1 && value < head->childLeft->value) {
            return rightRotate(head);
        }

        if (balance < -1 && value > head->childRight->value) {
            return leftRotate(head);
        }

        if (balance > 1 && value > head->childLeft->value) {
            head->childLeft = leftRotate(head->childLeft);
            return rightRotate(head);
        }

        if (balance < -1 && value < head->childRight->value) {
            head->childRight = rightRotate(head->childRight);
            return leftRotate(head);
        }

        return head;
    }
}

int inTree(struct Node *head, int value) {
    if (head == NULL) {
        return 0;
    } else {
        if (head->value == value) {
            return 1;
        }
        if (head->value < value) {
            return inTree(head->childRight, value);
        } else {
            return inTree(head->childLeft, value);
        }
    }
}

struct Node * minValueNode(struct Node* head){
    struct Node* touchNode = head;

    while (touchNode->childLeft != NULL)
        touchNode = touchNode->childLeft;

    return touchNode;
}

struct Node *delete(struct Node *head, int value) {
    if (head == NULL) {
        return head;
    } else {
        if (value < head->value) {
            head->childLeft = delete(head->childLeft, value);
        } else if (value > head->value) {
            head->childRight = delete(head->childRight, value);
        } else {
            if ((head->childLeft == NULL) || (head->childRight == NULL)) {
                struct Node *temp = head->childLeft ? head->childLeft : head->childRight;

                if (temp == NULL) {
                    temp = head;
                    head = NULL;
                } else {
                    *head = *temp;
                    free(temp);
                }
            } else {
                struct Node *temp = minValueNode(head->childRight);
                head->value = temp->value;
                head->childRight = delete(head->childRight, temp->value);
            }
        }
        if (head == NULL) return head;
        head->height = 1 + max(height(head->childLeft), height(head->childRight));
        int balance = getBalance(head);

        if (balance > 1 && value < head->childLeft->value) {
            return rightRotate(head);
        }

        if (balance < -1 && value > head->childRight->value) {
            return leftRotate(head);
        }

        if (balance > 1 && value > head->childLeft->value) {
            head->childLeft = leftRotate(head->childLeft);
            return rightRotate(head);
        }

        if (balance < -1 && value < head->childRight->value) {
            head->childRight = rightRotate(head->childRight);
            return leftRotate(head);
        }

        return head;
    }
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
        insert(head, val);
    }
    clock_t end = clock();

    double seconds = (double ) (end - start) / CLOCKS_PER_SEC;
    fprintf(result, "%lf\n", 1000 * seconds);
    fclose(result);
    fclose(input);
    start = clock();
    inTree(head, -1);
    inTree(head, 10000000);
    inTree(head, 50);
    inTree(head, 5);
    inTree(head, 14);
    end = clock();
    seconds = (double ) (end - start) / CLOCKS_PER_SEC;
    fprintf(resultFind, "%lf\n", 1000 * seconds);
    start = clock();
    delete(head, -1);
    delete(head, 10000000);
    delete(head, 50);
    delete(head, 5);
    delete(head, 14);
    end = clock();
    seconds = (double ) (end - start) / CLOCKS_PER_SEC;
    fprintf(resultDelete, "%lf\n",1000 *  seconds);
    fclose(resultFind);
    fclose(resultDelete);
    return 0;
}