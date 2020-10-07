/**
 * This interface defines the necessary methods for pet stores to sort and
 * search through their animals
 * @author 1331 TAs
 * @version 1.0
 */
public interface StoreOrganizer {

    /**
     * This method when implemented will return all of the animals in the store
     * @return all of the pets in the store
     */
    Animal[] getPets();

    /**
     * This method should allow a user to add an animal to their store inventory
     * @param a the animal to be added to the inventory
     */
    void add(Animal a);

    /**
     * This method should sort through the pets using bubble sort
     */
    void sort();

    /**
     * This method should search through the pets to look for a specific
     * animal. This should use the binary search method
     * @param a the animal to search through the list
     * @return the index the animal is found or -1 if the animal is not found
     */
    int binarySearch(Animal a);

    /**
     * This method should search through the pets to look for a specific
     * animal. This method should use the linear search method
     * @param a the animal to look for
     * @return the index the animal is found or -1 if the animal is not found
     */
    int linearSearch(Animal a);

}
