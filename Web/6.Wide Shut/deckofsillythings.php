<?php require_once 'config.php'; ?>
<!doctype html>
<html lang="en">
<head>
    <title>D&D Deck of Silly Things</title>
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">
    <meta charset="utf8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
<div class="container" style="max-width: 600px; margin-top: 2em;">
<div><h1>The D&D Deck of Silly Things</h1></div>

    <div>
        <table style="width:100%" >
            <tr>
                <td>0</td>
                <td>Backside</td>
            </tr>
            <tr>
                <td>1</td>
                <td>Sand of the Pocket</td>
            </tr>
            <tr>
                <td>2</td>
                <td>Comb of Beardmancy</td>
            </tr>
            <tr>
                <td>3</td>
                <td>Pen of Vapor</td>
            </tr>
            <tr>
                <td>4</td>
                <td>Monkey Wrench</td>
            </tr>
            <tr>
                <td>5</td>
                <td>Seal of Approval</td>
            </tr>
            <tr>
                <td>6</td>
                <td>Tail of the Duck</td>
            </tr>
            <tr>
                <td>7</td>
                <td>Ring of Finger Gun</td>
            </tr>
            <tr>
                <td>8</td>
                <td>World's Best Mug</td>
            </tr>
            <tr>
                <td>9</td>
                <td>Armor of Plot</td>
            </tr>
        </table>
    </div>
<?php

if(isset($_REQUEST['imgnumber'])){
    $image = $_REQUEST['imgnumber'];
}else{
    $image = null;
}
if(!empty($image)){
    $query = "SELECT * FROM images WHERE id = '" . $image . "';";
    $result = mysqli_query($vuln_db, $query);
    if ( $result != FALSE && mysqli_num_rows($result)>0){
        echo "<h1>Here's your card!</h1>";
        echo "<img style='width: 100%' src=img/" . $image . ".jpg >";
    }
    else {
        echo '<div class="alert alert-danger">Image not found</div>';
    }
}else{
?>
    <form method="post" id="image_form" class="form-horizontal" style="max-width: 75%; margin: 0 auto;">
        <div class="form-group">
            <label for="name">Choose an item number to show the related item card: </label>
            <input type="text" name="imgnumber" class="form-control">
        </div>
        <input type="submit" value="Enter" class="btn btn-primary" style="display: block; margin: 0 auto; min-width: 50%">
    </form>
<?php
}
?>

</div>
</body>
</html>