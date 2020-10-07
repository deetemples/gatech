import javafx.application.Application;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.ListView;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.scene.text.Font;
import javafx.stage.Stage;

/**
 * GUI application that represents Polly's Pet Shop
 *
 * @author CS1331 TA's
 * @version 1.0
 */
public class PetShop extends Application {

    private static final int PET_CAPACITY = 10;

    // Holds the store that will have all the pets
    private StoreOrganizer petStore = new Store(PET_CAPACITY);

    @Override
    public void start(Stage stage) {
        Label header = new Label("Polly's Pet Shop!");
        Font headerFont = new Font("Comic Sans MS", 48);
        header.setFont(headerFont);
        header.setAlignment(Pos.CENTER);

        // ObservableList of Animals that keeps track of
        // petStore's pets
        ObservableList<Animal> pets =
                FXCollections.observableArrayList();
        ListView<Animal> petsView = new ListView<>(pets);

        Button addPet = new Button("Add Pet");
        Button sortPets = new Button("Sort Pets");
        Button searchPet = new Button("Search Pet");

        addPet.setOnAction(event -> {
                Animal newPet = null;
                try {
                    newPet = PetValidator.receiveNew();
                } catch (Exception e) {
                    alertImproperPetInput();
                }
                if (newPet != null) {
                    petStore.add(newPet);
                    copyIntoObservableList(petStore.getPets(), pets);
                    searchPet.setDisable(true);
                }
            });

        sortPets.setOnAction(event -> {
                petStore.sort();
                copyIntoObservableList(petStore.getPets(), pets);
                if (pets.size() > 0) {
                    searchPet.setDisable(false);
                }
            });

        searchPet.setDisable(true);
        searchPet.setOnAction(event -> {
                Animal queriedPet = null;
                try {
                    queriedPet = PetValidator.receiveNew();
                } catch (Exception e) {
                    alertImproperPetInput();
                }

                if (queriedPet != null) {
                    int queriedIndex = petStore.binarySearch(queriedPet);

                    petsView.getSelectionModel().select(queriedIndex);
                }
            });

        HBox petActions = new HBox();
        petActions.getChildren().addAll(addPet, sortPets, searchPet);

        VBox root = new VBox();
        root.getChildren().addAll(header, petsView, petActions);

        stage.setScene(new Scene(root));
        stage.setTitle("Polly's Pet Shop!");
        stage.show();
    }

    /**
     * Alerts the user that proper input was not received
     */
    private void alertImproperPetInput() {
        String errorMsg = "Did not receive proper input."
                + " Perhaps you entered a number wrong?";
        Alert badInput = new Alert(Alert.AlertType.ERROR, errorMsg);
        badInput.showAndWait();
    }

    /**
     * Helper method that copies the contents of an array of Animals
     * into an ObservableList of Animals. Nulls are excluded
     *
     * @param pets the array to be copied from
     * @param observed the ObservableList to be copied into
     */
    private void copyIntoObservableList(Animal[] pets,
                                            ObservableList<Animal> observed) {
        observed.clear();
        for (Animal a : pets) {
            if (a != null) {
                observed.add(a);
            }
        }
    }
}
