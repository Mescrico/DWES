<?php
//Generar el numero aleatorio 

$dado = rand(1,6);

// Meter el condicional para seleccionar la imagen correcta
if($dado == 1){
    $imagen = "https://upload.wikimedia.org/wikipedia/commons/1/1b/Dice-1-b.svg";
} else if ($dado == 2) {
    $imagen = "https://upload.wikimedia.org/wikipedia/commons/5/5f/Dice-2-b.svg";
} else if ($dado == 3) {
    $imagen = "https://upload.wikimedia.org/wikipedia/commons/b/b1/Dice-3-b.svg";
} else if ($dado == 4) {
    $imagen = "https://upload.wikimedia.org/wikipedia/commons/f/fd/Dice-4-b.svg";
} else if ($dado == 5) {
    $imagen = "https://upload.wikimedia.org/wikipedia/commons/0/08/Dice-5-b.svg";
} else {
    $imagen = "https://upload.wikimedia.org/wikipedia/commons/2/26/Dice-6-b.svg";
}

//Mostrar el resultado
echo "Resultado del dado: " . $dado . "<br><br>"
echo '<img src="' . $imagen . '" width="150" alt="dado" >';


?>