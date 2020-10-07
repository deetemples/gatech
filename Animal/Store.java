//In order to help learn course concepts, I worked on the homework with Carmen Dyck and discussed homework
//topics and issues with Carmen Dyck for CS 1331.

/**
* This class represents a Store object that implements Store Organizer.
* @author Danielle Temples
* @version 1.0
*
*/

import java.util.Arrays;

public class Store implements StoreOrganizer {
    private Animal[] pets;
    private int index = -1;
    private int maxPets;

    /**
    * This method creates a Store constructer that takes in number of pets.
    * @param numPets number of pets
    */

    public Store(int numPets) {
        pets = new Animal[numPets];
        maxPets = numPets;
    }

    /**
    * This method gets pets.
    * @return pets
    */

    public Animal[] getPets() {
        return pets;
    }

    /**
    * This method adds animals into the pets array.
    * @param a Animal object
    */

    public void add(Animal a) {
        index++;
        if (index < maxPets) {
            pets[index] = a;
        }
    }

    /**
    * This method bubble sorts the animals in the pets array.
    * O(n^2); quite innefiicent for sorting large data volumes; stable and adaptive.
    */

    public void sort() {
        System.out.println(Arrays.toString(pets));
        boolean switched = false;
        int maxIndex = index;
        do {
            switched = false;
            for (int i = 0; i < maxIndex; i++) {
                if (pets[i].compareTo(pets[i + 1]) > 0) {
                    Animal temp = pets[i];
                    pets[i] = pets[i + 1];
                    pets[i + 1] = temp;
                    switched = true;
                }
                System.out.println(Arrays.toString(pets));
            }
            maxIndex--;
        } while (switched);
        System.out.println(Arrays.toString(pets));
    }

    /**
    * This method used binary search in the pets array to find an animal.
    * @param a Animal object
    * @return found
    * O(log n); doubling szie of input data has little effect on growth so extremely efficient.
    */

    public int binarySearch(Animal a) {
        sort();
        int found = -1;
        int minIndex = 0;
        int maxIndex = index;
        while (found == -1 && minIndex <= maxIndex) {
            int avg = ((minIndex + maxIndex) / 2);
            if (a.compareTo(pets[avg]) < 0) {
                maxIndex = avg - 1;
            } else if (a.compareTo(pets[avg]) > 0) {
                minIndex = avg + 1;
            } else {
                found = avg;
            }
        }
        return found;
    }

    /**
    * This method used linear search in the pets array to find an animal.
    * @param a Animal object
    * @return found
    * O(n); efficiency is expressed as a linear function with the number of comparisons
        to find a target increasing linearly.
    */

    public int linearSearch(Animal a) {
        sort();
        int found = -1;
        int currentIndex = 0;
        if (index == -1) {
            return -1;
        }
        while (found == -1 && currentIndex < index && a.compareTo(pets[index]) >= 0) {
            System.out.println("currentIndex = " + currentIndex);
            System.out.println(pets[index]);
            System.out.println();

            if (a.compareTo(pets[index]) == 0) {
                found = index;
            }
            index++;
        }
        return found;
    }
}