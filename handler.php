<!DOCTYPE html>
<html>
  <head>
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
    <link rel="stylesheet" href="https://code.getmdl.io/1.3.0/material.indigo-pink.min.css">
    <script defer src="https://code.getmdl.io/1.3.0/material.min.js"></script>
    <title>Welcome Page</title>
  </head>

  <body>
    
    <?php
    $Pizza = "";
    if ( isset( $_POST['Pizza'] ) ){
      $Pizza = $_POST['Pizza'];
    }
    echo "<h1>My Program</h1>\n";
    echo "<p>My Variable is = ".$Pizza."</p>\n";
    ?>
    
  </body>
  
</html>
