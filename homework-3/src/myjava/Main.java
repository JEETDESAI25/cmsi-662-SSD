package myjava;

public class Main {
    public static void main(String[] args) {
        StringStack stack = new StringStack(5);

        try {
            stack.push("Hello");
            stack.push("World");
            System.out.println(stack.pop());
            System.out.println(stack.pop());
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}