<?php

if($_SESSION['setor']!= 'admin'){
    header("location:login.html")
    exit();
}

?>