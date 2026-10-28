<?php
//Escribe un script PHP que sobre un array de temperaturas realice las siguientes operaciones: 
//Calcular la media. Calcular el valor máximo. Calcular el valor mínimo. 
//Mostrar todos los valores calculados. El array de temperaturas lo vamos a generar con números aleatorios. 
//El array será de 10 elementos y los valores aletorios generados estarán entre 1 y 30.

$array = [];
for($i = 0; $i < 10; $i++) {
    $array[$i] = rand(1,30);
}

for ($i=0; $i < count($array); $i++) { 
    echo 'Indice: ' . $i . ' Valor: ' . $array[$i] . '<br>';
}

$total = 0;
for ($i=0; $i < count($array); $i++) { 
    $total = $total + $array[$i];
}

$media = $total / count($array);

echo 'Temperatura media ' . $media;

$maximo = 0;
for ($i=0; $i < count($array); $i++) { 
    if ($array[$i] > $maximo) {
        $maximo = $array[$i];
    }
}

echo 'Temperatura máxima ' . $maximo;

$minimo = min($array);

echo 'Temperatura minima ' . $minimo;

?>