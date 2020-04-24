<?php

$meses=['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic'];
$ciudades=["Bucaramanga","Floridablanca","Girón","Piedecuesta"];

function generador()
{
	$ingresos = array(
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0)
	);
	$filas_in=4;
	$columnas_in=12;
	for ($i=0;$i<$filas_in;$i++) {
		for ($i1=0;$i1<$columnas_in;$i1++) {
			$numero_aleatorio_ingresos=rand(100,180);
			$ingresos[$i][$i1]=$numero_aleatorio_ingresos;
		}
	}
	return $ingresos;
}
function generador_1()
{
	$egresos = array(
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0)
	);

	$filas_eg=4;
	$columnas_eg=12;
	for ($i=0;$i<$filas_eg;$i++) {
		for ($i1=0;$i1<$columnas_eg;$i1++) {
			$numero_aleatorio_egresos=rand(60,130);
			$egresos[$i][$i1]=$numero_aleatorio_egresos;
		}
	}
	return $egresos;
}
function imprimir($arreglo)
{
	$meses=['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic'];
	$ciudades=["Bucaramanga","Floridablanca","Girón","Piedecuesta"];
	$filas=4;
	$columnas=12;
	print "El arreglo tiene ".$filas." filas y ".$columnas." columnas"."<br>";
	for ($i=0;$i<count($meses);$i++) {
		print $meses[$i].", ";
	}
	print "<br>";
	for ($i=0;$i<$filas;$i++) {
		print $ciudades[$i].": ";
		for ($i1=0;$i1<$columnas;$i1++) {
			print $arreglo[$i][$i1].", ";
		}
		print "<br>";
	}
}
function restador($ingresos, $egresos)
{
	$ganancias = array(
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0)
	);

	$filas_in=4;
	$columnas_in=12;
	$filas_eg=4;
	$columnas_eg=12;
	for ($i=0;$i<$filas_in;$i++) {
		for ($i1=0;$i1<$columnas_in;$i1++) {
			$resta=$ingresos[$i][$i1]-$egresos[$i][$i1];
			$ganancias[$i][$i1]=$resta;
		}
	}
	return $ganancias;
}

$ingresos=generador();
$egresos=generador_1();
$ganancias=restador($ingresos,$egresos);
print "Arreglo ingresos:"."<br>";
imprimir($ingresos);
print "<br>"."Arreglo egresos:"."<br>";
imprimir($egresos);
print "<br>"."Arreglo ganancias:"."<br>";
imprimir($ganancias);
?>
