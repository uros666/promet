<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Uroš Skrt</h1>
    <?php
        // DB config.
        require_once 'db_config.php';

        $conn = new mysqli($servername, $username, $password, $database);

        if ($conn->connect_error) {
            die("Povezava ni uspela: " . $conn->connect_error);
        }

        $sql = "SELECT stevilka, datum_zig, stevilo, kraj FROM prehod_avtomobilov;";
        $result = $conn->query($sql);

        while ($row = $result->fetch_assoc()) {
            echo "stevilka" . $row["stevilka"] .  " | datum" . $row["datum_zig"] . 
                " | stevilo" . $row["stevilko"]." | kraj" . $row["kraj"] . "<br>";
        }

        $conn->close();
    ?>
</body>
</html>
