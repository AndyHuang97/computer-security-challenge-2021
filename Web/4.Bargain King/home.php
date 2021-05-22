<html>

<head>
	<title>Bargain Kingdom</title>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<style>
		table,
		th,
		td {
			border: 1px solid black;
		}
	</style>
</head>

<body>
	<h1 style="text-align:center">The Bargain Kingdom</b></h1>
	<h3 style="text-align:center">Unmissable offers for excellent condition second-hand home appliances.</3>
		<br>

		<div style="width: 100%; display: table;">
			<div style="display: table-row">

				<div style="width: 15%; display: table-cell;">
				</div>

				<div style="width: 30%; display: table-cell; border:1px solid black;">

					<h2 style="text-align:center">Appliances for sale:
					</h2>

					<form id="appliances_form" action="home.php">
					</form>
					<select style="margin-left: 80px;" name="appliance" form="appliances_form" onchange="document.getElementById('appliances_form').submit();">

						<?php
						echo "<option value=\"none\" selected disabled hidden>" . $_GET["appliance"] . "</option>";
						$db = 'db';
						$connection = new mysqli($db, "bargain_king", "supersecretpasswordnotsureweevenneedit", "bargain_kingdom_db");

						$query = "SELECT name FROM appliances;";
						$results = $connection->query($query);
						if ($results) {
							while ($row = $results->fetch_assoc()) {
								echo "<option value=\"" . $row["name"] . "\">" . $row["name"] . "</option>";
							}
						}
						$connection->close();
						?>

					</select>

					<br><br><br>

					<div style="width: 100%; display: table;">
						<div style="display: table-row">

							<?php
							$db = 'db';
							$connection = new mysqli($db, "bargain_king", "supersecretpasswordnotsureweevenneedit", "bargain_kingdom_db");

							if (!$_GET["appliance"]) {
								$query = "SELECT appliances.name, appliances.price_new, appliances.price_used, images.path FROM appliances, images WHERE appliances.image=images.id;";
							} else {
								$query = "SELECT appliances.name, appliances.price_new, appliances.price_used, images.path FROM appliances, images WHERE appliances.image=images.id and appliances.name=\"" . urldecode($_GET["appliance"]) . "\";";
							}

							$results = $connection->query($query);
							$row = $results->fetch_assoc();

							if (!$row) {
								echo "<p style=\"color:red;\">404: appliance " . urldecode($_GET["appliance"]) . " was not found in bargain_kingdom_db</p>";
								return;
							}

							$path = $row["path"];
							$name = $row["name"];
							$price_new = $row["price_new"];
							$price_used = $row["price_used"];

							echo "<div style=\"width: 50%; height:100%; display: table-cell;\">";
							echo "<img src=\"" . $path . "\" width=\"250\" height=\"250\">";
							echo "</div>";
							echo "<div style=\"width:50%; height:100%; display: table-cell;\">";
							echo "<p font-size:22px\"><b>Name:</b>" . $name . "</p>";
							echo "<p font-size:22px\"><b>Our Starting Price:</b>" . $price_used . "</p>";
							echo "<p font-size:22px\"><b>Original Price:</b>" . $price_new . "</p>";
							echo "</div>";
							?>
						</div>
					</div>
				</div>

				<div style="width: 4%; display: table-cell;">
				</div>

				<div style="width: 35%; display: table-cell; border:1px solid black;">
					<h2 style="text-align:center;">Last 5 Bids:
	</h3>
	<table style="border:1px solid black; margin-left:120px;">
		<tr>
			<th>Email</th>
			<th>Bid Price</th>
			<th>Date</th>
		</tr>

		<?php
		$db = 'db';
		$connection = new mysqli($db, "bargain_king", "supersecretpasswordnotsureweevenneedit", "bargain_kingdom_db");
		$query = $connection->prepare("SELECT email, price, bid_date FROM bids WHERE appliance = ? ORDER BY price DESC");
		$appliance = urldecode($_GET["appliance"]);
		$query->bind_param('s', $appliance);
		$query->execute();
		$results = $query->get_result();
		$count = 0;

		while (($row = $results->fetch_assoc()) && $count < 5) {
			$email = $row["email"];
			$price = $row["price"];
			$date = $row["bid_date"];

			$price_color = "color: black";
			if ($price < $price_used) {
				$price = $price . "(invalid)";
				$price_color = "color: red";
			}

			echo "<tr><td>" . $email . "</td> <td style=\"" . $price_color . "\">" . $price . "</td><td>" . $date . "</td></tr>";
			$count += 1;
		}

		for (; $count < 5; $count += 1) {
			echo "<tr><td>-</td><td>-</td><td>-</td>";
		}

		?>

	</table>

	<br> <br> <br>

	<form action="/bid.php" method="post" style="margin-left:40px">
		<label for="email">email:</label><br>
		<input type="email" id="email" name="email"><br>
		<label for="price">price:</label><br>
		<input type="number" id="price" name="price" value=<?php echo $price_used; ?>><br><br>
		<input type="hidden" id="appliance" name="appliance" value="<?php echo urldecode($_GET["appliance"]); ?>">
		<input type="submit" value="Submit">
	</form>

	</div>

	<div style="width: 15%; display: table-cell;">
	</div>

	</div>
	</div>
</body>


</html>