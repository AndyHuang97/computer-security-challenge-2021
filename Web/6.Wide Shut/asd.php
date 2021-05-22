<?php
    if(isset($_GET['source'])){
        die(highlight_file(__FILE__));
    }

 # Since I implemented password hashing the following code doesn't work. I don't know why
    if(isset($_POST['username']) && $_POST['password']){
        
        if(is_array($_POST['username']) || is_array($_POST['password'])){
            die('Invalid data');
        }

        if($_POST['username'] == '' || $_POST['password'] == ''){
            die('Invalid data');
        }
        
        include 'sql.php';

        
        $user = $_POST['username'];
        $pwd = $_POST['password'];

        # I don't want SQL Injections !!
        $user = str_replace("'", "\\'", $user);
        $user = str_replace("\"", "\\\"", $user);

        # now hash the user supplied password for later user
        $password_hashed = sha1($pwd);

        # Check if there is a user account with that username. 
        $query1 = "SELECT password FROM users WHERE username = '$user'";
        $user = query($query1);

        if(count($user) == 0 ){
            die('Invalid username or password');
        }
        
        $password = $user[0]['password'];
        
        # Because I'm a security expert, I store every password hash in another table
        # Retrieve the hashed password and the pepper from the database
        $query2 = "SELECT hash,pepper FROM hashed_passwords WHERE password = '$password'";
        $res = query($query2)[0];
        
        # For improved security, rehash the password with the pepper
        $saved_pwd = md5($res['hash'] . $res['pepper']);
        
        # check if the hash of the submitted password is the same of the database
        if($password_hashed == $saved_pwd){
            # Success! you are logged in! GG
            $flash = $flag;
        }

    }

    ?>

<!DOCTYPE html>
<html>
<head>
        <!-- CSS only -->
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">

<!-- JS, Popper.js, and jQuery -->
<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
<title>JackSecurity</title>
</head>
<body>
    <div class="main">
        <div class="container">
            <div class="row">
                <h1>Jack Security</h1>
            </div>
            <div class="row mt-3">
                <p class="lead">
                I made <a href='/?source'>this</a> login for my website.
</p>
<p class="lead">
                I read online that I have to "crypt" passwords on the database, but I'm not sure I have implemented correctly. Even with the right user/password I can not log in. Can you help me?
                </p>
            </div>
        </div>
    <?php
        if(isset($flash)){
            echo "<div class=\"container\">$flash</div>";
        }
    ?>  

    <div class="container mt-5">
        <div class="row justify-content-center">
            <form method=POST>
                <div class="form-group">
                    <input class="form-control" type=text name=username placeholder=Username>
                </div>
                <div class="form-group">
                    <input class="form-control" type=password name=password placeholder=Password>
                </div>
                <button type="submit" class="btn btn-primary">Submit</button>
            </form>
        </div>
    </div>
    </div>
</body>
</html> 1