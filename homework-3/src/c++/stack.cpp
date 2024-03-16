#include <iostream>
#include <memory>
#include <stdexcept>

class StringStack {
public:
    StringStack(int initialCapacity = 10) : capacity(initialCapacity), top(-1) {
        // Allocate an array of unique_ptr to strings
        items = std::make_unique<std::unique_ptr<std::string>[]>(capacity);
    }

    void push(const std::string& item) {
        if (top >= capacity - 1) {
            expand();
        }
        // Increment top and create a new string in the array
        items[++top] = std::make_unique<std::string>(item);
    }

    std::string pop() {
        if (isEmpty()) {
            throw std::out_of_range("Pop attempted on an empty stack.");
        }
        std::string item = *items[top]; // Copy the top item
        items[top--].reset(); // Reset (delete) the top unique_ptr, decrement top
        return item;
    }

    bool isEmpty() const {
        return top == -1;
    }

private:
    std::unique_ptr<std::unique_ptr<std::string>[]> items; // Array of unique_ptr to strings
    int capacity;
    int top;

    void expand() {
        int newCapacity = capacity * 2;
        // Create a new, larger array of unique_ptr to strings
        std::unique_ptr<std::unique_ptr<std::string>[]> newItems = std::make_unique<std::unique_ptr<std::string>[]>(newCapacity);

        // Move the strings from the old array to the new one
        for (int i = 0; i <= top; i++) {
            newItems[i] = std::move(items[i]);
        }

        // Replace the old array with the new one
        items = std::move(newItems);
        capacity = newCapacity;
    }
};

int main() {
    StringStack stack(5);

    try {
        stack.push("Hello");
        stack.push("World");
        std::cout << stack.pop() << std::endl;
        std::cout << stack.pop() << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}
