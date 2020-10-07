//In order to help learn course concepts, I worked on the homework with Carmen Dyck and discussed homework
//topics and issues with Carmen Dyck for CS 1331.

import javafx.application.Application;
import javafx.stage.Stage;
import javafx.scene.control.ToggleGroup;
import javafx.scene.Scene;
import javafx.scene.shape.Circle;
import javafx.scene.control.TextField;
import javafx.scene.control.Label;
import javafx.scene.control.RadioButton;
import javafx.scene.control.Button;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.Pane;
import javafx.scene.control.Alert;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.layout.VBox;
import javafx.scene.layout.HBox;
import javafx.scene.paint.Color;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;


/**
* This class constructs CSPaint which extends Application.
* @author Danielle Temples
* @version 1.0
*
*/

public class CSPaint extends Application {

    private Color inputColor = Color.PURPLE;
    private int shapeCounter = 0;
/**
* Main method to run the application from the command line.
* @param args Command line arguments.
*/

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) {
        Pane canvas = new Pane();
        canvas.setPrefSize(650, 450);
        canvas.setStyle("-fx-background-color: white;");

        ToggleGroup toggle = new ToggleGroup();

        RadioButton rb1 = new RadioButton("Draw");
        rb1.setToggleGroup(toggle);
        rb1.setSelected(true);

        RadioButton rb2 = new RadioButton("Erase");
        rb2.setToggleGroup(toggle);

        RadioButton rb3 = new RadioButton("Circle");
        rb3.setToggleGroup(toggle);

        RadioButton rb4 = new RadioButton("LinkedIn");
        rb4.setToggleGroup(toggle);

        Button clear = new Button("Clear");

        Label coordinates = new Label("(0, 0)");

        Label shapeNumber = new Label("Number of shape: " + shapeCounter);

        TextField textField = new TextField();

        textField.setOnAction(e -> {
                try {
                    inputColor = Color.valueOf(textField.getText());
                } catch (IllegalArgumentException ex) {
                    Alert error = new Alert(AlertType.ERROR);
                    error.setHeaderText("Invalid Color");
                    error.setContentText("Invalid color entered.");
                    error.showAndWait();
                }
            });

        VBox vbox = new VBox();
        vbox.getChildren().addAll(rb1, rb2, rb3, rb4, textField, clear);
        vbox.setSpacing(10);
        vbox.setStyle("-fx-background-color: silver;");

        HBox hbox = new HBox();
        hbox.getChildren().addAll(coordinates, shapeNumber);
        hbox.setSpacing(10);

        canvas.setOnMouseDragged(e -> {
                if (rb1.isSelected() && e.getX() > 0) {
                    canvas.getChildren().add(draw(e.getX(), e.getY(), inputColor, 2));
                } else if (rb2.isSelected()) {
                    canvas.getChildren().add(draw(e.getX(), e.getY(), Color.WHITE, 10));
                }
            });

        canvas.setOnMousePressed(e -> {
                if (rb3.isSelected() && e.getX() > 0) {
                    canvas.getChildren().add(draw(e.getX(), e.getY(), inputColor, 15));
                } else if (rb1.isSelected() && e.getX() > 0) {
                    canvas.getChildren().add(draw(e.getX(), e.getY(), inputColor, 2));
                } else if (rb2.isSelected()) {
                    canvas.getChildren().add(draw(e.getX(), e.getY(), Color.WHITE, 10));
                } else if (rb4.isSelected()) {
                    canvas.getChildren().add(image(e.getX(), e.getY()));
                }
            });

        canvas.setOnMouseMoved(e -> {
                coordinates.setText("(" + e.getX() + ", " + e.getY() + ")");
            });

        canvas.setOnMouseReleased(e -> {
                if (rb1.isSelected() || rb3.isSelected() || rb4.isSelected()) {
                    shapeCounter++;
                    shapeNumber.setText("Number of shape: " + shapeCounter);
                }
            });

        clear.setOnAction(e -> {
                canvas.getChildren().clear();
                shapeCounter = 0;
                shapeNumber.setText("Number of shape: " + shapeCounter);
            });

        BorderPane pane = new BorderPane();
        pane.setLeft(vbox);
        pane.setBottom(hbox);
        pane.setCenter(canvas);


        Scene scene = new Scene(pane);
        primaryStage.setTitle("CSPaint");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    private Circle draw(double x, double y, Color color, int radius) {
        Circle myCircle = new Circle(x, y, radius);
        myCircle.setFill(color);
        myCircle.setStroke(color);
        return myCircle;
    }

    private ImageView image(double x, double y) {
        Image linkedin = new Image("/linkedin.jpg");
        ImageView imageView = new ImageView(linkedin);
        imageView.setX(x);
        imageView.setY(y);
        imageView.setFitWidth(70);
        imageView.setFitHeight(100);
        return imageView;
    }

}