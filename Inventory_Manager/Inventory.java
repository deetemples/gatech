//In order to help learn course concepts, I worked on the homework with Carmen Dyck and discussed homework
//topics and issues with Carmen Dyck for CS 1331.

/**
 * An Inventory.
 * @author jdierberger3 and dtemples3
 * @version 1331.
 */
public class Inventory {

    // TODO : Add an Item[] instance variable called contents.
    // Initialize it at declaration; give it a default length of 4.
    private Item[] contents = new Item[4];

    // Merge two inventorys, merging other into this inventory.
    public void merge(Inventory other) {
        // TODO : Compute contents.length + other.contents.length
        // TODO : Create a new Item[] of the size above
        // TODO : Copy all the elements from contents into the new Item[]
        // TODO : Copy all the elements from other.contents into the new Item[]
        // TODO : Set contents to be the new Item[] we just filled
        int totalLength = contents.length + other.contents.length;
        Item[] merged = new Item[totalLength];
        for (int i = 0; i < contents.length; i++) {
            merged[i] = contents[i];
        }
        for (int i = 0; i < other.contents.length; i++) {
            merged[i + contents.length] = other.contents[i];
        }
        contents = merged;


    }

    // Get the i-th item, where the 0th item is the first.
    // Return null if the index is invalid.
    public Item getItem(int i) {
        // TODO : Check if "i" is a bad index into our array
            // If so, return null
        // TODO : Otherwise, return the element at index i
        if ((i > (contents.length - 1)) || (i < 0)) {
            return null;
        } else {
            return contents[i];
        }
    }

    // Put an item at the i-th position, where the 0th item is the first.
    // Return false if the index is invalid. Otherwise return true.
    public boolean putItem(int i, Item item) {
        // TODO : Check if "i" is a bad index into our array
            // If so, return false
        // TODO : Otherwise, set the element at index i to item
        if ((i > (contents.length - 1)) || (i < 0)) {
            return false;
        } else {
            contents[i] = item;
            return true;
        }
    }

    // Get the length of contents.
    public int getContentsLength() {
        // TODO : Return the length of contents.
        // remove this in your final code.
        return contents.length;
    }

}