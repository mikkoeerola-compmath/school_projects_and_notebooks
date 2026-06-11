module fi.tuni.prog3.mavenproject1 {
    requires javafx.controls;
    requires javafx.fxml;

    opens fi.tuni.prog3.mavenproject1 to javafx.fxml;
    exports fi.tuni.prog3.mavenproject1;
}
