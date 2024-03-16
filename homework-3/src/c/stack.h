#ifndef SECURESTACK_H
#define SECURESTACK_H

// A structure to hold operation status and messages
typedef struct {
    int success; // 0 for failure, 1 for success
    int error_code; // Specific error code if success is 0
    char* error_message; // Human-readable error message
} OperationResult;

// A structure to represent the stack
typedef struct {
    char** items; // Array of strings
    int capacity; // Maximum number of items the stack can hold
    int top; // Index to the top element of the stack
} SecureStack;

// Function prototypes
SecureStack* createStack(int initialCapacity);
OperationResult push(SecureStack* stack, const char* item);
char* pop(SecureStack* stack, OperationResult* result);
void freeStack(SecureStack* stack);

#endif // SECURESTACK_H
