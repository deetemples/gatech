import javafx.scene.control.ChoiceDialog;
import javafx.scene.control.TextInputDialog;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

/**
 * A utility class that validates user input when asking
 * for a pet.
 *
 * @author CS1331 TA's
 * @version 1.0
 */
public class PetValidator {

    // All possible types of pets
    private static final List<String> TYPES = new ArrayList<>();
    // The "static" block allows you to add initial values to
    // a static variable without using a constructor
    static { // This block only executes once, ever
        TYPES.add("Dog");
        TYPES.add("Cat");
    }

    /**
     * Takes input from the user about a pet and
     * returns an instance with the user's specifications
     *
     * @return an Animal that represents the new pet
     * @throws Exception if the user does not give valid input
     */
    public static Animal receiveNew() throws Exception {
        String type = getTypeFromUser();
        String name = getNameFromUser();
        double price = getPriceFromUser();
        switch (type) {
        case "Dog":
            String tailPrompt = "Does the dog have a curly tail?";
            boolean curlyTail = getBooleanFieldFromUser(tailPrompt);
            String droolPrompt = "What is the dog's drool rate?";
            int droolRate = getIntegerFieldFromUser(droolPrompt);
            // Errors may occur here if the constructor is written wrong
            return new Dog(name, price, curlyTail, droolRate);
        case "Cat":
            String micePrompt = "How many mice has the cat caught?";
            int miceCaught = getIntegerFieldFromUser(micePrompt);
            String lasagnaPrompt = "Does the cat like lasagna?";
            boolean likesLasagna = getBooleanFieldFromUser(lasagnaPrompt);
            // Errors may occur here if the constructor is written wrong
            return new Cat(name, price, miceCaught, likesLasagna);
        default:
            return null;
        }
    }

    /**
     * Asks for a pet's type from the user by showing a ChoiceDialog
     *
     * @return the pet's type
     * @throws Exception if the Dialog closes with no received input
     */
    private static String getTypeFromUser() throws Exception {
        ChoiceDialog<String> petTypePopup = new ChoiceDialog<>("Dog", TYPES);
        petTypePopup.setHeaderText("What is the pet's type?");
        Optional<String> petType = petTypePopup.showAndWait();
        if (petType.isPresent()) {
            return petType.get();
        } else {
            throw new Exception();
        }
    }

    /**
     * Asks for a pet's type from the user by showing a TextInputDialog
     *
     * @return the pet's name
     * @throws Exception if the Dialog closes with no received input
     */
    private static String getNameFromUser() throws Exception {
        TextInputDialog petNamePopup = new TextInputDialog("Buzz");
        petNamePopup.setHeaderText("What is the pet's name?");
        Optional<String> petName = petNamePopup.showAndWait();
        if (petName.isPresent()) {
            return petName.get();
        } else {
            throw new Exception();
        }
    }

    /**
     * Asks for a pet's price from the user by showing a TextInputDialog
     *
     * @return the pet's price as a double
     * @throws Exception if the Dialog closes with no received input
     */
    private static double getPriceFromUser() throws Exception {
        TextInputDialog petPricePopup = new TextInputDialog("0.00");
        petPricePopup.setHeaderText("What is the pet's price?");
        Optional<String> petPrice = petPricePopup.showAndWait();
        if (petPrice.isPresent()) {
            return Double.parseDouble(petPrice.get());
        } else {
            throw new Exception();
        }
    }

    /**
     * Asks user for a yes/no answer that will be translated to a boolean,
     * which will be assigned to a pet's field
     *
     * @param prompt the prompt for the user to answer
     * @return the user's yes/no answer translated as a boolean
     * @throws Exception if the Dialog closes with no received input
     */
    private static boolean getBooleanFieldFromUser(String prompt)
            throws Exception {
        ChoiceDialog<String> yesNoPopup =
                new ChoiceDialog<>("Yes", List.of("Yes", "No"));
        yesNoPopup.setHeaderText(prompt);
        Optional<String> response = yesNoPopup.showAndWait();
        if (response.isPresent()) {
            return response.get().equals("Yes");
        } else {
            throw new Exception();
        }
    }

    /**
     * Asks user for an integer that will assigned to a pet's field
     *
     * @param prompt the prompt for the user to answer
     * @return the user's input integer
     * @throws Exception if the Dialog closes with no received input
     */
    private static int getIntegerFieldFromUser(String prompt) throws Exception {
        TextInputDialog numberPopup =
                new TextInputDialog("0");
        numberPopup.setHeaderText(prompt);
        Optional<String> response = numberPopup.showAndWait();
        if (response.isPresent()) {
            return Integer.parseInt(response.get());
        } else {
            throw new Exception();
        }
    }

}
