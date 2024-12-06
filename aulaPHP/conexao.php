
<!-- 
//     session_start();
//     include("com.php");


// if(empty($_GET["nome"]) || empty($_GET["senha"])){
//     header("location:login.html");
//     exit();

// }



// -->



<?php


session_start();
include("com.php");
$nome = mysqli_real_escape_string($con, $_GET["nome"]);

$senha = mysqli_real_escape_string($con, $_GET["senha"]);


echo $nome."nome".$senha . "<br><br>";
if (empty($nome) || empty($senha)) {

    echo "<script>
            alert('Por favor, preencha todos os campos.');
            setTimeout(function(){
                window.location.href = 'login.html';
            }, 2000); // Espera 2 segundos antes de redirecionar
          </script>";
    exit(); 
}

$query = "select * from usuario where usuario = '{$nome}' and senha = '{$senha}' ";



$result = mysqli_query($con, $query);

$retorno = mysqli_fetch_array($result);

$row = mysqli_num_rows($result);

echo $row;

if(!$row) {
    
    echo "<script>
            alert('Não existe!!! .');
            setTimeout(function(){
                window.location.href = 'login.html';
            }, 2000); // Espera 2 segundos antes de redirecionar
          </script>";
    exit(); 
} else {
    $_SESSION["nome"] = $nome;
    $_SESSION["setor"] = $retorno["adm"];

    header("location:admin.php");
    exit();

} 



?>