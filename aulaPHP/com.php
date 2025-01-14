<?php

$host = "127.0.0.1";
$usuario = "root";
$senha =  "";
$db = "aula";

$con = new mysqli($host, $usuario, $senha, $db);



if($con -> connect_errno){
    "Falha na conexão: (".$con->connect_errno.")".$con->connect_errno;
} 
else {
    echo 'oi';
}
?>

