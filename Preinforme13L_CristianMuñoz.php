<?php
$Supercomputadoras = array(
    array('Summit' , '2414592' , '148600' , '200794'),
    array('Sierra' , '1572480' , '94640' , '125712'),
    array('Sunway TaihuLight' , '10649600' , '93014' , '125435'),
    array('Tianhe-2A' , '4981760' , '61444' , '100678'),
    array('Frontera' , '448448' , '23516' , '38745'),
    array('Piz Daint' , '387872' , '21230' , '27154'),
    array('Trinity' , '979072' , '20158' , '41461'),
    array('AI Bridging Cloud Infrastructure (ABCI)' , '391680' , '19880' , '32576'),
    array('SuperMUC-NG' , '305856' , '19476' , '26873'),
    array('Lasen' , '288288' , '18200' , '23047')
);

//Lista de listas de las supercomputadoras según su promedio de los valores asignados, imprimir la supercomputadora con su respectivo promedio

$lista_promedio=[];
$niveles=count($Supercomputadoras);
$columnas=4;
for ($i=0;$i<$niveles;$i++) {
	$promedio=0;
	$suma=0;
	$cont=0;
	for ($i1=1;$i1<$columnas;$i1++) {
		$suma+=intval($Supercomputadoras[$i][$i1]);
		$cont+=1;
	}
	$promedio=round($suma/$cont,2);
	$lista_variable=[$Supercomputadoras[$i][0],$promedio];
	$lista_promedio[$i]=$lista_variable;
}
$long=count($lista_promedio);
print "Lista de las supercomputadoras según su promedio de los valores asignados:"."<br>";
for ($i=0;$i<$long;$i++) {
	print $lista_promedio[$i][0].': '.$lista_promedio[$i][1]."<br>";
}

//Con base en el primer punto halle la desviación estandar para cada supercomputadora

for ($i=0;$i<$long;$i++) {
	$sumatoria=0;
	for ($i1=1;$i1<$columnas;$i1++) {
		$sumatoria+=($lista_promedio[$i][1]-intval($Supercomputadoras[$i][$i1]))**2;
	}
	$varianza=($sumatoria)/($columnas-2);
	$desviación_estandar=round($varianza**0.5,2);
	print "La desviación estandar de los valores de la supercomputadora".$Supercomputadoras[$i][0]."es: ".$desviación_estandar."<br>";
}
	
//Crear un diccionario el cual contenga las supercomputadoras con su máximo de T/Flops y el usuario pueda modificar el máximo de T/Flops de la supercomputadora que él desee, se podrá modificar las veces que se quiera pero los cambios no quedarán guardados

if (isset($_POST['resultado'])) {
	$cont=0;
	print "<br>";
	for ($i=0;$i<$niveles;$i++) {
		print $cont.'->'.$Supercomputadoras[$i][0]."<br>";
		$cont+=1;
	}
	$n1=$_POST['n1'];
	$n2=$_POST['n2'];
	$Supercomputadoras_TFlops=array();
	for ($i=0;$i<$niveles;$i++) {
		if ($i!=$n1) {
			$Supercomputadoras_TFlops[$i]=array($Supercomputadoras[$i][0]=>$Supercomputadoras[$i][3]);
		}
		else {
			$Supercomputadoras_TFlops[$i]=array($Supercomputadoras[$i][0]=>$n2);
		}
	}
	print_r($Supercomputadoras_TFlops);
}

?>
<html>
<body>
<form action="Preinforme13L_CristianMuñoz.php" method="post" name="calcular">
	<label> Ingrese el número correspondiente para la supercomputadora que usted desee modificar sus T/Flops:</label>
	<input type="text"name="n1"/><br/>
	<label> Ingrese la cantidad máxima de T/Flops que desea agregarle la supercomputadora: </label>
	<input type="text"name="n2"/><br/>
	<input type="submit" name="resultado"value="Ver resultado"/>
</form>

</body>
</html>
