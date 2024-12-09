<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>PixelBytes</title>
    <!-- Link to favicon -->
    <link rel="PixelBytes Icon" href="../media/gear.png" type="image/x-icon" />
    <link rel="stylesheet" href="../css/style.css" />
    <script src="../js/selectScript.js" defer></script>
</head>
<body class="body">
<header>
    <nav class="nav">
        <a href="../index.php"><img src="../media/gear.png" alt="PixelBytes Logo" height="25px" /></a>
        <div class="logo">PixelBytes</div>
        <div class="food">
      </div>
        <ul>
          <li><a href="../index.php">Home</a></li>
          <li><a href="./learn.php">Learn</a></li>
          <li><a href="./lessons.php">Lessons</a></li>
          <!-- <li><a href="./html/login.html">Login</a></li> ? -->
        </ul>
      </nav>
</header>
<div class="lessonContainer">
    <div class="dropdownContainer">
        <div class="dropdown">
            <form name="form1" id="form1" action="/html/questions.php">
                Subjects: 
                <select name="subject" id="subject">
                    <option value="" selected="selected">Select subject</option>
                </select>
                <br><br>
                Level: 
                <select name="level" id="level">
                    <option value="" selected="selected">Please select subject first</option>
                </select>
                <br><br>
                Category: 
                <select name="category" id="category">
                    <option value="" selected="selected">Please select level first</option>
                </select>
                <br><br>
                <input type="submit">
            </form>
        </div>
    </div>
</div>
</body>
</html>

