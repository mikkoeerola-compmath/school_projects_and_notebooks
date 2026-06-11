package fi.tuni.prog3.calc;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.control.Button;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;
import javafx.scene.layout.Background;
import javafx.scene.paint.Color;
import javafx.scene.layout.BackgroundFill;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import java.math.BigDecimal;



/**
 * JavaFX Calculator
 */
public class Calculator extends Application {

    @Override
    public void start(Stage stage) {
        
        GridPane gridPane = new GridPane();
        gridPane.setHgap(5);
        gridPane.setVgap(5);

        TextField op1 = new TextField();
        op1.setId("fieldOp1");
        TextField op2 = new TextField();
        op2.setId("fieldOp2");
        
        Label lab1 = new Label("First operand:");
        lab1.setId("labelOp1");
        Label lab2 = new Label("Second operand:");
        lab2.setId("labelOp2");
        
        Button addBtn = new Button();
        addBtn.setId("btnAdd");
        addBtn.setText("Add");
        Button subBtn = new Button();
        subBtn.setId("btnSub");
        subBtn.setText("Subtract");
        Button mulBtn = new Button();
        mulBtn.setId("btnMul");
        mulBtn.setText("Multiply");
        Button divBtn = new Button();
        divBtn.setId("btnDiv");
        divBtn.setText("Divide");
        
        Label labRes = new Label("Result:");
        labRes.setId("labelRes");
        
        Label fieldRes = new Label("");
        fieldRes.setMaxWidth(100);
        fieldRes.setId("fieldRes");
        
        BackgroundFill bfill = new BackgroundFill(Color.WHITE, null, null);
        Background backG = new Background(bfill);
        fieldRes.setBackground(backG);
        
        gridPane.add(lab1, 0, 0);
        gridPane.add(op1, 1, 0);
        gridPane.add(lab2, 0, 1);
        gridPane.add(op2, 1, 1);
        gridPane.add(addBtn, 0, 2);
        gridPane.add(subBtn, 1, 2);
        gridPane.add(mulBtn, 0, 3);
        gridPane.add(divBtn, 1, 3);
        gridPane.add(labRes, 0, 4);
        gridPane.add(fieldRes, 1, 4);
        
        var scene = new Scene(gridPane, 300, 200);
        stage.setScene(scene);
        stage.setTitle("Calculator");
        
        addBtn.setOnAction(new EventHandler<ActionEvent>() {
        
            @Override
            public void handle(ActionEvent e) {
                double a = Double.parseDouble(op1.getText());
                double b = Double.parseDouble(op2.getText());
                double result = a+b;
                BigDecimal bigR = BigDecimal.valueOf(result);
                bigR.stripTrailingZeros();
                fieldRes.setText(bigR.toPlainString());
            }
        });
        
        subBtn.setOnAction(new EventHandler<ActionEvent>() {
        
            @Override
            public void handle(ActionEvent e) {
                double a = Double.parseDouble(op1.getText());
                double b = Double.parseDouble(op2.getText());
                double result = a-b;
                BigDecimal bigR = BigDecimal.valueOf(result);
                bigR.stripTrailingZeros();
                fieldRes.setText(bigR.toPlainString());
            }
        });
        
        mulBtn.setOnAction(new EventHandler<ActionEvent>() {
        
            @Override
            public void handle(ActionEvent e) {
                double a = Double.parseDouble(op1.getText());
                double b = Double.parseDouble(op2.getText());
                double result = a*b;
                BigDecimal bigR = BigDecimal.valueOf(result);
                bigR.stripTrailingZeros();
                fieldRes.setText(bigR.toPlainString());
            }
        });
        
        divBtn.setOnAction(new EventHandler<ActionEvent>() {
        
            @Override
            public void handle(ActionEvent e) {
                double a = Double.parseDouble(op1.getText());
                double b = Double.parseDouble(op2.getText());
                double result = (b != 0)? a/b : 0;
                BigDecimal bigR = BigDecimal.valueOf(result);
                bigR.stripTrailingZeros();
                fieldRes.setText(bigR.toPlainString());
            }
        });
        
        
        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }

}