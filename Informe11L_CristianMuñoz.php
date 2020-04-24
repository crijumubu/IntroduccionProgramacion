<?php

$meses=['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic'];
$ciudades=["Bucaramanga","Floridablanca","Girón","Piedecuesta"];

function generador()
{
	$ingresos = array(
    array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
    array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
    array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
    array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0));

	$egresos = array(
    array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
    array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
    array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
    array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0));

	$filas_in=4;
	$columnas_in=12;
	for ($i=0;$i<$niveles_in;$i++)
	{
		for ($i1=0;$i<$columnas_in;$i++)
		{
			$numero_aleatorio_ingresos=rand(100,180);
			$numero_aleatorio_egresos=rand(60,130);
			$ingresos[$i][$i1]=$$numero_aleatorio_ingresos;
			$egresos[$i][$i1]=$$numero_aleatorio_egresos;
		}
	}
	return $ingresos,$egresos;
}
function imprimir($arreglo)
{
	$filas=4;
	$columnas=12;
	print "El arreglo tiene ".$filas." filas y ".$columnas." columnas";
	print $meses;
	for ($i=0;$i<$filas;$i++)
	{
		print $ciudades[$i],$arreglo[$i];
	}
}
function restador($ingresos,$egresos)
{
	$ganancias = array(
    array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
    array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
    array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
    array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0));

	$filas_in=4;
	$columnas_in=12;
	$filas_eg=4;
	$columnas_eg=12;
	for ($i=0;$i<$filas_in)
	{
		$resta=$ingresos[$i][$i1]-$egresos[$i][$i1];
		$ganancias[$i][$i1]=$resta;
	}
	return $ganancias;
}
$ingresos,$egresos=generador();
imprimir($ingresos);
imprimir($egresos);
imprimir($ganancias);
?>