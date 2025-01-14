
<?php

include("conn.php");
$nome = mysqli_real_escape_string($con, $_POST["nome"]);

$senha = mysqli_real_escape_string($con, $_POST["senha"]);


echo $nome."nome".$senha;
if (empty($nome) || empty($senha)) {
echo $row;
}


?>