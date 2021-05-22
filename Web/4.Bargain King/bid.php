<?php

if ($_POST["price"] && $_POST["email"] && $_POST["appliance"]) {
    $db = 'db';
    $connection = new mysqli($db, "bargain_king", "supersecretpasswordnotsureweevenneedit", "bargain_kingdom_db");

    $query = $connection->prepare("INSERT INTO bids (email, price, appliance, bid_date) VALUES(?, ?, ?, NOW())");
    $query->bind_param('sis', urldecode($_POST["email"]), urldecode($_POST["price"]), urldecode($_POST["appliance"]));
    $query->execute();
}

header("Location: ./home.php?appliance=" . urldecode($_POST["appliance"]));
exit();
?>


Bradley@bargainkingdom.com', (SELECT password from USERS where email='Bradley@bargainkingdom.com')) --