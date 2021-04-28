//
// Created by Michal on 15.04.2021.
//

#include <stdio.h>
#include <mm_malloc.h>
#include "time.h"

struct Node {
    int value;
    struct Node *childLeft;
    struct Node *childRight;
};

struct Node * createNode(int value) {
    struct Node *newNode = (struct Node *)malloc(sizeof (struct Node));
    newNode->value = value;
    newNode->childLeft = NULL;
    newNode->childRight = NULL;

    return newNode;
}

void preOrder(struct Node *root){
    if(root != NULL)
    {
        printf("%d ", root->value);
        preOrder(root->childLeft);
        preOrder(root->childRight);
    }
}

struct Node * insert(struct Node *head, int value) {
    if (head == NULL) {
        return createNode(value);
    } else if (value <= head->value) {
        head->childLeft = insert(head->childLeft, value);
    } else if (value > head->value) {
        head->childRight = insert(head->childRight, value);
    }
    return head;
}

struct Node *minValueNode(struct Node *head) {
    struct Node* touchNode = head;
    while (touchNode != NULL && touchNode->childLeft != NULL) {
        touchNode = touchNode->childLeft;
    }
    return touchNode;
}

struct Node *delete(struct Node *head, int value) {
    if (head == NULL) {
        return head;
    }
    if (value < head->value) {
        head->childLeft = delete(head->childLeft, value);
    } else if (value > head->value) {
        head->childRight = delete(head->childRight, value);
    } else {
        if (head->childLeft == NULL) {
            struct Node *temp = head->childRight;
            free(head);
            return temp;
        }
        else if (head->childRight == NULL) {
            struct Node *temp = head->childLeft;
            free(head);
            return temp;
        }
        struct Node* temp = minValueNode(head->childRight);
        head->value = temp->value;
        head->childRight = delete(head->childRight, temp->value);
    }
    return head;
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

int main() {
    FILE *input = fopen("txt/input.txt", "r");
    FILE *result = fopen("txt/result.txt", "a");
    FILE *resultFind = fopen("txt/resultFind.txt", "a");
    FILE *resultDelete = fopen("txt/resultDelete.txt", "a");
    struct Node *head = NULL;
    clock_t start = clock();
    while (!feof(input)) {
        int val = fscanf(input, "%d\n", &val);
        head = insert(head, val);
    }
    clock_t end = clock();
    double seconds = (double ) (end - start) / CLOCKS_PER_SEC;
    fprintf(result, "%lf\n", 1000* seconds);
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
    fprintf(resultDelete, "%lf\n", 1000*seconds);
    fclose(resultFind);
    fclose(resultDelete);
    return 0;
}
