#include "stack.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

SecureStack* createStack(int initialCapacity) {
    SecureStack* stack = (SecureStack*)malloc(sizeof(SecureStack));
    if (!stack) {
        printf("Error: Memory allocation failed for stack\n");
        exit(1); // Fail fast on memory allocation failure
    }
    
    stack->items = (char**)malloc(sizeof(char*) * initialCapacity);
    if (!stack->items) {
        printf("Error: Memory allocation failed for stack items\n");
        free(stack); // Cleanup before failing
        exit(2); // Fail fast on memory allocation failure
    }

    stack->capacity = initialCapacity;
    stack->top = -1; // Empty stack
    return stack;
}

// Helper function to expand the stack's capacity
static void expandStack(SecureStack* stack) {
    int newCapacity = stack->capacity * 2;
    char** newItems = (char**)realloc(stack->items, sizeof(char*) * newCapacity);
    if (!newItems) {
        printf("Error: Memory allocation failed during expansion\n");
        exit(3); // Fail fast on memory allocation failure
    }
    
    stack->items = newItems;
    stack->capacity = newCapacity;
}

OperationResult push(SecureStack* stack, const char* item) {
    if (stack->top == stack->capacity - 1) {
        expandStack(stack); // Attempt to expand the stack if full
    }

    stack->items[++stack->top] = strdup(item); // Duplicate and push the item
    if (!stack->items[stack->top]) {
        printf("Error: Memory allocation failed for item\n");
        exit(4); // Fail fast on memory allocation failure
    }

    OperationResult result = {1, 0, "Push successful"};
    return result;
}

char* pop(SecureStack* stack, OperationResult* result) {
    if (stack->top == -1) {
        result->success = 0;
        result->error_code = 1;
        result->error_message = "Pop failed: Stack is empty";
        return NULL;
    }

    char* item = stack->items[stack->top];
    stack->items[stack->top--] = NULL; // Remove the item and decrement top
    result->success = 1;
    result->error_message = "Pop successful";
    return item;
}

void freeStack(SecureStack* stack) {
    while (stack->top != -1) {
        free(stack->items[stack->top--]);
    }
    free(stack->items);
    free(stack);
}

int main() {
    SecureStack* stack = createStack(5);
    OperationResult result;

    push(stack, "Hello");
    push(stack, "World");
    printf("%s\n", pop(stack, &result));
    printf("%s\n", pop(stack, &result));

    freeStack(stack);
    return 0;
}
