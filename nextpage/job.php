<!DOCTYPE HTML>  
<html>
<head>
<style>
.error {color: #FF0000;}
</style>
</head>
<body>  

<?php
// define variables and set to empty values
$nameErr = $locationErr = $genderErr = $websiteErr = "";
$name = $location = $gender = $comment = $website = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  if (empty($_POST["name"])) {
    $nameErr = "Name is required";
  } else {
    $name = test_input($_POST["name"]);
    // check if name only contains letters and whitespace
    if (!preg_match("/^[a-zA-Z-' ]*$/",$name)) {
      $nameErr = "Only letters and white space allowed";
    }
  }
  
  if (empty($_POST["location"])) {
    $locationErr = "location is required";
  } else {
    $location = test_input($_POST["location"]);
    // check if e-mail address is well-formed
  }
    
  if (empty($_POST["skills_req"])) {
    $skills_req = "";
  } else {
    $skills_req = test_input($_POST["skills_req"]);
    // check if URL address syntax is valid (this regular expression also allows dashes in the URL)
    // if (!preg_match("/\b(?:(?:https?|ftp):\/\/|www\.)[-a-z0-9+&@#\/%?=~_|!:,.;]*[-a-z0-9+&@#\/%=~_|]/i",$website)) {
    //   $websiteErr = "Invalid URL";
    // }
  }

  if (empty($_POST["vanancies"])) {
    $vanancies = "";
  } else {
    $vanancies = test_input($_POST["vanancies"]);
  }

  if (empty($_POST["gender"])) {
    $genderErr = "Gender is required";
  } else {
    $gender = test_input($_POST["gender"]);
  }
}

function test_input($data) {
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}
?>

<h2>PHP Form Validation Example</h2>
<p><span class="error">* required field</span></p>
<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">  
  Name of Company: <input type="text" name="name" value="<?php echo $name;?>">
  <span class="error">* <?php echo $nameErr;?></span>
  <br><br>
  Location <input type="text" name="location" value="<?php echo $location;?>">
  <span class="error">* <?php echo $locationErr;?></span>
  <br><br>
  skills_req: <input type="text" name="skills_req" value="<?php echo $skills_req;?>">
  <span class="error"><?php echo $skills_reqErr;?></span>
  <br><br>
  vanancies: <input type="number" name="vanancies" value="<?php echo $vanancies;?>">
  <span class="error"><?php echo $vananciesErr;?></span>
  <br><br>
  <input type="submit" name="submit" value="Submit">  
</form>

<?php
echo "<h2>Your Input:</h2>";
echo $name;
echo "<br>";
echo $location;
echo "<br>";
echo $skills_req;
echo "<br>";
echo $vanancies;
echo "<br>";
echo $gender;
?>

</body>
</html>


</body>
</html>
