<?php

    session_start();
    if(!$_SESSION['nome']){
        header('location:login.html');
        exit();
    }


    if($_SESSION['setor'] == 0){

        header('location:retornouser.php');
        exit();
        
    }
?>


