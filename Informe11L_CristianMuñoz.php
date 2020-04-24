<?php

function generador()
{
	$meses=['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic'];
	$ciudades=["Bucaramanga","Floridablanca","Girón","Piedecuesta"];
	
	$ingresos = array(
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0)
	);
	$filas_in=count($ciudades);
	$columnas_in=count($meses);
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
	$meses=['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic'];
	$ciudades=["Bucaramanga","Floridablanca","Girón","Piedecuesta"];
	
	$egresos = array(
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0)
	);

	$filas_eg=count($egresos);
	$columnas_eg=count($meses);
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
	
	$filas=count($ciudades);
	$columnas=count($meses);
	print "El arreglo tiene ".$filas." filas y ".$columnas." columnas"."<br>";
	for ($i=0;$i<$columnas;$i++) {
		if ($i!=$columnas-1) {
			print $meses[$i].", ";
		}
		else
		{
			print $meses[$i];
		}
	}
	print "<br>";
	for ($i=0;$i<$filas;$i++) {
		print $ciudades[$i].": ";
		for ($i1=0;$i1<$columnas;$i1++) {
			if ($i1!=($columnas-1))
			{
				print $arreglo[$i][$i1].", ";
			}
			else
			{
				print $arreglo[$i][$i1];
			}
		}
		print "<br>";
	}
}
function restador($ingresos, $egresos)
{
	$meses=['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic'];
	$ciudades=["Bucaramanga","Floridablanca","Girón","Piedecuesta"];
	
	$ganancias = array(
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0)
	);

	$filas=count($ciudades);
	$columnas=count($meses);
	for ($i=0;$i<$filas;$i++) {
		for ($i1=0;$i1<$columnas;$i1++) {
			$resta=$ingresos[$i][$i1]-$egresos[$i][$i1];
			$ganancias[$i][$i1]=$resta;
		}
	}
	return $ganancias;
}
function generador3D_ingresos($ingresos)
{
	$meses=['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic'];
	$ciudades=["Bucaramanga","Floridablanca","Girón","Piedecuesta"];
	$filas=count($ciudades);
	$columnas=count($meses);
	
	$ingresos_2018 = array(
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0)
	);	
	for ($i=0;$i<$filas;$i++)
	{
		for ($i1=0;$i1<$columnas;$i1++) 
		{
			$ingresos_2018[$i][$i1]=round($ingresos[$i][$i1]*(1-(9.5/100)),2);
		}
	}
	$ingresos_2017 = array(
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0)
	);
	for ($i=0;$i<$filas;$i++) {
		for ($i1=0;$i1<$columnas;$i1++) {
			$ingresos_2017[$i][$i1]=round($ingresos_2018[$i][$i1]*(1-(9.5/100)),2);
		}
	}
	$ingresos_2016 = array(
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0)
	);
	for ($i=0;$i<$filas;$i++) {
		for ($i1=0;$i1<$columnas;$i1++) {
			$ingresos_2016[$i][$i1]=round($ingresos_2017[$i][$i1]*(1-(9.5/100)),2);
		}
	}
	$ingresos_2015 = array(
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0)
	);
	
	for ($i=0;$i<$filas;$i++) {
		for ($i1=0;$i1<$columnas;$i1++) {
			$ingresos_2015[$i][$i1]=round($ingresos_2016[$i][$i1]*(1-(9.5/100)),2);
		}
	}
	$ingresos3D=array($ingresos_2015,$ingresos_2016,$ingresos_2017,$ingresos_2018,$ingresos);
	return $ingresos3D;
}
function generador3D_egresos($egresos)
{
	$meses=['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic'];
	$ciudades=["Bucaramanga","Floridablanca","Girón","Piedecuesta"];
	$filas=count($ciudades);
	$columnas=count($meses);

	$egresos_2018 = array(
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0)
	);
	for ($i=0;$i<$filas;$i++) {
		for ($i1=0;$i1<$columnas;$i1++) {
			$egresos_2018[$i][$i1]=round($egresos[$i][$i1]*(1-(9.5/100)),2);
		}
	}
	$egresos_2017 = array(
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0)
	);
	for ($i=0;$i<$filas;$i++) {
		for ($i1=0;$i1<$columnas;$i1++) {
			$egresos_2017[$i][$i1]=round($egresos_2018[$i][$i1]*(1-(9.5/100)),2);
		}
	}
	$egresos_2016 = array(
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0)
	);
	for ($i=0;$i<$filas;$i++) {
		for ($i1=0;$i1<$columnas;$i1++) {
			$egresos_2016[$i][$i1]=round($egresos_2017[$i][$i1]*(1-(9.5/100)),2);
		}
	}
	$egresos_2015 = array(
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0),
	array(0 , 0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0)
	);
	for ($i=0;$i<$filas;$i++) {
		for ($i1=0;$i1<$columnas;$i1++) {
			$egresos_2015[$i][$i1]=round($egresos_2016[$i][$i1]*(1-(9.5/100)),2);
		}
	}
	$egresos3D=array($egresos_2015,$egresos_2016,$egresos_2017,$egresos_2018,$egresos);
	return $egresos3D;
}
function imprimir3D($arreglo3D)
{
	$meses=['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic'];
	$ciudades=["Bucaramanga","Floridablanca","Girón","Piedecuesta"];
	
	$cont_ciudades=0;
	$año=2015;
	$año_prohibido=2020;
	$filas=count($ciudades);
	$columnas=count($meses);
	print "<br>"."Año ".$año."<br>"."<br>";
	print $meses[0].", ".$meses[1].", ".$meses[2].", ".$meses[3].", ".$meses[4].", ".$meses[5].", ".$meses[6].", ".$meses[7].", ".$meses[8].", ".$meses[9].", ".$meses[1].", ".$meses[11];
	for ($i=0;$i<5;$i++) {
		print "<br>".$ciudades[$cont_ciudades].": ";
		for ($i1=0;$i1<$filas;$i1++) {
			for ($i2=0;$i2<$columnas;$i2++) {
				if ($i2!=$columnas-1) {
					print $arreglo3D[$i][$i1][$i2].", ";
				} else {
					print $arreglo3D[$i][$i1][$i2];
				}
			}
			$cont_ciudades=$cont_ciudades+1;
			print "<br>".$ciudades[$cont_ciudades].": ";
		}
		$cont_ciudades=0;
		if ($i!=5-1)
		{
			$año=$año+1;
			print "<br>"."Año ".$año."<br>"."<br>";
			print $meses[0].", ".$meses[1].", ".$meses[2].", ".$meses[3].", ".$meses[4].", ".$meses[5].", ".$meses[6].", ".$meses[7].", ".$meses[8].", ".$meses[9].", ".$meses[1].", ".$meses[11];
		}
	}
}
function calcular_ganacias3D($arreglo_1_3D,$arreglo_2_3D)
{
	$años=5;
	$filas=4;
	$columnas=12;
	$ganancias=$arreglo_1_3D;
	for ($i=0;$i<$años;$i++)
	{
		for ($i1=0;$i1<$filas;$i1++)
		{
			for ($i2=0;$i2<$columnas;$i2++)
			{
				$resta=$arreglo_1_3D[$i][$i1][$i2]-$arreglo_2_3D[$i][$i1][$i2];
				$ganancias[$i][$i1][$i2]=$resta;
			}
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
$ingresos3D=generador3D_ingresos($ingresos);
$egresos3D=generador3D_egresos($egresos);
print "<br>"."Arreglo ingresos3D"."<br>";
imprimir3D($ingresos3D);
print "<br>"."Arreglo egresos3D"."<br>";
imprimir3D($egresos3D);
print "<br>"."Arreglo ganancias3D"."<br>";
imprimir3D(calcular_ganacias3D($ingresos3D,$egresos3D));
?>
