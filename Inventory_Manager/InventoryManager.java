//In order to help learn course concepts, I worked on the homework with Carmen Dyck and discussed homework
//topics and issues with Carmen Dyck for CS 1331.

import java.util.Scanner;

/**
 * The InventoryManager.
 * @author jdierberger3 and dtemples3
 * @version 1331
 */
public class InventoryManager {

    /*
     * Name of the program, if you want to customize that.
     */
    private static String programName = "CS1331 Inventory Management System";

    // Merge two inventories. Merge i2 into i1.
    public static void mergeInventories(Inventory i1, Inventory i2) {
        // TODO : In one line (using the merge method), merge i1 and i2.
        i1.merge(i2);
    }

    // Add the item at pos to inventory. If doesn't work, print:
    // "Can't add there."
    public static void addItem(Inventory inventory, int pos, Item item) {
        // TODO : Try to add the item. If invalid, print an error.
        boolean answer = inventory.putItem(pos, item);
        if (!answer) {
            System.out.println("Can't add there.");
        }
    }

    // Print an Item
    public static void printItem(Item item) {
        // TODO : Print "(name, price, weight)", using valeus from item
        // If the item is null, print "(empty, 0, 0)"
        if (item == null) {
            System.out.print("(empty, 0, 0)");
        } else {
            System.out.printf("(%s, %2.2f, %2.2f)", item.getName(), item.getPrice(), item.getWeight());
        }
    }

    // Print a comma separated list of an Inventory's Items
    public static void showInventory(Inventory inventory) {
        // if getContentsLength() is less than or equal to  0
            // print "()"
        // else
            // Print the first item with the printItem method.
            // For items at index 1 to getContentsLength() - 1
                // Get and print the item
            // print a newline
        if (inventory == null || inventory.getContentsLength() <= 0) {
            System.out.println("()");
        } else {
            printItem(inventory.getItem(0));
            for (int i = 1; i <= (inventory.getContentsLength() - 1); i++) {
                System.out.print(", ");
                printItem(inventory.getItem(i));
            }
            System.out.println();
        }
    }

    /**
     * Main method. DO NOT MODIFY THIS METHOD.
     * @param args The console launch arguments.
     */
    public static void main(String[] args) {
        System.out.println("Welcome to " + programName);
        Scanner scanner = new Scanner(System.in);
        Inventory[] inventories = new Inventory[10];
        int inventoriesSize = 0;
        while (true) {
            System.out.println("What would you like to do? (enter a number)");
            System.out.println("[1] Add an Inventory");
            System.out.println("[2] View list of Inventories");
            System.out.println("[3] View an Inventory");
            System.out.println("[4] Merge two Inventories");
            System.out.println("[5] Put an Item in an Inventory");
            System.out.println("[6] Quit");
            int choice = -1;
            choice = Integer.parseInt(scanner.nextLine());
            System.out.println();
            Inventory inventory = null;
            switch (choice) {
            case 1:
                if (inventoriesSize >= inventories.length) {
                    Inventory[] inventories2
                        = new Inventory[inventoriesSize + 10];
                    for (int i = 0; i < inventoriesSize; // jd
                        inventories2[i++] = inventories[i]) {
                        i = i;
                    }
                }
                inventories[inventoriesSize++] = new Inventory();
                break;
            case 2:
                int c = 0;
                for (Inventory i : inventories) {
                    if (i == null) {
                        continue;
                    }
                    System.out.println("Inventory [" + c++ + "]" + " with "
                        + i.getContentsLength() + " items");
                }
                System.out.println();
                break;
            case 3:
                System.out.print("Enter which inventory to show: ");
                choice = Integer.parseInt(scanner.nextLine());
                inventory = ((choice < 0
                    || choice >= inventories.length)
                    ? null : inventories[choice]);
                if (inventory == null) {
                    System.out.println("That doesn't exist");
                    System.out.println();
                    break;
                }
                showInventory(inventory);
                break;
            case 4:
                System.out.print("Enter the reciever inventory number: ");
                choice = Integer.parseInt(scanner.nextLine());
                Inventory inventory1 = ((choice < 0
                    || choice >= inventories.length)
                    ? null : inventories[choice]);
                if (inventory1 == null) {
                    System.out.println("That doesn't exist");
                    System.out.println();
                    break;
                }
                System.out.print("Enter the giver inventory number: ");
                choice = Integer.parseInt(scanner.nextLine());
                Inventory inventory2 = ((choice < 0
                    || choice >= inventories.length)
                    ? null : inventories[choice]);
                if (inventory2 == null) {
                    System.out.println("That doesn't exist");
                    System.out.println();
                    break;
                }
                mergeInventories(inventory1, inventory2);
                break;
            case 5:
                System.out.print("Use a randomly generated Item? [y/...]: ");
                String decision = scanner.nextLine();
                if (decision.toLowerCase().charAt(0) == 'y') {
                    System.out.print("Select an inventory: ");
                    choice = Integer.parseInt(scanner.nextLine());
                    System.out.println();
                    inventory = ((choice < 0
                        || choice >= inventories.length)
                        ? null : inventories[choice]);
                    if (inventory == null) {
                        System.out.println("That doesn't exist");
                        System.out.println();
                        break;
                    }
                    showInventory(inventory);
                    System.out.print("Select a slot: ");
                    choice = Integer.parseInt(scanner.nextLine());
                    System.out.println();
                    addItem(inventory, choice, new Item());
                } else {
                    System.out.print("Select an inventory: ");
                    choice = Integer.parseInt(scanner.nextLine());
                    System.out.println();
                    inventory = ((choice < 0
                        || choice >= inventories.length)
                        ? null : inventories[choice]);
                    if (inventory == null) {
                        System.out.println("That doesn't exist");
                        System.out.println();
                        break;
                    }
                    showInventory(inventory);
                    System.out.print("Select a slot: ");
                    choice = Integer.parseInt(scanner.nextLine());
                    System.out.println();
                    System.out.print("Enter a name: ");
                    String name = scanner.nextLine();
                    System.out.println();
                    System.out.print("Enter a price: ");
                    double price = Double.valueOf(scanner.nextLine());
                    System.out.println();
                    System.out.print("Enter a weight: ");
                    double weight = Double.valueOf(scanner.nextLine());
                    System.out.println();
                    Item item = new Item(name, price, weight);
                    addItem(inventory, choice, item);
                }
                break;
            case 6:
                System.out.println("Goodbye");
                return;
            default:
                System.out.println("That's not an option: try again.");
                break;
            }
        }
    }

}