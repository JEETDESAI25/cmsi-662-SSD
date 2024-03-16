package myjava;

public class StringStack {
    private String[] items; // Array to store the stack items
    private int top; // Index of the top element in the stack
    private int capacity; // Current maximum capacity of the stack

    // Constructor with initial capacity
    public StringStack(int initialCapacity) {
        if (initialCapacity <= 0) {
            throw new IllegalArgumentException("Initial capacity must be greater than 0.");
        }
        this.capacity = initialCapacity;
        this.items = new String[initialCapacity];
        this.top = -1; // Stack is initially empty
    }

    // Pushes a new string onto the stack
    public void push(String item) {
        if (item == null) {
            throw new NullPointerException("Cannot push null to the stack.");
        }
        // Check if the stack is full and expand if necessary
        if (top == capacity - 1) {
            expandCapacity();
        }
        items[++top] = item;
    }

    // Pops the top string from the stack
    public String pop() {
        if (isEmpty()) {
            throw new IllegalStateException("Cannot pop from an empty stack.");
        }
        String item = items[top];
        items[top--] = null; // Help with garbage collection
        return item;
    }

    // Checks if the stack is empty
    public boolean isEmpty() {
        return top == -1;
    }

    // Doubles the stack's capacity
    private void expandCapacity() {
        capacity *= 2;
        String[] newItems = new String[capacity];
        System.arraycopy(items, 0, newItems, 0, items.length);
        items = newItems;
    }



}