<?php
//Escribe una función que reciba dos parámetros de entrada (inicio y fin) y que imprima las tablas demultiplicar entre esos dos números. 
//Utilice la función del ejercicio anterior.

$inicio = filter_input(INPUT_GET, 'inicio', FILTER_VALIDATE_INT);
$fin = filter_input(INPUT_GET, 'fin', FILTER_VALIDATE_INT);

function TablaMultiplicar(int $numero) {
    for ($i=1; $i <= 10; $i++) { 
        $resultado = $i*$numero;
        echo 'Multiplicacion ' . $i . 'x' . $numero . ' = ' . $resultado . '<br>';
    }
}

function TablaMultiplicarDos(int $inicio, int $fin) {
    for($j = $inicio; $j <= $fin; $j++) {
        TablaMultiplicar($j);
        echo '<br>';
    }
}
if($inicio === null || $fin === null) {
    echo 'No has puesto ningun numero';
} else {
    TablaMultiplicarDos($inicio, $fin);
}

?>