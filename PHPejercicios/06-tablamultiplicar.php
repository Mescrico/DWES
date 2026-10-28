<?php
//Escribe una función que reciba un número como parámetro de entrada y que imprima su tabla de multiplicar.

$numero = filter_input(INPUT_GET, 'numero', FILTER_VALIDATE_INT);

function TablaMultiplicar(int $numero) {
    for ($i=1; $i <= 10; $i++) { 
        $resultado = $i*$numero;
        echo 'Multiplicacion ' . $i . 'x' . $numero . ' = ' . $resultado . '<br>';
    }
}
if($numero === null) {
    echo 'No has puesto ningun numero';
} else {
    TablaMultiplicar($numero);
}

?>